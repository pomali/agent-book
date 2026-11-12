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

## Adapting an existing text

For a public-domain or openly licensed work. `books/ajax/` shows the result.

1. **Check the rights and write them down.** Translation, edition and
   illustrations each have their own status. Record it in `SOURCE.md`.
2. **Convert mechanically.** Use a script, not retyping and not an agent's
   memory of the text. Keep line breaks in verse. Diff a sample against the
   source.
3. **Divide for sittings**, at the work's own joints. Say that the divisions
   and titles are yours.
4. **Number the passages** so they can be cited.
5. **Correct only evident slips** and list every one.
6. **Write the Companion for each part.** One line to say before it. Three to
   six things to watch for, each pointing at a passage. Two questions. The
   choices a director or teacher would face. This is where your work is.
7. **Write canon from the outside in**: what the first audience knew; what
   happens; the conditions the work was made for; what came after; and the
   open questions, stated fairly, with an instruction not to settle them.
8. **Add a glossary** if the language is old. Tell the agent to gloss in
   passing.
9. **Decide the bridge.** How may the agent help a modern reader without
   replacing the text: paraphrase alongside, glosses only, performance? Make
   it a reading mode and say which passages must always be given in the
   original words.
10. **Mark what needs care** and write the rule.

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
