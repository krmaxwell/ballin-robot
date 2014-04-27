def Map(object):

    def __init__(self, scenes):
        assert isinstance(scenes, set)
        self.scenes = scenes

    def add_scene(scene):
        assert isinstance(scene, Scene)
        self.scenes.add(scene)


def Scene(object):
    
    def __init__(self, description, props):
        assert isinstance(description, string)
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


def Prop(object):

    def __init__(self, description, location):
        assert isinstance(description, string)
        # prop should be in a Scene or a Player inventory
        assert isinstance(location, Scene) or isinstance(location, set)
        self.description = description
        self.location = location

    # how do we move these? does the Prop really need to know its location?


def Player(object):

    def __init__(self, location):
        pass

    inventory = set()
