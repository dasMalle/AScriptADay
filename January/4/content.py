class Player:
    __name = ""
    __inventory = []
    __dressed = None

    def __init__(self, name):
        self.__name = name

    def pick_up_obj(self, obj):
        if obj.is_pickable():
            self.__inventory.append(obj)
            print("Great now I am carrying ", obj.get_name())
        else:
            print("I can't carry that!")

    def drop_obj(self, obj):
        if type(obj) is Item:
            if self.__inventory.count(obj) >= 1:
                self.__inventory.remove(obj)
                print("The floor is a better place for you ", obj.get_name())
            else:
                print("I don't even have that thing")
        else:
            print("Are you kidding me that's not even a thing!")

    def get_inventory(self):
        return self.__inventory

    def get_dressed(self, obj):
        if type(obj) is Item:
            if obj.is_wearable():
                self.__dressed = True
                print("Great now I am wearing ", obj.get_name())
        else:
            print("I can't wear that!")


class Item:
    __name = ""
    __pickable = False
    __wearable = False
    __description = ""

    def __init__(self, name, interaction, pickable=False, wearable=False):
        self.__name = name
        self.__pickable = pickable
        self.__wearable = wearable
        self.__description = interaction

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def is_pickable(self):
        return self.__pickable

    def is_wearable(self):
        return self.__wearable

    def __str__(self):
        return self.__name
