# Studio: Hold Fast

Briefs for things you may make for the reader. Make one when it will explain
something better than your next paragraph would. Save to
`reader/hold-fast/artifacts/` with a provenance note (see `START.md`).

## Capability ladder

| Rung | You can | Do |
|---|---|---|
| 0 | Chat text only | Describe precisely; a small ASCII profile of a thread is fine. Lean on *Try it* with real objects. |
| 1 | Write or render SVG/HTML | All V and W briefs as vector diagrams and single-file pages. This book is best at this rung. |
| 2 | Generate images | Only for V1 and chapter openers. Generated images get dimensions and proportions wrong; never use them for anything the reader will measure from. |
| 3 | Generate speech | A briefs. |
| 4 | Publish | Only if the reader asks to share a page. |

## Direction

**Look.** Technical drawing, not cartoon. White or very dark background
following the reader's theme. One ink colour for objects, one accent colour
(a warm orange) for the single thing the diagram is about, grey for
dimensions. Label on the drawing, not in a legend. Every dimension has a unit.
Section views are hatched. No shadows, no gradients, no decoration.

**Scale.** Proportions must follow canon. An M8 × 1.25 thread drawn to scale
has a 60° profile and pitch 1.25/8 of the diameter. If you exaggerate for
clarity, write "not to scale" on the drawing.

**Voice (audio).** Calm, unhurried, a person standing next to you. Short
sentences. Numbers spoken once, then repeated. Never a sentence that needs to
be seen to be understood.

**Pages.** One self-contained HTML file, no network requests, works on a phone
held in one hand in a workshop. Large controls. Shows its assumptions and the
canon items its numbers come from. Every page carries the safety line where
its numbers could be misused.

## Visual briefs

### V1: Two books and a hand
- when: part 01, if the reader cannot do the experiment
- make: side view of two stacked blocks, a downward force, a sideways push,
  and the friction force opposing it at the interface
- must show: clamp load, push, friction, each as an arrow with a label
- must not: show any pin or bolt through the blocks
- canon: C1, C3, C4
- done when: the reader can say which arrow stops the sliding

### V2: Thread anatomy
- when: part 02 "Three measurements"; whenever pitch and diameter are confused
- make: half-section of an external thread
- must show: major diameter, minor diameter, pitch, 60° angle; one crest in
  the accent colour
- must not: draw the thread as separate rings; omit units
- canon: T2, T3, T4
- done when: the reader points to pitch and major diameter unprompted

### V3: The unrolled ramp
- when: part 02 "Why it stays put"
- make: a cylinder with one turn of thread, beside the same turn unrolled into
  a right triangle: base = circumference, height = pitch
- must show: the lead angle (about 3° for M8), and for comparison a steeper
  line marking where steel-on-steel would begin to slide
- canon: T1, T10
- done when: the reader can say why a coarse standard thread does not unwind
  under steady load

### V4: Where the torque goes
- when: part 06 "Where the effort goes"
- make: one horizontal bar split 50 / 40 / 10, labelled under-head friction,
  thread friction, bolt stretch; a second bar below for a lubricated bolt
  with a visibly larger stretch share
- must not: use a pie chart; imply the lubricated shares are exact
- canon: Q4, Q5
- done when: the reader can explain why oil plus a dry torque figure is
  dangerous

### V5: Drive spotter
- when: part 03
- make: head-on views of slotted, PH, PZ, Torx, hex socket, square
- must show: the four extra lines of PZ in the accent colour
- canon: D2, D4, D6
- done when: the reader correctly names three screws from their own jar

### V6: Two holes
- when: part 04
- make: section through two boards with a wood screw: clearance hole above,
  pilot hole below; beside it the same joint without a clearance hole, boards
  held apart
- canon: W1, W2, W3
- done when: the reader can say which hole is which and what happens without
  the upper one

### V7: Reading a bolt head
- when: part 05
- make: hex head from above with "8.8" marking, annotated with the two sums
- canon: M1, M2
- done when: the reader decodes 10.9 alone

### V8: Slip and unwind
- when: part 07
- make: three-frame strip: joint clamped; joint slipping sideways; nut having
  turned a few degrees
- canon: L1, L2
- done when: the reader stops saying "vibration shakes it round" (X13)

### V9: Plug in a wall
- when: part 08
- make: sections of one expansion plug in solid masonry (expanded, gripping)
  and in plasterboard (nothing to grip); arrows for pull-out and hanging load
- must not: show any load figure
- canon: A2, A4, A5

### V10: Shear and pull-out
- when: part 09
- make: nail and screw side by side under a sideways load and under a
  straight pull, showing which does well at which
- canon: N1, N2

### V11: Bad neighbours
- when: part 10
- make: stainless screw in an aluminium plate with a water droplet; the
  aluminium pitted around the hole
- canon: R2

### V12: The reader's cheat card
- when: end of part 11, or the end of a *Fix my thing* session
- make: one printable A5 page containing only what this reader used: their
  screw sizes, their pilot and clearance holes, their torque figures, their
  wall type, each with its limit
- must not: include anything they did not meet; exceed one page
- done when: the reader says they would pin it up

## Web briefs

### W1: Thread explorer
- when: part 02, for readers who ask "what if"
- make: a page with sliders for diameter and pitch that redraws the thread
  profile to scale and reports advance per turn, lead angle, and whether the
  thread is self-locking for a chosen friction value
- presets: the canon coarse sizes M3–M12
- canon: T2–T5, T10
- test: M8 × 1.25 reports about 3° lead angle and 1.25 mm per turn

### W2: Torque and preload
- when: part 06 after the worked example
- make: choose size (M6–M12), class 8.8, thread condition (dry K 0.2,
  lubricated K 0.15); show target preload, torque, and what preload the *dry*
  torque would produce on a *lubricated* thread, against proof load
- must show: "Use the manufacturer's figure when there is one" at the top
- canon: M4, Q2, Q3, Q6, Q7
- test: M8, dry → about 25 N·m; M10, dry → about 50 N·m; dry torque on a
  lubricated M8 → preload about one third higher, at the proof load

### W3: Pilot hole helper
- when: part 04
- make: a page that walks the reader through measuring their own screw's core
  and choosing a bit, using the hold-the-bit-in-front method, with the canon
  4 mm example
- must not: output sizes for screws canon does not cover as if they were
  tabulated; it teaches the method
- canon: W1, W3, W4

### W4: Chooser
- when: part 11
- make: the part's question sequence as a short interactive path ending in a
  plain-language recommendation that cites parts
- must not: recommend for safety-critical uses; show the safety line and stop

## Audio briefs

### A1: Part read aloud
- when: the reader asks to listen
- make: narration of a written part. Tables are spoken as sentences. Formulas
  are spoken in words, once slowly.
- done when: nothing in it requires the page

### A2: Hands on the spanner
- when: part 06, the reader is at the job
- make: a 60–90 second spoken guide to tightening by feel: snug, the firm
  rise, stop if it goes soft; for several bolts, round in stages
- canon: Q8 and part 06 "Without a torque wrench"
- done when: usable without looking at a screen

### A3: What loose sounds like
- when: part 07, rung 3 only
- make: short described-or-synthesised contrast of a tight joint tapped and a
  loose one rattling, with a spoken note that a rattle means the clamp load
  has already gone
- canon: C5
