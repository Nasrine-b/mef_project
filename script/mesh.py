from triangle import Triangle
from segment import Segment
from point import Point
from math import sqrt, pow
import gmsh
import sys
class Mesh:

    def __init__(self,*args): #Point, segment, triangle
        self.listPoint = []
        self.listTrig = []
        self.listSeg = []
        self.npts = 0

    def __str__(self):
        return "Id = "+str(self.id)+": \n Point 0 : ("+str(self.listPoint[0][1])+")\n Point 1 : (" +str(self.listPoint[1][1])+")\n Point 2 : ("+str(self.listPoint[2][1])+")"

    def GmshToMesh(self,filename=""):
        gmsh.open(filename)
        #Récupérer les points
        nodes = gmsh.model.mesh.getNodes()
        if not len(nodes[1]):
            print("[ERROR] le fichier {} est vide!".format(filename))
            sys.exit(1)
        print(nodes)
        for i in range(0,len(nodes[1]),3):
            pt = Point(nodes[1][i] , nodes[1][i+1])
            self.listPoint.append(pt)
        self.npts = len(self.listPoint)

        phys_group = gmsh.model.getPhysicalGroups()
        for (dim,tag) in phys_group:
            id_entity = gmsh.model.getEntitiesForPhysicalGroup(dim,tag)
            if dim == 1:
                for id_seg in id_entity :
                    idSeg_idPt = gmsh.model.mesh.getElements(dim,id_seg) #identifiant segment / identifiant point
                    idSeg = idSeg_idPt[1][0]
                    idPt = idSeg_idPt[2][0]
                    for i in range(0,len(idPt),2):
                        pt1 = self.listPoint[int(idPt[i]) - 1 ]
                        pt2 = self.listPoint[int(idPt[i+1]) -1]
                        seg = Segment(pt1,pt2,physical_tag = tag)
                        self.listSeg.append(seg)
            if dim == 2:
                for id_trig in id_entity :
                    idTrig_idPt = gmsh.model.mesh.getElements(dim,id_trig) #identifiant triangle / identifiant point
                    idTrig = idTrig_idPt[1][0]
                    idPt = idTrig_idPt[2][0]
                    for i in range(0,len(idPt),3):
                        pt1 = self.listPoint[int(idPt[i]) - 1 ]
                        pt2 = self.listPoint[int(idPt[i+1]) -1]
                        pt3 = self.listPoint[int(idPt[i+2]) -1]
                        trig = Triangle(pt1,pt2,pt3,physical_tag = tag)
                        self.listTrig.append(trig)

    def getElements(self,dim,physical_tag):
        if dim == 1 :
            list = []
            for i in range(len(self.listSeg)):
                tag = self.listSeg[i].tag
                if tag == physical_tag :
                    list.append(self.listSeg[i])
            return list
        elif dim == 2 :
            list = []
            for i in range(len(self.listTrig)):
                tag = self.listTrig[i].tag
                if tag == physical_tag :
                    list.append(self.listTrig[i])
            return list

    def getPoints(self,dim,physical_tag):
        points = []
        if dim == 1 :
            list = self.getElements(dim,physical_tag)
            for i in range(len(list)):
                points.append(list[i].listPoint[0])
                points.append(list[i].listPoint[1])
        elif dim == 2 :
            list = self.getElements(dim,physical_tag)
            for i in range(len(list)):
                points.append(list[i].listPoint[0])
                points.append(list[i].listPoint[1])
                points.append(list[i].listPoint[2])
        return points

    def Loc2Glob(self,idTrig,index):
        return self.listTrig[idTrig].listPoint[index].id
