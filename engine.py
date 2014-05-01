import ConfigParser

DEBUG = True


class Map(object):

    def __init__(self):
        self.scenes = dict()

    def add_scene(self, name, scene):
        if DEBUG:
            print "Adding %r in Map.add_scene() as %r" % (name, scene)
        assert isinstance(name, str)
        assert isinstance(scene, Scene)
        self.scenes[name] = scene

    def load_scenes(self, filename):
        if DEBUG:
            print "Loading scenes from %r" % filename
        assert isinstance(filename, str)
        map_db = ConfigParser.ConfigParser()
        map_db.read(filename)
        for each in map_db.items('Scenes'):
            s_name, s_desc = each
            new_scene = Scene(s_desc, set())
            self.add_scene(s_name, new_scene)
        for each in map_db.items('Exits'):
            s_name, e_list = each
            for next_exit in e_list.split(','):
                if DEBUG:
                    print "Adding exit %r in %r" % (next_exit, s_name)
                self.scenes[s_name].add_exit(self.scenes[next_exit])
        self.start_scene = self.scenes[map_db.get('Player', 'start_scene')]


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
        if len(self.props) > 0:
            print "You see:"
            for prop in self.props:
                print "- %s" % prop
        else:
            print "Nothing notable here."
        print self.exits


class Prop(object):

    def __init__(self, description, location):
        assert isinstance(description, str)
        # prop should be in a Scene or a Player inventory
        assert isinstance(location, Scene) or isinstance(location, set)
        self.description = description
        self.location = location
        self.location.add_prop(self)

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
