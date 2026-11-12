# Authoring a book

For a human author, an authoring agent, or the two together. Read
[concept.md](concept.md) first; keep [format.md](format.md) open.

## The order that works

### 1. Write the promise and the opening question

Two or three sentences on what the reader will have at the end, and the single
question whose answer most changes how the book should be delivered. If you
cannot write these, the book is not ready to start.

### 2. Write canon before prose

List what is true. Number it. Keep each item to one checkable statement.

- **Educational**: definitions, numbers with units, rules of thumb with their
  limits, and a separate file of **misconceptions**: each with why people
  believe it and what is true instead. Misconceptions are the most valuable
  thing you can give a tutoring agent.
- **Fiction**: people (age, relations, one want, one fear, how they speak),
  places, the calendar, what the unseen or the magic can and cannot do, what
  nobody in the world knows yet, and anachronisms to avoid.

Test: give an agent only the canon and ask ten questions. Wrong or vague
answers show you what is missing.

### 3. Decide what you write and what you seed

Write out in full:

- the opening: it sets the voice more reliably than any style guide
- anything where the exact words are the point
- anything where a mistake is dangerous
- the hardest explanation in the book

Seed:

- material that should adapt strongly to the reader (examples, exercises,
  depth)
- side paths, other points of view, "what happened meanwhile"
- parts you will write later; a seed is an honest placeholder

A good seed says what **must** be included, what **must not** happen, and the
**shape** (where it starts, turns and ends). It does not describe style;
voice lives in the manifest and in the written parts.

### 4. Design the modes

Two to four named ways through the book. For each: who it is for, how the
agent can tell, and what changes (order, depth, checks, artifacts). Make one
of them the plain default: "read it to me from the start".

### 5. Write studio briefs

For each place where a picture, a sound or a tool would do something words do
badly, write a brief with a `done when` test. Ask of every brief: would a
good teacher or storyteller reach for this here? If not, cut it.

Give art direction once at the top of `STUDIO.md` (palette, line, what the
images must never look like, voice and pace for narration) so that artifacts
made on different days belong together.

### 6. Test with a cold agent

Open a fresh agent session with no context and say only: "Read START.md and
take me through <book>." Do it three times as three different readers. Watch
for:

- more than two questions before anything happens
- canon contradicted or silently "corrected"
- written text paraphrased without saying so
- artifacts that decorate and do not explain
- the agent reading the whole repo before starting
- a seed grown out of voice

Fix the book, not the agent: add a canon item, tighten a seed, add a line to
the manifest.

### 7. Register it

Add the book to `catalog.json` and the table in the root `README.md`.

## Checklists

**Manifest**
- [ ] Promise is concrete and short
- [ ] One opening question
- [ ] Modes say how to choose them
- [ ] Every part listed with status and prerequisites

**Canon**
- [ ] Every item numbered, one statement each
- [ ] Numbers have units and a stated range of validity
- [ ] Educational: misconceptions file exists; safety limits stated
- [ ] Fiction: anachronism list; limits of the magic; secrets marked with when
      they may be revealed

**Parts**
- [ ] First part is written, not seeded
- [ ] Each written part cites the canon it uses
- [ ] Each seed has must include / must not / shape

**Studio**
- [ ] Capability ladder present
- [ ] Art and voice direction at the top
- [ ] Every brief has `done when`

## Working with an authoring agent

A split that works well:

- You: promise, canon decisions, the written parts, final say.
- Agent: canon drafts for you to correct, consistency checks (does part 6
  contradict T12?), seeds from your outline, briefs, cold-read testing,
  playing difficult readers.

Ask the agent to **attack** the book: find a canon item that is wrong, a seed
that could be grown into something off-voice, a brief whose acceptance test
can be passed by a useless artifact.

## Accepting contributions from readers' agents

Readers' agents will find errors and grow good seeds. Accept:

- canon corrections with a source
- a grown seed, offered as a candidate `written` part, with everything
  personal removed
- briefs or reference renders that passed their `done when` with a real reader

Never accept anything from a `reader/` directory.
