import fw
import content


def init_stage():
    rooms = [fw.Dungeon('Bedroom', fw.Rooms.Bedroom, {"bed": content.Item("bed", "soft and cozy"),
                                                      "closet": content.Item("closet", "where clothes might be"),
                                                      "pants": content.Item("pants", "I hate pants", True, True)},
                        {fw.Direction.West: fw.Rooms.Hallway}),
             fw.Dungeon('Hallway', fw.Rooms.Hallway, ['keys'],
                        {fw.Direction.West: fw.Rooms.Bathroom, fw.Direction.East: fw.Rooms.Bedroom,
                         fw.Direction.North: fw.Rooms.Exit, fw.Direction.South: fw.Rooms.Kitchen}),
             fw.Dungeon('Bathroom', fw.Rooms.Bathroom, {'sink': content.Item("sink", "drip drop"),
                                                        'shower': content.Item("shower", "makes people clean"),
                                                        'toilet': content.Item("toilet", "taking a dump?")},
                        {fw.Direction.East: fw.Rooms.Hallway}),
             fw.Dungeon('Kitchen', fw.Rooms.Kitchen, {'oven': content.Item("oven", "for pizza"),
                                                      'fridge': content.Item("fridge", "very empty")},
                        {fw.Direction.South: fw.Rooms.Hallway, fw.Direction.North: fw.Rooms.Yard}),
             fw.Dungeon('Yard', fw.Rooms.Yard, {'tire swing': content.Item("tire swing", "just for kids? meh")},
                        {fw.Direction.North: fw.Rooms.Kitchen})]
    dungeon_map = fw.Level(rooms, fw.Rooms.Bedroom)
    return dungeon_map

pickup = None
player = None
level = init_stage()  # initializes the dungeons
curDungeon = level.get_cur_dungeon()
print("Beep, beep. Good morning master! Welcome back to the living!\n What should I call you?")
name = input()
player = content.Player(name)
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
        loot = curDungeon.get_objects()
        print("which item would you like to pick up? ", loot.keys())
        pickup = input()
        if curDungeon.has_object(pickup):
            obj = curDungeon.get_obj(pickup)
            player.pick_up_obj(obj)
        else:
            print("Do you have hallucinations? There is no such item here")
    elif usr_input == 'exit':
        break
    else:
        print("nah not that way")
        continue
