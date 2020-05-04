class Polynomial:
    def __init__(self, line):
        self.line = line
        self.size = len(line)

    def __call__(self, other):
        result = 0
        for i in range(self.size):
            result = result + self.line[i] * (other ** i)
        return result

    def __add__(self, other):
        maximum = max(self.size, len(other.line))
        result = [0 for i in range(maximum)]
        for i in range(maximum):
            if self.size > i:
                result[i] = result[i] + self.line[i]
            if len(other.line) > i:
                result[i] = result[i] + other.line[i]
        return Polynomial(result)
        
poly1 = Polynomial([0, 1])
poly2 = Polynomial([10])
poly3 = poly1 + poly2
poly4 = poly2 + poly1
print(poly3(-2), poly4(-2))
print(poly3(-1), poly4(-1))
print(poly3(0), poly4(0))
print(poly3(1), poly4(1))
print(poly3(2), poly4(2))