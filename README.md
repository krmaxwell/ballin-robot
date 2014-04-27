ballin-robot
============

Game engine for text-based adventure games (experimental toy only).

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
