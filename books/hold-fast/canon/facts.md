# Canon: facts

Binding for the agent. One statement per item. Units always. Where a number is
a rule of thumb, its limits are stated; outside them, use manufacturer data.

## C: Clamping

- C1. A threaded fastener's main job is to create **clamp load**: it squeezes
  the parts together.
- C2. A tightened bolt is a stretched spring. The tension in it is called
  **preload**. Preload equals clamp load when no outside force acts.
- C3. In a well-designed bolted joint, sideways (shear) load is carried by
  **friction** between the clamped parts, not by the bolt's shank.
- C4. Friction force available = clamp load × coefficient of friction.
  Dry steel on steel is roughly 0.15–0.2.
- C5. A joint that keeps its clamp load keeps its strength and stays tight.
  Most fastener failures in service begin with loss of clamp load.
- C6. Wood screws and nails also work by clamping and friction, but wood
  creeps and shrinks, so their clamp load fades over time. They rely more on
  the fastener's own body than a steel joint does.

## T: Threads

- T1. A thread is a helix: an inclined plane wrapped around a cylinder.
- T2. **Major diameter**: across the thread crests. It is the nominal size
  (M8 ≈ 8 mm). **Minor (root) diameter**: across the bottoms of the grooves.
- T3. **Pitch**: distance from one crest to the next, measured along the axis.
  For a single-start thread, one full turn advances the screw by one pitch.
- T4. ISO metric and Unified inch threads have a 60° angle between flanks.
- T5. ISO metric **coarse** pitches (mm): M3 0.5, M4 0.7, M5 0.8, M6 1.0,
  M8 1.25, M10 1.5, M12 1.75. Coarse is the default; if no pitch is written,
  it is coarse.
- T6. A metric screw is named `M<diameter> × <length>`; a fine pitch is added
  as `M8 × 1.0 × 40`. Length is measured from under the head, except for
  countersunk screws, which are measured overall.
- T7. Inch threads are named diameter–threads per inch: `1/4-20` is 1/4 inch,
  20 threads per inch (UNC, coarse). UNF is the fine series.
- T8. Metric and inch threads do not interchange. Some pairs are close enough
  to start and then jam or strip, notably M8 × 1.25 and 5/16-18.
- T9. Almost all threads are right-hand: clockwise tightens. Left-hand threads
  are used where rotation would loosen a right-hand one; the left pedal of a
  bicycle is the common example.
- T10. The lead angle of a standard coarse thread is small (about 3° for M8),
  less than the friction angle of steel on steel. So a standard thread is
  **self-locking** under steady load: it will not spin loose by itself.
- T11. Wood screws, sheet-metal screws and chipboard screws have widely spaced,
  sharp threads that form their own mating thread in the material. Machine
  screws and bolts need a nut or a tapped hole.
- T12. A fine thread has a larger stress area and adjusts more precisely; a
  coarse thread is quicker, more tolerant of dirt and damage, and better in
  soft materials.

## D: Heads and drives

- D1. Head shape decides how the head sits: **countersunk** sits flush in a
  conical recess; **pan, button, cheese, hex** sit on the surface and bear on
  a flat area.
- D2. Phillips (PH) and Pozidriv (PZ) are different. PZ has four extra thin
  radial lines on the head and near-parallel flanks. A PH bit in a PZ screw,
  or the reverse, slips and damages both.
- D3. Phillips tends to **cam out** (the bit climbs out) under high torque.
- D4. Torx (TX, six-lobe) and hex socket transmit torque without an axial
  push and hardly cam out. Common sizes: T20 for 4 mm wood screws, T25 for
  4.5–5 mm, T30 for 6 mm.
- D5. The most common cause of a stripped head is the wrong size or type of
  bit, worn bits second.
- D6. Slotted drives centre poorly and slip sideways; they survive because
  they are easy to make and can be cleaned out.

## W: Wood

- W1. Two different holes: a **clearance hole** in the top piece, as wide as
  the screw's shank or thread so the screw slides through; a **pilot hole** in
  the bottom piece, about the screw's root diameter.
- W2. Without a clearance hole (or an unthreaded shank) in the top piece, the
  thread grips both pieces and can hold them apart ("jacking").
- W3. Pilot hole rule of thumb: root diameter in hardwood; slightly smaller
  in softwood. For a 4 mm wood screw that is about 2.5 mm in hardwood and
  2 mm in softwood.
- W4. Pilot holes prevent splitting, most needed near ends and edges and in
  hardwood.
- W5. Screws hold far worse in **end grain** than across the grain; treat end
  grain as roughly half as strong or less and prefer another joint.
- W6. Rule of thumb for length: about two-thirds of the screw in the piece
  that receives the thread.
- W7. Hardened screws (drywall screws especially) are brittle and snap under
  shear or bending. They are not structural fasteners.
- W8. Chipboard and MDF hold screws weakly near edges and after a screw has
  been removed and re-driven.

## M: Metal joints

- M1. Property class on a metric steel bolt head, e.g. **8.8**: first number
  × 100 = nominal tensile strength in MPa (800); first × second × 10 = yield
  strength in MPa (640).
- M2. Common classes: 4.6 (400/240 MPa), 8.8 (800/640), 10.9 (1000/900),
  12.9 (1200/1080).
- M3. Stainless A2-70 and A4-70: 700 MPa tensile, about 450 MPa yield. A4
  resists chlorides (sea, road salt) better than A2.
- M4. Tensile stress area (mm²), coarse thread: M5 14.2, M6 20.1, M8 36.6,
  M10 58.0, M12 84.3.
- M5. A nut should be of a class matching the bolt (class 8 nut for 8.8 bolt).
  A standard full nut is designed so the bolt breaks before the threads strip.
- M6. Thread engagement in a tapped hole, rule of thumb: about 1 × diameter
  in steel, 1.5–2 × diameter in aluminium.
- M7. Tap drill for a metric coarse thread ≈ diameter − pitch: M6 5.0 mm,
  M8 6.8 mm, M10 8.5 mm.
- M8. Clearance hole, medium fit (mm): M3 3.4, M4 4.5, M5 5.5, M6 6.6, M8 9,
  M10 11, M12 13.5.
- M9. A flat washer spreads load, protects the surface and gives consistent
  friction under the turning part. It is not a locking device.

## Q: Torque

- Q1. Torque is turning force × lever length, in newton-metres (N·m).
- Q2. Short formula: **T ≈ K × F × d**. T torque (N·m), F preload (N),
  d nominal diameter (m), K the "nut factor".
- Q3. K is about 0.2 for dry, plain or zinc-plated steel as supplied; about
  0.15 or lower when lubricated. It varies widely with finish and lubricant.
- Q4. Roughly 90 % of tightening torque is spent on friction (about 50 % under
  the head or nut, about 40 % in the threads). Only about 10 % stretches the
  bolt.
- Q5. Because of Q4, the same torque can give preload scattered by about
  ±25 % or more. Lubricating a thread and using a dry-torque value can
  over-tighten the bolt severely.
- Q6. A common target preload is about 75 % of the bolt's proof load.
  Proof stress for class 8.8 up to M16 is 580 MPa.
- Q7. Approximate dry torques for class 8.8, coarse thread, K = 0.2, 75 % of
  proof: M6 10 N·m, M8 25 N·m, M10 50 N·m, M12 88 N·m. These are examples of
  the calculation. When a manufacturer gives a torque, that value wins.
- Q8. Tighten multi-bolt joints in stages and in a criss-cross pattern.
- Q9. A click-type torque wrench is stored at its lowest setting and is used
  for tightening only.

## L: Loosening

- L1. The main cause of bolts rotating loose is repeated **sideways slip** of
  the joint, which momentarily frees the thread friction (shown by Junker's
  transverse vibration test).
- L2. The first defence is enough preload that the joint never slips.
- L3. Clamp load is also lost without rotation: surfaces bed in, gaskets and
  paint creep, wood shrinks.
- L4. A longer bolt clamping the same joint stretches more for the same
  preload and so loses less when the joint settles.
- L5. Plain split (helical spring) washers do little to prevent loosening
  under vibration in tests.
- L6. Things that do work: wedge-locking washer pairs, thread-locking
  adhesive, prevailing-torque (nylon-insert) nuts, lock wire, castellated nuts
  with split pins. Nylon-insert nuts stop the nut from falling off; they do
  not preserve preload.
- L7. Medium-strength threadlocker can be undone with hand tools;
  high-strength usually needs heat.

## A: Walls and anchors

- A1. Identify the wall before choosing a fixing: solid masonry or concrete,
  hollow block, plasterboard on studs, or wood.
- A2. A plastic expansion plug works by being forced against the sides of the
  hole. The hole must be the plug's diameter, clean, and as deep as the screw
  will reach.
- A3. Plug and screw must match; the plug's packaging gives the screw range.
  A typical 8 mm plug takes a 4.5–6 mm screw.
- A4. Plasterboard alone is weak. Heavy loads go into the studs or onto
  fixings made for hollow walls (toggles, metal cavity anchors).
- A5. Load **pulling straight out** of a wall or ceiling is far more severe
  for an anchor than load hanging **down along** the wall.
- A6. Rated loads on anchor packaging apply only to the stated base material
  and installation.

## N: Other fasteners

- N1. Nails hold well in shear and bend rather than snap; they resist being
  pulled straight out poorly compared with screws.
- N2. Screws resist pull-out well and can be removed; ordinary hardened wood
  screws are weaker than nails in shear and bending.
- N3. Rivets make a permanent joint and suit thin sheet; a blind ("pop") rivet
  is set from one side.
- N4. A good glued wood joint along the grain is stronger than the wood
  itself; glue is weak on end grain and under peeling.
- N5. Joinery (mortise, dovetail, dowel) carries load through shape; fasteners
  then only keep the joint closed.

## R: Materials and corrosion

- R1. Zinc plating gives light indoor protection. Hot-dip galvanising gives
  long outdoor protection and a thick, rough coat that needs matching nuts.
- R2. Two different metals touching in the presence of water form a galvanic
  pair; the less noble metal corrodes faster. Stainless screws in aluminium
  with salt water attack the aluminium.
- R3. Stainless threads can **gall** (cold-weld) when tightened dry and fast.
  Lubricate and go slowly.
- R4. Stainless A2/A4-70 is weaker than class 8.8 steel. It is not a drop-in
  replacement in a highly loaded joint.
- R5. High-strength steel (10.9 and above) that has been electroplated can
  suffer hydrogen embrittlement and fail after a delay.
- R6. Brass screws are soft; in hardwood, drive a steel screw of the same size
  first to form the thread.
