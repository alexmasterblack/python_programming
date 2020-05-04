class Balance:
    def __init__(self):
        self.right_side = 0
        self.left_side = 0
    
    def add_left(self, item):
        self.left_side = self.left_side + item

    def add_right(self, item):
        self.right_side = self.right_side + item

    def result(self):
        if self.left_side == self.right_side:
            return ('=')
        elif self.left_side > self.right_side:
            return ('L')
        else:
            return ('R')

balance = Balance()
balance.add_right(10)
balance.add_left(5)
balance.add_left(5)
print(balance.result())
balance.add_left(1)
print(balance.result())