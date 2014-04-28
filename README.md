ballin-robot
============

Game engine for text-based adventure games (experimental toy only). Partly works for [LPTHW Exercise 45](http://learnpythonthehardway.org/book/ex45.html).

Architecture
------------

There are a few core types of objects:

- Map: Container object for Scenes
- Scene: Location object that has exits to other Scenes. Also contains Props.
- Prop: Object contained within either a Scene or a Player inventory.
- Player: Object representing our location in the Map (Scene). Has an inventory.
- Inventory: Container object for any Props carried by the Player.

**Still to decide**: How will we implement verbs: 
- text-based with a natural language parser?
- explicitly listed verbs per prop?

Future ideas
------------
- Web interface (e.g. using Bottle)
  - different backgrounds on a per-scene basis?
- RPG elements (e.g. player stats)
- NPCs
- Combat system???
