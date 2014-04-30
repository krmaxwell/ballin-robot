import engine


def test_load_scenes():
    my_map = engine.Map()
    my_map.load_scenes('example.map')
    assert len(my_map.scenes) == 2

def test_start_player():
    my_map = engine.Map()
    my_map.load_scenes('example.map')
    me = engine.Player(my_map.start_scene)
    assert me.location == my_map.start_scene

def test_move_player():
    my_map = engine.Map()
    my_map.load_scenes('example.map')
    me = engine.Player(my_map.start_scene)
    me.move(my_map.scenes['cave_entrance'])
    assert me.location == my_map.scenes['cave_entrance']
