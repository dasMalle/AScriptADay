# today just a singleton pattern, with help from this book: https://www.packtpub.com/application-development/python-unlocked
# I find singletons super useful in game development, in normal software dev be careful with them though!
from six import with_metaclass


class Singleton(type):
    _registry = {}

    def __call__(cls, *args, **kwargs):
        if cls not in Singleton._registry:
            Singleton._registry[cls] = type.__call__(cls, *args, **kwargs)
        return Singleton._registry[cls]


class Me(with_metaclass(Singleton, object)):

    def __init__(self, data):
        print("initialized", data)
        self.data = data

m = Me(2)
n = Me(3)
print(m.data, n.data)