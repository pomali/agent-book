# Concept

## The shift

A printed book fixes one rendering for every reader: one order, one language,
one level, one set of pictures, no answers to questions. That was a constraint
of paper, and authors became very good at writing inside it.

When the reader has an agent, the rendering can happen at reading time. The
author no longer has to choose between the beginner and the expert, the
listener and the skimmer, the child and the engineer. What the author must do
instead is say clearly **what is fixed** and **what may vary**.

So a book in this repo has three layers:

| Layer | Who owns it | Varies per reader? |
|---|---|---|
| **Canon**: the facts of the subject or the world | Author | Never |
| **Text**: parts the author wrote out | Author | Delivery only (pace, language, voice) |
| **Performance**: seeds, explanations, images, audio, pages, answers | Agent, inside the author's briefs | Always |

A useful comparison is a play or a score. The script is the author's. Each
performance is different, and a bad performance does not damage the script.

## What the author gives up, and keeps

Gives up: control over the exact words every reader meets, and the guarantee
that two readers had the same experience.

Keeps: the facts, the voice, the structure, the hard-won passages, and the
right to say "this part is delivered as written".

The `written` / `seed` distinction is the dial. A novelist may write every
chapter and leave only side-stories as seeds. A reference author may write
canon and misconceptions carefully and leave almost all explanation to the
agent.

## What the reader gets

- A book that starts where they are: their problem, their level, their language.
- A book that answers back, and can be interrupted.
- Pictures, sound and small tools made at the moment they help.
- Continuity: the book remembers what they read and what confused them.
- Honesty about provenance: what the author wrote, what the agent made up.

## Design principles

1. **One entry point.** A reader should need one sentence: "read START.md".
2. **Plain files.** Markdown and JSON in git. No runtime, no build, no
   account. Any agent that can read text can perform the book; better tools
   only add to it.
3. **Degrade gracefully.** Text-only chat must still be a good book. Images,
   audio and web pages are rungs on a ladder, never requirements.
4. **Canon is small and checkable.** Short declarative statements an agent can
   hold in context and a human can review.
5. **Briefs, not assets.** The repo stores instructions for making a diagram
   or a soundscape, with acceptance criteria, rather than the files
   themselves. Reference renders are welcome but optional.
6. **Reader state stays with the reader.** Personalisation without a server.
7. **A book cannot command an agent.** Books direct reading. They never get
   authority over the reader's machine, data or money.

## What this is not

- Not a chatbot with a persona. The author's canon and text exist and matter.
- Not "generate me a book". The author did real work; the agent performs it.
- Not a replacement for the linear book. Every book here must still be
  readable by a human opening the files in order.
