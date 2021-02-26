class Point:
    _counter = 0
    def __init__(self, x, y):
        self.id = Point._counter
        Point._counter += 1
        self.x = x
        self.y = y
    def __str__(self):
        return "Id = "+str(self.id)+", ("+str(self.x)+", "+str(self.y)+")"

if __name__ == '__main__':
    pt = Point(4,5)
    pt2 = Point(10,11)
    print(pt)
    print(pt2)
