---
id: 02-thread
title: Anatomy of a thread
status: written
needs: []
canon: [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11]
briefs: [V2, V3, W1]
---

# Anatomy of a thread

Cut a long, thin right-angled triangle out of paper. Wrap it around a pencil,
starting with the short upright side. The sloping edge climbs the pencil in a
spiral.

That is a thread: a ramp wrapped around a cylinder. Everything a screw does
follows from the ramp. Turning the screw is pushing a load up a slope. A
gentle slope means many turns and little effort for a large force, which is
the whole trick: a hand on a spanner can stretch a steel bolt with tonnes of
tension because it is walking that load up a very long, very shallow ramp.

## Three measurements

Look at a bolt from the side and you see a row of peaks and valleys. Three
numbers describe them.

**Major diameter** is the width across the peaks. It is the size the screw is
named by. An M8 bolt measures a shade under 8 mm across its thread.

**Minor diameter**, also called root diameter, is the width across the bottoms
of the valleys. This is the solid core, the part that actually carries the
tension. It matters every time you drill a hole for a thread to bite into.

**Pitch** is the distance from one peak to the next, measured along the length
of the screw. It is also how far the screw travels in one full turn. An M8
bolt with its standard pitch of 1.25 mm moves 1.25 mm per turn. Eight turns:
one centimetre.

On metric and on the common inch threads, the two sides of each peak meet at
60°.

## Reading a name

Metric screws are named by diameter and length: **M6 × 30** is 6 mm across
the thread and 30 mm long. Length is measured from under the head, because
that is the part that goes into the work. Countersunk screws are the
exception: their heads go into the work too, so they are measured overall.

If nothing is said about pitch, the screw has the standard **coarse** pitch
for its size:

| Size | M3 | M4 | M5 | M6 | M8 | M10 | M12 |
|---|---|---|---|---|---|---|---|
| Coarse pitch (mm) | 0.5 | 0.7 | 0.8 | 1.0 | 1.25 | 1.5 | 1.75 |

A finer pitch is written in the middle: **M8 × 1.0 × 40**.

Inch threads count the other way round. Where metric gives the distance
between threads, inch gives the number of threads in one inch. **1/4-20** is a
quarter-inch screw with 20 threads per inch.

The two systems do not mix, and the dangerous cases are the near misses. An
M8 × 1.25 bolt and a 5/16-18 nut are close enough in size that they will start
together, turn a little, tighten up, and convince you that you are done. What
you have is two ruined threads holding by their fingernails. The test is
simple: a matching nut spins on freely by fingers for as many turns as you
like. If it tightens after two or three, stop.

## Why it stays put

A ramp can be so steep that things slide back down it, or shallow enough that
friction holds them where they are. A standard thread is deliberately on the
shallow side. Unroll one turn of an M8 thread and the slope is about 3°.
Steel sliding on steel does not start to slip until a slope of roughly 8° or
more. So a tightened bolt under a steady load cannot unwind by itself. The
thread is **self-locking**.

Steady is the important word. Part 07 is about what happens when the load
stops being steady.

## Which way

Nearly every thread is right-handed: turn clockwise, looking at the head, and
it goes in. Left-handed threads exist in the few places where the motion of
the machine would undo a right-handed one. The left pedal of a bicycle is the
one most people meet. If something will not undo, consider, before reaching
for a longer lever, that it may be asking to go the other way.

## Two families

Hold a bolt next to a wood screw and the difference is plain.

The **machine thread** on the bolt is fine and regular, and it is half of a
pair. It needs a matching thread to run in: a nut, or a hole that has had a
thread cut into it.

The **wood screw** has tall, sharp, widely spaced threads and a point. It
brings no partner. It makes its own, pressing a thread into the wood as it
goes. Chipboard screws and sheet-metal screws belong to the same family.

Which family you are holding decides almost everything about the hole you
drill, and that is where parts 04 and 05 go their separate ways.

## Try it

1. Make the paper ramp. Then make a second with a steeper slope and compare
   the spirals: that is fine pitch against coarse.
2. Find any bolt. Lay a ruler along the thread and count the peaks in 10 mm.
   Ten peaks: pitch 1.0 mm, probably M6. Eight: 1.25, probably M8. Measure
   across the thread to confirm.
3. Mark the head with a pen, turn a nut exactly one turn, and see how far it
   moved.

## Checks

- "A screw is labelled M5 × 20. What are the 5 and the 20? What is its pitch,
  and how do you know?" (diameter, length under head; 0.8 mm, coarse by
  default)
- "Why can a nut that goes on three turns still be the wrong nut?" (near-match
  threads start, then bind)
- "Why doesn't a tight bolt unscrew itself under a steady pull?" (shallow ramp,
  friction angle larger than lead angle)

## Notes for the agent

- Brief V2 belongs at "Three measurements". If the reader has a bolt in hand,
  use the bolt first and the diagram second.
- If the reader's hardware is inch (North America, old British machinery),
  lead with inch naming and treat metric as the comparison.
- Brief W1 (thread explorer) is worth building only for *Course* readers who
  ask "what if the pitch were…".
- Do not explain thread tolerances or classes of fit here. If asked, give one
  sentence and move on.
