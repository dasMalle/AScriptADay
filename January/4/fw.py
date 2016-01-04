import content

class Level:
    __map = {}  # this hold the list with all the rooms, and therefore also their connections.
    __curPos = None  # player position (Dungeon)

    def __init__(self, dungeon_map, start_pos, inventory=None):
        self.__map = dungeon_map
        self.__curPos = start_pos
        self.__inventory = inventory

    def set_map(self, dungeonmap):
        self.__map = dungeonmap

    def get_map(self):
        return self.__map

    def get_curPos(self):
        return self.__curPos

    def set_curPos(self, newPos):
        self.__curPos = newPos

    def print_cur_dungeon(self):
        dungeon = self.__map[self.__curPos]
        print(dungeon.toString())

    def get_cur_dungeon(self):
        return self.__map[self.__curPos]

    def move(self, direction):
        dungeon = self.__map[self.__curPos]
        next_room = dungeon.get_connection(direction)
        if next_room is not None:
            self.__curPos = next_room
            return "moving"
        else:
            return "wall"


class Dungeon:
    __name = ""
    __index = None
    __objects = {}
    __connection = {}  # dictionary of direction and next room

    def __init__(self, name, index, objects, connection):
        self.__name = name
        self.__index = index
        self.__objects = objects
        self.__connection = connection

    def get_name(self):
        return self.__name

    def get_index(self):
        return self.__index

    def add_obj(self, name, item):
        self.__objects[name] = item

    def get_obj(self, key):
        item = self.__objects.get(key)
        if type(item) is content.Item:
            return item

    def set_objects(self, objects):
        self.__objects = objects

    def get_objects(self):
        return self.__objects

    def get_connection(self, direction=None):
        if direction is None:
            return self.__connection
        else:
            return self.__connection.get(direction)

    def has_object(self, obj):
        return obj in self.__objects

    def toString(self):
        return "The following objects are lying around in the {}: {}. It has {} doors".format(self.__name,
                                                                                              self.__objects.keys(),
                                                                                              len(self.get_connection()))

class Direction:
    East, West, North, South = range(4)


class Rooms:
    Bedroom, Hallway, Bathroom, Kitchen, Yard, Exit = range(6)