import engine



my_map = engine.Map()
my_map.load_scenes('example.map')

me = engine.Player(my_map.start_scene)
me.move(my_map.scenes['cave_entrance'])
