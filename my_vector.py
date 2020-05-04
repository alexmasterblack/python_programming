import math

class MyVector:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def __add__(self,  other):
        new_x1 = self.x1 + other.x1
        new_x2 = self.x2 + other.x2
        return MyVector(new_x1, new_x2)

    def __iadd__(self, other):
        self.x1 += other.x1
        self.x2 += other.x2
        return self
    
    def __sub__(self, other):
        new_x1 = self.x1 - other.x1
        new_x2 = self.x2 - other.x2
        return MyVector(new_x1, new_x2)

    def __mul__(self, other):
        new_x1 = self.x1 * other
        new_x2 = self.x2 * other
        return MyVector(new_x1, new_x2)

    def __rmul__(self, other):
        new_x1 = self.x1 * other
        new_x2 = self.x2 * other
        return MyVector(new_x1, new_x2)

    def __imul__(self, other):
        self.x1 *= other
        self.x2 *= other
        return self

    def __eq__(self, other):
        if self.x1 == other.x1 and self.x2 == other.x2:
            return True
        else: 
            return False
    
    def __ne__(self, other):
        if self.x1 != other.x1 and self.x2 != other.x2:
            return True
        else: 
            return False
    
    def __len__(self):
        return math.floor(math.sqrt(self.x1 ** 2 + self.x2 ** 2))

    def __str__(self):
        return 'MyVector({}, {})'.format(self.x1, self.x2)
  

v1 = MyVector(-2, 5)
v2 = MyVector(3, -4)
v_sum = v1 + v2
print(v_sum)