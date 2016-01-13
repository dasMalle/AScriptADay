class Level:
    __map = {}  # this hold the list with all the rooms, and therefore also their connections.
    __curPos = None  # player position (Dungeon)

    def __init__(self, dungeon_map, startPos):
        self.__map = dungeon_map
        self.__curPos = startPos

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
    __objects = []
    __connection = {}  # dictionary of direction and next room

    def __init__(self, name, index,  objects, connection):
        self.__name = name
        self.__index = index
        self.__objects = objects
        self.__connection = connection

    def get_name(self):
        return self.__name

    def get_index(self):
        return self.__index

    def set_objects(self, objects):
        self.__objects = objects

    def get_objects(self):
        return self.__objects

    def get_connection(self, direction=None):
        if direction is None:
            return self.__connection
        else:
            return self.__connection.get(direction)

    def toString(self):
        return "The following objects are lying around in the {}: {}. It has {} doors".format(self.__name,
                                                                                              self.__objects,
                                                                                              len(self.get_connection()))


class Direction:
    East, West, North, South = range(4)


class Rooms:
    Bedroom, Hallway, Bathroom, Kitchen, Yard, Exit = range(6)




def init_stage():
    rooms = [Dungeon('Bedroom', Rooms.Bedroom, ['bed', 'closet'], {Direction.West: Rooms.Hallway}),
             Dungeon('Hallway', Rooms.Hallway, ['keys'], {Direction.West: Rooms.Bathroom, Direction.East: Rooms.Bedroom,
                                           Direction.North: Rooms.Exit, Direction.South: Rooms.Kitchen}),
             Dungeon('Bathroom', Rooms.Bathroom, ['sink', 'shower', 'toilet'], {Direction.East: Rooms.Hallway}),
             Dungeon('Kitchen', Rooms.Kitchen, ['oven', 'fridge'], {Direction.South: Rooms.Hallway,
                                                                    Direction.North: Rooms.Yard}),
             Dungeon('Yard', Rooms.Yard, ['tire swing'], {Direction.North: Rooms.Kitchen})]
    dungeon_map = Level(rooms, Rooms.Bedroom)
    return dungeon_map


level = init_stage()  # initializes the dungeons
print("Beep, beep. Good morning master! Welcome back to the living!\n What should I call you?")
name = input()
print("Alright I will call you %s! Please get out of bed and ready for work %s. "% (name, name))
print("press n for north, e for east, s for south or w for west. 'exit' quits the game.")

while True:
    level.print_cur_dungeon()
    # print("\n <")
    usr_input = input()
    if usr_input == 'n':
        print(level.move(Direction.North))
    elif usr_input == 'e':
        print(level.move(Direction.East))
    elif usr_input == 's':
        print(level.move(Direction.South))
    elif usr_input == 'w':
        print(level.move(Direction.West))
    elif usr_input == 'exit':
        break
    else:
        print("nah not that way")
        continue


