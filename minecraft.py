class BaseObject:
    def __init__(self, x, y, z):
        self.coord = (x, y, z)

    def get_coordinates(self):
        return (self.coord) 

class Block(BaseObject):
    def shatter(self):
        self.coord = (None, None, None)

class Entity(BaseObject):
    def move(self, x, y, z):
        self.coord = (x, y, z)

class Thing(BaseObject):
    pass

minecraft = BaseObject(4, 5, 0)

print(minecraft.get_coordinates())