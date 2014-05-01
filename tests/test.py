import engine


my_map = engine.Map()
my_map.load_scenes('example.map')


def test_load_scenes():
    assert len(my_map.scenes) == 2


def test_start_player():
    me = engine.Player(my_map.start_scene)
    assert me.location == my_map.start_scene


def test_move_player():
    me = engine.Player(my_map.start_scene)
    me.move(my_map.scenes['cave_entrance'])
    assert me.location == my_map.scenes['cave_entrance']

def test_insert_prop():
    treasure_map = engine.Prop('a treasure map', my_map.scenes['cave_outside'])
    assert treasure_map.location == my_map.scenes['cave_outside']
    assert treasure_map in my_map.scenes['cave_outside'].props
