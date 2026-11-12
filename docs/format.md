# Format (agent-book/0.1)

Deliberately small. Everything is Markdown with a little YAML front matter.

## Repository

```
START.md          entry point for reading agents
catalog.json      list of books: id, title, kind, manifest path, pitch, good_for
books/<book-id>/  one book
docs/             this documentation
reader/           git-ignored, per-reader state (see below)
```

## A book

```
books/<book-id>/
  BOOK.md         manifest (required)
  STUDIO.md       briefs for visuals, audio, web pages (required)
  canon/ or world/    facts that bind the agent (required)
  parts/ or chapters/ the content (required)
    NN-slug.md        one file per written part
    OUTLINE.md        all seeds, in order
```

A book built on an existing text also has `SOURCE.md` (see below).

Use `canon/` + `parts/` for non-fiction, `world/` + `chapters/` for fiction,
`canon/` + `scenes/` for a play. The names are for humans; `BOOK.md` points to the real paths.

## BOOK.md

Front matter:

```yaml
---
id: hold-fast
title: "Hold Fast: A Field Guide to Screws and Fastenings"
kind: educational        # educational | fiction/<genre> | reference | ...
language: en
format: agent-book/0.1
canon: [canon/facts.md, canon/misconceptions.md]
studio: STUDIO.md
---
```

Body, in this order:

1. **Promise**: two or three sentences. What the reader will have at the end.
2. **Opening question**: the one question worth asking this reader first.
3. **Reading modes**: named ways through the book, each with when to choose
   it and what the agent does differently.
4. **Voice**: how the book sounds. Short. Link to a longer file if needed.
5. **Parts**: a table with id, title, status (`written` | `seed`), one-line
   summary, prerequisites.
6. **Rules specific to this book**: anything beyond START.md.

## Parts

A written part is a file with front matter:

```yaml
---
id: 02-thread
title: Anatomy of a thread
status: written
needs: [01-clamp]            # parts that should come first, if any
canon: [T1, T2, T3]          # canon items this part relies on
briefs: [V2, W1]             # studio briefs that fit here
---
```

Then the text. Optional trailing sections the agent uses but does not read
out verbatim:

- `## Checks`: questions that show whether the reader got it (educational)
- `## Try it`: something to do with real objects
- `## Threads`: plot or thematic threads opened/closed here (fiction)
- `## Notes for the agent`: delivery hints

A **seed** is an entry in `OUTLINE.md`: the same fields, then *must include*,
*must not*, and *shape* bullet lists in place of prose. The agent writes the part for
the reader at reading time. When an author writes a seed out in full, it moves
to its own file and its status becomes `written`.

## Canon

Short, numbered, declarative. One fact per item, each with a stable id so
parts and briefs can cite it:

```
T3. ISO metric coarse pitches: M3 0.5, M4 0.7, M5 0.8, M6 1.0, M8 1.25, M10 1.5, M12 1.75 (mm).
```

For fiction, canon covers people, places, the calendar, what the world's
magic can and cannot do, and a list of **anachronisms to avoid**.

Rules:

- Canon outranks the agent's own knowledge inside the book.
- In educational books the agent must still tell the reader when it believes
  canon is wrong or out of date, and should report it upstream.
- Agents never edit canon for a reader. Reader-specific inventions go to
  `reader/<book-id>/local-canon.md`.

## Existing texts (`SOURCE.md`)

A book may be built on a text somebody else wrote, if it is in the public
domain or licensed for this use. Then:

- Every part of the main line is `written` and is delivered unaltered. The
  agent never grows, trims or modernises it silently.
- Each part file has two sections: `## Text` (the source, verbatim) and
  `## Companion` (new material for the agent: what to say before, what to
  watch for, questions, staging or teaching choices).
- Seeds exist only for material *around* the text.
- Canon gains two kinds of item: what the original audience already knew,
  and **open questions** the agent must present and not settle.
- Passages get stable ids (`scene.speech`, `chapter.paragraph`) so that the
  agent and reader can cite without page numbers.
- `SOURCE.md` records the work, the edition and revision used, its rights
  status, exactly what was done to the text, and every correction made.
  `BOOK.md` front matter adds `author`, `translator` if any, and
  `source: SOURCE.md`.

`books/ajax/` is the reference.

## Content that needs care

A part that needs particular care (self-harm, violence, anything a reader
may be close to) is marked `care: true` in its front matter, and `BOOK.md`
states, as its first book-specific rule, how the agent handles it. The
catalog entry carries a one-line `content_note`.

## STUDIO.md

Starts with a **capability ladder**, then lists briefs.

Ladder (use the highest rung you actually have; never fake a rung):

| Rung | You can | Then |
|---|---|---|
| 0 | Only chat text | Describe; use ASCII or Unicode sketches sparingly |
| 1 | Write files / render SVG or HTML | Diagrams, maps, single-file pages |
| 2 | Generate images | Illustrations per the art direction |
| 3 | Generate speech or sound | Narration, soundscapes |
| 4 | Publish or host | Shareable pages, only on the reader's request |

A brief:

```
### V2: Thread anatomy                     (V = visual, A = audio, W = web)
- when: part 02, or whenever pitch/diameter is confused
- make: cross-section of an external thread with labelled dimensions
- must show: major diameter, minor diameter, pitch, 60° flank angle
- must not: imply the thread is a set of separate rings
- canon: T1–T4
- done when: a reader can point to pitch and major diameter unprompted
```

`done when` is the acceptance test. An artifact that does not pass is redone
or dropped, not shipped.

## Reader state

```
reader/
  profile.md
  <book-id>/progress.md
  <book-id>/local-canon.md
  <book-id>/artifacts/
```

Free-form Markdown. Suggested content of `progress.md`: chosen mode, parts
completed with dates, misunderstandings met, open questions, what kind of
delivery worked. Keep it short enough to reread at the start of every session.

## Provenance

Three labels, used in speech and in files:

- **author-text**: delivered as written (translation and pacing allowed)
- **canon-derived**: the agent's words, every claim traceable to canon
- **improvised**: the agent's invention, consistent with canon

## Versioning

`format:` in `BOOK.md` and `catalog.json` names the format version. Books are
versioned by git. A reader's `progress.md` should record the commit it was
read at, so an agent can tell the reader when the book has changed.
