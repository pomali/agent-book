# Ideas and open questions

A working list. Rough order: nearer and cheaper first.

**Adopted so far** (now in `format.md`): the live reader, canon tests, seeds
graduating through `candidates/`, the reader's own edition, tone files per
language, per-book provenance, and brief kinds for maps, character sheets,
3D objects and style (CSS, shaders). The rest is open.

## Reading experiences

- **Real-time reading.** *The Unploughed Strip* runs St George's Day to St
  George's Day. An agent could deliver each chapter in its own month, with a
  two-minute "today in Lieskovany" on ordinary days. A book you live beside
  for a year.
- **Start from the reader's own problem.** *Hold Fast* is best entered with a
  photo of a stripped screw or a wobbling shelf. Generalise: every educational
  book declares the kinds of real-world problem it can be entered from.
- **Interview the book.** Talk to a character (bounded by canon and by what
  that character knows on that date), or to "the author" about why a rule of
  thumb is what it is.
- **Other points of view.** Same chapter from the ox-boy, the priest, the
  thing in the pool. All seeds; canon keeps them honest.
- **Dual-layer reading.** Fiction with a switchable "what is historically
  true here" layer; non-fiction with a switchable "where this came from"
  layer.
- **Shared reading.** Two readers, two agents, one book: agents exchange
  spoiler-safe notes ("she is past chapter 4 and thinks the priest is right")
  so the humans can talk about it.
- **Child and adult together.** One performance, two levels: the agent reads
  to the child and slips the adult a margin note.

## Things the agent makes

- **The reader's own copy.** At the end, the agent compiles what this reader
  actually read: text, their questions, the images made for them. It becomes a
  one-off edition as HTML, EPUB or print-ready PDF.
- **Persistent objects.** A village map that fills in as chapters are read. A
  fastener "cheat card" that grows with each part and ends up on the workshop
  wall.
- **Small tools, not just pages.** Torque estimator, pilot-hole chart, a
  tally-stick keeper. The book ships the spec and the test cases; the agent
  builds it for the reader's device.
- **Audio first.** A book performed in the workshop or the kitchen: voice
  only, hands busy. The briefs need an "eyes-free" variant.
- **Physical output.** STL for a thread-pitch gauge; a printable tally stick;
  a seed-packet insert.

- **A shelf of classics.** Any public-domain text can be given a Companion
  layer. *Ajax* took one script and one sitting to convert; the work is in
  the companions and the open questions. A converter from Standard Ebooks or
  Project Gutenberg to scene files, plus an agent drafting companions for an
  editor to correct, would scale it.
- **Annotation layers by different hands.** One fixed text, several
  Companions: a director's, a classicist's, a soldier's, a schoolteacher's.
  The reader picks who sits beside them.

## Format

- **Canon tests.** A `tests/` file of question → expected answer pairs. Any
  agent can self-check before performing; authors get regression tests for
  their world.
- **Reference renders.** Store one approved output per brief as a target for
  style and quality, without making it mandatory.
- **Skills / MCP packaging.** Ship each book also as an agent skill or a tiny
  MCP server (`get_part`, `search_canon`, `save_progress`) for agents that
  prefer tools to files.
- **Links between books.** The plough in 1300 has no screws, but it has
  wedges, pegs and a forge-welded share. A fastening part could open onto a
  scene; a scene could open onto a lesson. A shared `links` vocabulary would
  make a shelf more than a list.
- **Translation as performance.** Canon carries a glossary of terms that must
  be translated consistently, or left alone (*lán*, *šoltýs*).
- **Reader-level knobs.** A manifest could expose a few explicit dials (depth,
  pace, how much invention is allowed) that the reader sets once.

## Feedback loop

- **The book learns.** With consent, agents report anonymised aggregates:
  where readers stop, which canon items get questioned, which seeds get grown
  most. The author sees where the book is weak.
- **Seeds graduate.** A seed grown well for one reader is offered upstream;
  the author edits and promotes it to `written`.
- **Errata that reach readers.** An agent comparing `progress.md`'s commit
  with HEAD can say: "The torque table you read in March was corrected."

## Open questions

- **Authorship.** If half the words a reader met were improvised, what did the
  author write? Is provenance labelling enough?
- **Sameness.** Shared reading relies on a shared text. How much variation can
  a book take before two readers have not read the same book?
- **Trust and safety.** A book is instructions to an agent, which makes it a
  possible injection vector. START.md draws a line; is a signed manifest or an
  allow-list of capabilities needed?
- **Quality floor.** A weak agent gives a weak performance and the author
  takes the blame. Should a book state a minimum capability?
- **Money and licence.** How does an author get paid for a git repo? Licence
  for canon vs. text vs. reader-generated artifacts? Who owns the reader's own
  edition?
- **Evaluation.** How do we know an agent-book beat a paper one? Recall after
  a week, a repair actually completed, a reader who came back for chapter 7.
- **Longevity.** Will a book written for today's agents perform in ten years?
  Plain text and small canon are the bet.
