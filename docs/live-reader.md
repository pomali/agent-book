# Live reader

A page the reader reads in their browser while the agent writes ahead of
them. What the reader does on the page (how far they are, what they select,
which choice they tap, what they type) goes back to the agent, and the next
page can answer it.

It lives in `live/`: one HTML file and one small Python server, standard
library only, listening on the reader's own machine and nowhere else. It is a
tool of this repository, not part of any book. Start it only when the reader
wants it.

## Run it

```bash
python3 live/serve.py serve reader/<book-id>/live
```

The reader opens `http://127.0.0.1:8787/`. The agent then loops:

```bash
python3 live/serve.py wait reader/<book-id>/live
```

`wait` blocks until the reader does something, prints the new events, and
exits. Read them, append one or more pages to `pages.jsonl`, wait again.

## The loop

1. Write the first page (and the second: stay one page ahead).
2. `wait`.
3. On `reached` for the newest page, or `waiting`: write the next page.
4. On `ask`, `more`, `choice`, `say`: let the next page answer it, in the
   book's own manner. A question may get a short aside and then the story
   goes on; a choice changes what happens; "more of this" slows down and
   stays with the thing selected.
5. On `mark`: note it in `progress.md`. Marked passages belong in the
   reader's own edition.
6. Finish with a page that has `"end": true`.

Keep pages short: a screen or two. Short pages are what make the book
responsive; a whole chapter in one page cannot react to anything.

## Pages

One JSON object per line in `pages.jsonl`:

| Field | Meaning |
|---|---|
| `id` | Your name for the page; comes back in events. |
| `title` | Optional heading. |
| `html` | The page body. Text, inline SVG, `data:` images. Scripts, event handlers and remote loads are stripped. |
| `choices` | Optional list of labels shown as buttons under the page. |
| `theme` | Optional: `bg`, `ink`, `accent`, `muted`, `font`, `measure` (CSS values). Applied when the reader arrives at the page, with a slow fade, and kept until changed. |
| `shader` | Optional GLSL fragment shader body drawn behind the text; uniforms `u_time` (seconds) and `u_res` (pixels). `null` turns it off. Skipped for readers who ask for reduced motion. |
| `end` | `true` on the last page. |

## Events

One JSON object per line in `events.jsonl`, each with `type` and `at`:

| Type | Sent when | Carries |
|---|---|---|
| `open` | the page is opened | |
| `reached` | a page scrolls into view | `page`, `index`, `of` |
| `waiting` | the reader is near the end and no page follows | `after` |
| `choice` | a choice button is tapped | `page`, `text` |
| `ask` / `more` / `mark` | the reader selects text and taps one | `page`, `text` |
| `say` | the reader types in the box at the bottom | `text` |

## What a book says about it

A book's `STUDIO.md` may carry a brief for live reading (kind `L`): how long
a page is, what choices are worth offering, how theme and shader follow the
story. Without one, use the book's voice and keep the page plain.

## Limits

- Written text is still the author's. Cut it into pages at paragraph breaks;
  do not rewrite it to fit.
- Text keeps a readable contrast against any theme or shader you set. If in
  doubt, leave the shader off.
- Where a browser cannot reach the reader's machine (a phone, a hosted chat),
  use whatever your environment offers for live pages, or fall back to chat.
  The loop is the same.
