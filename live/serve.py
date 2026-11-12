#!/usr/bin/env python3
"""Live reader: a local page the reader reads while their agent writes ahead.

  python3 live/serve.py serve <state_dir> [--port 8787]
  python3 live/serve.py wait  <state_dir> [--timeout 600]

<state_dir> is normally reader/<book-id>/live/. It holds:
  pages.jsonl    one JSON page per line, appended by the agent
  events.jsonl   one JSON event per line, appended by this server

`wait` blocks until the reader does something, prints the new events as JSON
lines, and exits. Standard library only. Listens on 127.0.0.1 only.
"""
import argparse, json, os, sys, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))


def lines(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [l for l in f.read().split("\n") if l.strip()]


def serve(state, port):
    os.makedirs(state, exist_ok=True)
    pages, events = os.path.join(state, "pages.jsonl"), os.path.join(state, "events.jsonl")

    class H(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def send(self, code, body, ctype="application/json"):
            body = body.encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", ctype + "; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            path, _, query = self.path.partition("?")
            if path == "/":
                with open(os.path.join(HERE, "index.html"), encoding="utf-8") as f:
                    return self.send(200, f.read(), "text/html")
            if path == "/pages":
                after = 0
                for kv in query.split("&"):
                    if kv.startswith("after=") and kv[6:].isdigit():
                        after = int(kv[6:])
                out = []
                for l in lines(pages)[after:]:
                    try:
                        out.append(json.loads(l))
                    except ValueError:
                        out.append({"title": "", "html": "<p>(unreadable page)</p>"})
                return self.send(200, json.dumps(out))
            self.send(404, "{}")

        def do_POST(self):
            if self.path != "/event":
                return self.send(404, "{}")
            n = int(self.headers.get("Content-Length") or 0)
            if n > 20000:
                return self.send(413, "{}")
            try:
                ev = json.loads(self.rfile.read(n))
                assert isinstance(ev, dict)
            except Exception:
                return self.send(400, "{}")
            ev["at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
            with open(events, "a", encoding="utf-8") as f:
                f.write(json.dumps(ev, ensure_ascii=False) + "\n")
            self.send(200, "{}")

    srv = ThreadingHTTPServer(("127.0.0.1", port), H)
    print("Live reader at http://127.0.0.1:%d/  (state: %s)" % (port, state), flush=True)
    srv.serve_forever()


def wait(state, timeout):
    events, mark = os.path.join(state, "events.jsonl"), os.path.join(state, "events.seen")
    seen = int(open(mark).read() or 0) if os.path.exists(mark) else 0
    end = time.time() + timeout
    while time.time() < end:
        ls = lines(events)
        if len(ls) > seen:
            print("\n".join(ls[seen:]))
            with open(mark, "w") as f:
                f.write(str(len(ls)))
            return 0
        time.sleep(0.5)
    print('{"type": "timeout"}')
    return 0


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("cmd", choices=["serve", "wait"])
    p.add_argument("state_dir")
    p.add_argument("--port", type=int, default=8787)
    p.add_argument("--timeout", type=int, default=600)
    a = p.parse_args()
    sys.exit(serve(a.state_dir, a.port) if a.cmd == "serve" else wait(a.state_dir, a.timeout))
