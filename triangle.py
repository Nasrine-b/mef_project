from point import Point
from math import sqrt, pow
import numpy as np

def phiRef(element, i:int, param:[float]):
    if(element.name == "Triangle"):
        if i == 0:
            return 1 - param[0] - param[1]
        elif i == 1:
            return param[0]
        elif i ==2 :
            return param[1]

class Triangle:
    _counter = 0

    def __init__(self,*args,physical_tag = -1): #   point1,point2,point3
        if len(args) == 3:
            self.name = "Triangle"
            self.id = Triangle._counter
            Triangle._counter += 1
            self.listPoint = [args[0],args[1],args[2]]
            self.tag = physical_tag
            x0 = self.listPoint[0].x
            x1 = self.listPoint[1].x
            x2 = self.listPoint[2].x
            y0 = self.listPoint[0].y
            y1 = self.listPoint[1].y
            y2 = self.listPoint[2].y
            self.area_ = float((1/2) * abs((x1-x0)*(y2-y0) - (y1-y0)*(x2-x0)))
        elif len(args) == 0:
            self.id = Triangle._counter
            Triangle._counter += 1
            self.listPoint = [()]
            self.tag = -1
        else:
            print("[ERROR] wrong number of arguments : point1, point2, point3")

    def area(self):
        return self.area_

    def jac(self):
        return 2*self.area_

    def __str__(self):
        return "Id = "+str(self.id)+": \n Point 0 : ("+str(self.listPoint[0])+")\n Point 1 : (" +str(self.listPoint[1])+")\n Point 2 : ("+str(self.listPoint[2])+")"

    def append(self, point1,point2,point3):
        self.listPoint.append(point1)
        self.listPoint.append(point2)
        self.listPoint.append(point3)

    def gaussPoint(self, order = 2):
        if order == 2:
            w = np.array([1/6, 1/6, 1/6])
            ksi = np.array([1/6, 4/6 , 1/6])
            eta =  np.array([1/6, 1/6, 4/6])
            x = np.zeros(order+1)
            y = np.zeros(order+1)
            for i in range(3):
                for j in range(3):
                    sx = self.listPoint[j].x
                    sy = self.listPoint[j].y
                    psi = phiRef(self,j,[ksi[i],eta[i]])
                    x[i] += psi * sx
                    y[i] += psi * sy
        elif order == 1:
            w = 1/6
            ksi = 1/3
            eta = 1/3
            x = 0
            y = 0
            for j in range(3):
                sx = self.listPoint[j].x
                sy = self.listPoint[j].y
                psi = phiRef(self,j,[ksi[i],eta[i]])
                x += psi * sx
                y += psi * sy
        return (w,ksi,eta,x,y)
