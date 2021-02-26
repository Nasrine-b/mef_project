from point import Point
from math import sqrt, pow

class Segment:
    _counter = 0

    def __init__(self,*args,physical_tag = -1 ):    #   point1, point2
        if len(args) == 2:
            self.name = "Segment"
            self.id = Segment._counter
            Segment._counter += 1
            self.listPoint = [args[0],args[1]]
            x0 = self.listPoint[0].x
            x1 = self.listPoint[1].x
            y0 = self.listPoint[0].y
            y1 = self.listPoint[1].y
            self.tag = physical_tag
            self.area_ = sqrt( pow((x0 - x1),2) + pow((y0 - y1) , 2) )
        elif len(args) == 0:
            self.id = Segment._counter
            Segment._counter += 1
            self.listPoint = []
            self.tag = -1
        else:
            print("[ERROR] wrong number of arguments : point1, point2")

    def area(self):
        return self.area_

    def jac(self):
        return self.area_

    def __str__(self):
        return "Id = "+str(self.id)+": \n Point 0 : ("+str(self.listPoint[0])+")\n Point 1 : (" +str(self.listPoint[1])+")"

    def append(self, point1,point2):
        self.listPoint.append(point1)
        self.listPoint.append(point2)
