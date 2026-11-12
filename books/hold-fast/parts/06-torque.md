---
id: 06-torque
title: How tight is tight
status: written
needs: [01-clamp, 05-metal]
canon: [C2, M1, M4, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9]
briefs: [V4, W2, A2]
---

# How tight is tight

Part 01 said the bolt is a spring and what we want from it is stretch. Here is
the awkward fact this part is about: **you cannot feel the stretch.** What you
feel in your hand, and what a torque wrench measures, is how hard the nut is
to turn. Those are related, but loosely, and most of what goes wrong with
tightening lives in the gap between them.

## Torque

Torque is turning effort: force times the length of the lever. Push with 100
newtons, about the weight of a 10 kg bag, on the end of a spanner 0.2 m long
and you apply 20 newton-metres, written 20 N·m. Twice the spanner, twice the
torque for the same push.

## Where the effort goes

When you pull on that spanner, you might imagine all your effort going into
stretching the bolt. Very little does.

- About **half** is spent dragging the underside of the nut or bolt head
  around on the surface it sits on.
- About **four tenths** is spent on friction between the threads.
- About **one tenth** is left to stretch the bolt.

So roughly nine tenths of your work makes heat and one tenth makes preload.
Now consider what a small change in friction does. If the surfaces are a
little slicker, a drop of oil, a different plating, the friction share falls,
and the stretch share does not rise a little: it can double. Same wrench, same
click, a very different bolt.

This is why two rules that sound fussy are not:

1. **A torque value is only valid for the thread condition it was written
   for.** "Dry" and "lubricated" figures are different numbers. Oil the
   threads and then use a dry figure, and you can take a bolt well past where
   it should be.
2. **Even done perfectly, torque gives preload with a scatter of about a
   quarter either way.** A torque wrench does not measure tightness. It makes
   your guess repeatable.

## A number you can work out

The usual short formula is

**T ≈ K × F × d**

T is the torque, F the preload you want, d the bolt's nominal diameter, and K
a "nut factor" that sweeps all the friction into one number. For ordinary
steel bolts, plain or zinc-plated, as they come from the box, K is about
0.2. Lubricated, about 0.15 or less.

How much preload should you want? A common target is about three quarters of
the bolt's **proof load**, the highest tension it can take and still spring
back fully. For the everyday class 8.8 bolt, proof stress is 580 MPa.

Work an M8 through:

- Stress area of an M8 coarse thread: 36.6 mm².
- Proof load: 580 × 36.6 ≈ 21 200 N.
- Target preload, three quarters of that: about 15 900 N. That is the weight
  of a small car, hanging on a bolt as thick as a pencil.
- Torque: 0.2 × 15 900 N × 0.008 m ≈ **25 N·m**.

The same sum for neighbouring sizes, class 8.8, dry:

| Bolt | M6 | M8 | M10 | M12 |
|---|---|---|---|---|
| Torque (N·m), about | 10 | 25 | 50 | 88 |

Two things to take from the table. First, torque climbs steeply with size, far
faster than the diameter does; "a bit more for a bigger bolt" underestimates
it badly. Second, 10 N·m on an M6 is not much: a firm pull on a short spanner.
Small bolts are over-tightened by strong hands every day.

These figures show the reasoning. **When the maker of a machine gives a
torque, use theirs.** They know things the formula does not: a soft aluminium
thread, a gasket, a part that must not be crushed. Often their number is much
lower than the bolt could take, because the bolt is not the weakest thing in
the joint.

## Without a torque wrench

Most screws in the world are tightened by hand and most of them are fine. A
few habits get you most of the way.

- **Feel for the change.** The nut runs down freely, meets the surface, and
  the resistance rises firmly. That firm rise is the bolt stretching. If the
  resistance then stops rising, if it goes soft or smooth while you are still
  turning, stop at once. Something is yielding: the bolt, the thread, or the
  part.
- **Match the lever to the bolt.** Spanners and hex keys are made longer for
  bigger sizes on purpose. Use the tool at its own length, with one hand, and
  do not add a pipe.
- **More than one bolt: go round in stages.** Bring all of them to snug, then
  to about half, then to full, crossing from side to side as you would
  tighten a wheel. One bolt taken to full while its neighbours are loose
  tilts the part and its load is released when the others come up.

## When it matters, measure something better

Where preload truly matters, engineers stop trusting torque alone. They
tighten to a low torque and then turn through a set angle, which is really
measuring stretch through the pitch of the thread. Or they measure the bolt's
change in length directly. You do not need these at the workbench. It is
enough to know that they exist because torque, the thing we can easily
measure, is one step removed from the thing we want.

## Looking after the wrench

A click-type torque wrench is a spring instrument. Wind it back to its lowest
setting after use so the spring is not left compressed. Use it to tighten, not
to break loose stuck fasteners. Pull smoothly and stop at the click; a second
click "to be sure" adds torque.

## Try it

1. With a kitchen or luggage scale hooked on the end of a spanner, pull to a
   chosen force and work out the torque from the lever length. Compare with
   what your hand calls "tight".
2. Take two identical bolts and nuts, one dry and one with a drop of oil.
   Tighten both to the same modest torque, marking the nut first. Count how
   much further the oiled one turned.

## Checks

- "You oil a bolt and tighten it to the dry figure. Is the bolt tighter,
  looser, or the same as intended, and why?" (tighter, possibly far too
  tight: less friction, more of the torque becomes stretch)
- "A wrench clicks at 25 N·m. What do you actually know about the bolt?"
  (the turning effort; preload only to within about a quarter)
- "The manual says 6 N·m for an M6 into an aluminium casing; the table says
  10. Which, and why might they differ?" (the manual; the thread in the
  casing is the weak part)

## Notes for the agent

- Safety line from BOOK.md applies here more than anywhere: wheels, brakes,
  steering, lifting gear, anything overhead. Give the principle, then send the
  reader to the manufacturer's figure.
- If the reader has no part 05 behind them (*Fix my thing*), give M1 and M4 in
  two sentences before the worked example, or skip the example and use the
  table.
- Misconceptions X2, X3, X4 all surface here.
- W2 (torque and preload explorer) fits after the worked example for readers
  who like to move a slider. A2 is the eyes-free version of "Without a torque
  wrench" for someone whose hands are on the spanner.
