import engine

my_map = engine.Map([]) # no scenes at first, we will build these

cave_outside = engine.Scene('You see the entrance to a cave in the side of a hill.', set())
my_map.add_scene(cave_outside)

cave_entrance = engine.Scene('Your eyes adjust quickly to the darkness. A small chest sits off to the side.', set())
my_map.add_scene(cave_entrance)

cave_outside.add_exit(cave_entrance)
cave_entrance.add_exit(cave_outside)

me = engine.Player(cave_outside)
