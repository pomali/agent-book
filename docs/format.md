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
provenance: strict       # strict | light | off
tests: tests.md          # optional
tone: tone/              # optional, one file per language
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
### V2: Thread anatomy
- when: part 02, or whenever pitch/diameter is confused
- make: cross-section of an external thread with labelled dimensions
- must show: major diameter, minor diameter, pitch, 60° flank angle
- must not: imply the thread is a set of separate rings
- canon: T1–T4
- done when: a reader can point to pitch and major diameter unprompted
```

Brief ids start with a letter for the kind of thing made. Use what the book
needs; these are the kinds in use:

| Letter | Kind | Examples |
|---|---|---|
| V | Visual | diagram, plate, portrait |
| M | Map | a place that fills in as the reader goes |
| C | Character sheet | who someone is, as far as the reader knows |
| O | Object | a 3D model to turn, or a file to print |
| A | Audio | narration, soundscape |
| S | Style | CSS theme, typography, a shader behind the page |
| W | Web | a page or small tool |
| L | Live | how the book behaves in the live reader |

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

How much the agent must say about what is the author's and what is its own
is the book's choice, set by `provenance` in `BOOK.md`:

- `strict`: always clear, in speech and in generated files. For books a
  reader may act on, and for texts by a named author that must not be
  confused with the agent's paraphrase.
- `light`: when it matters, or when asked.
- `off`: never volunteered. For fiction, where it breaks the spell. The agent
  still answers truthfully if the reader asks.

The three labels, where used: **author-text** (delivered as written),
**canon-derived** (the agent's words, traceable to canon), **improvised**
(the agent's invention, consistent with canon).

## Canon tests (`tests.md`)

Question and expected-answer pairs that can be answered from canon alone. An
agent runs through them silently before performing; an author runs them
after every canon change. Include questions whose right answer is a refusal:
a secret not yet revealed, a number the book does not have, an open question
that must not be settled.

```
- Q: What is the coarse pitch of M8?
  A: 1.25 mm. (T5)
```

## Tone files (`tone/<language>.md`)

Agents translate at reading time. A tone file makes the translation the
author's: for one language it fixes the register, the names and terms that
must always be rendered the same way, what stays untranslated, and a short
sample of the book in that language to tune the ear. The book's main voice
file remains the reference for everything not language-specific.

## Seeds graduating (`candidates/`)

A seed grown well for one reader can become part of the book.

1. The reader's agent, with the reader's consent, submits the grown text as
   `books/<id>/candidates/<seed-id>-<short-name>.md`, with the seed's front
   matter and `status: candidate`. Nothing personal in it.
2. Several candidates for one seed may sit side by side.
3. The author picks, edits freely, moves the result to the main line as
   `NN-slug.md` with `status: written`, deletes the seed from `OUTLINE.md`,
   and adds any new facts to canon and a question to `tests.md`.

Reading agents ignore `candidates/`.

## The reader's own edition

Every book should define, as a brief in `STUDIO.md`, what the reader can take
away at the end: one file holding the book as this reader met it.

## Versioning

`format:` in `BOOK.md` and `catalog.json` names the format version. Books are
versioned by git. A reader's `progress.md` should record the commit it was
read at, so an agent can tell the reader when the book has changed.
