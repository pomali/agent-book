# Live reader

A page the reader reads in their browser while the agent writes ahead of
them. It is meant to feel like reading a book: one column, top to bottom, at
the reader's pace. Beside the text the agent can hang **sidenotes** that the
reader opens or passes by: a gloss, a picture, an animation, a small tool, a
reference. What the reader does (how far they are, what they open, what they
select, what they type) goes back to the agent, so the notes on the next page
can be about what this reader is curious about.

This is not a choose-your-own-adventure. The main text goes one way.

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
4. On `ask`, `more`, `say`: answer in a **sidenote** on the next page, and
   let the main text carry on undisturbed. A reader who keeps opening notes
   of one kind (history, pictures, how things work) should find more of that
   kind; a reader who opens none should get fewer.
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
| `notes` | Optional list of sidenotes: `{ "after": 2, "label": "What is a tally?", "html": "…" }`. `after` is the paragraph it hangs beside. Shown closed, as its label; in the margin on a wide screen. The `html` may hold text, an inline SVG picture or animation, a `data:` image. |
| `choices` | Optional list of labels shown as buttons under the page. For a check question in an educational book. Not for forking a story. |
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
| `note` | a sidenote is opened | `page`, `text` (its label) |
| `choice` | a choice button is tapped | `page`, `text` |
| `ask` / `more` / `mark` | the reader selects text and taps one | `page`, `text` |
| `say` | the reader types in the box at the bottom | `text` |

## What a book says about it

A book's `STUDIO.md` may carry a brief for live reading (kind `L`): how long
a page is, what sidenotes are worth hanging, how theme and shader follow the
story. Without one, use the book's voice and keep the page plain.

## Sidenotes

- Label them so the reader can decide without opening: "The tithe", "Map:
  where they are", "Why 60°?".
- Two or three to a page at most. A page with none is fine.
- A note never holds anything the main text needs. Skipping all of them
  loses nothing of the book.
- Anything too large for a note (a full page, a 3D object, audio) is made as
  a file in `artifacts/` and the note says where it is.

## Limits


- Written text is still the author's. Cut it into pages at paragraph breaks;
  do not rewrite it to fit.
- Text keeps a readable contrast against any theme or shader you set. If in
  doubt, leave the shader off.
- Where a browser cannot reach the reader's machine (a phone, a hosted chat),
  use whatever your environment offers for live pages, or fall back to chat.
  The loop is the same.
