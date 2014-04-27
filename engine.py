class Map(object):

    def __init__(self, scenes):
        assert isinstance(scenes, set)
        self.scenes = scenes

    def add_scene(self, scene):
        assert isinstance(scene, Scene)
        self.scenes.add(scene)


class Scene(object):

    def __init__(self, description, props):
        assert isinstance(description, str)
        assert isinstance(props, set)
        self.description = description
        self.props = props
        self.exits = set()

    def add_exit(self, next_scene):
        assert isinstance(next_scene, Scene)
        self.exits.add(next_scene)

    def add_prop(self, prop):
        assert isinstance(prop, Prop)
        self.props.add(prop)

    def remove_prop(self, prop):
        assert prop in self.props
        self.props.discard(prop)

    def enter(self):
        print self.description
        print self.props


class Prop(object):

    def __init__(self, description, location):
        assert isinstance(description, str)
        # prop should be in a Scene or a Player inventory
        assert isinstance(location, Scene) or isinstance(location, set)
        self.description = description
        self.location = location

    # how do we move these? does the Prop really need to know its location?


class Player(object):

    def __init__(self, location):
        assert isinstance(location, Scene)
        self.location = location
        self.inventory = set()
        self.location.enter()

    def move(self, new_location):
        assert new_location in self.location.exits
        self.location = new_location
        self.location.enter()
