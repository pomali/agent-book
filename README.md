# agent-book

An experiment: what is a book when the reader arrives with an agent?

A book here is not a finished block of prose. It is **source material plus
performance instructions**: canon the agent must not contradict, text the
author wrote, seeds the agent may grow, and briefs for visuals, audio and web
pages the agent can produce for one particular reader.

## Read a book

Tell your agent:

> Read `START.md` in https://github.com/pomali/agent-book and take me through a book.

That is the whole interface.

## The shelf

| Book | Kind | What it is |
|---|---|---|
| [Hold Fast](books/hold-fast/BOOK.md) | Educational | Screws and fastenings: why joints hold, how to pick and tighten the right fastener. |
| [The Unploughed Strip](books/the-unploughed-strip/BOOK.md) | Fantasy | One farming family, one year (1300–1301), a valley in the Kingdom of Hungary, and a debt to things that are not people. |

## Make a book

Start at [docs/](docs/README.md): the concept, the format, an authoring guide,
and a list of open ideas.

## Layout

```
START.md       entry point for a reading agent
AGENTS.md      routing for any agent that lands in the repo
catalog.json   machine-readable shelf
books/<id>/    one directory per book
docs/          how the format works and how to write for it
reader/        local, git-ignored: one reader's profile, progress, artifacts
```
