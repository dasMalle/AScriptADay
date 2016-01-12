import fw


def init_stage():
    rooms = [fw.Dungeon('Bedroom', fw.Rooms.Bedroom, ['bed', 'closet'],
                        {fw.Direction.West: fw.Rooms.Hallway}),
             fw.Dungeon('Hallway', fw.Rooms.Hallway, ['keys'],
                        {fw.Direction.West: fw.Rooms.Bathroom, fw.Direction.East: fw.Rooms.Bedroom,
                         fw.Direction.North: fw.Rooms.Exit, fw.Direction.South: fw.Rooms.Kitchen}),
             fw.Dungeon('Bathroom', fw.Rooms.Bathroom, ['sink', 'shower', 'toilet'],
                        {fw.Direction.East: fw.Rooms.Hallway}),
             fw.Dungeon('Kitchen', fw.Rooms.Kitchen, ['oven', 'fridge'], {fw.Direction.South: fw.Rooms.Hallway,
                                                                          fw.Direction.North: fw.Rooms.Yard}),
             fw.Dungeon('Yard', fw.Rooms.Yard, ['tire swing'], {fw.Direction.North: fw.Rooms.Kitchen})]
    dungeon_map = fw.Level(rooms, fw.Rooms.Bedroom)
    return dungeon_map


level = init_stage()  # initializes the dungeons
print("Beep, beep. Good morning master! Welcome back to the living!\n What should I call you?")
name = input()
print("Alright I will call you %s! Please get out of bed and ready for work %s. "% (name, name))
print("press n for north, e for east, s for south or w for west. p for picking up objects, 'exit' quits the game.")

while True:
    level.print_cur_dungeon()
    # print("\n <")
    usr_input = input()
    if usr_input == 'n':
        print(level.move(fw.Direction.North))
    elif usr_input == 'e':
        print(level.move(fw.Direction.East))
    elif usr_input == 's':
        print(level.move(fw.Direction.South))
    elif usr_input == 'w':
        print(level.move(fw.Direction.West))
    elif usr_input == 'p':
        curDungeon = level.get_cur_dungeon()
        print("which item would you like to pick up? ", curDungeon.get_objects())
        input()
        print("nah way too heavy")
    elif usr_input == 'exit':
        break
    else:
        print("nah not that way")
        continue
