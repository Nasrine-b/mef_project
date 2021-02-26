from triangle import Triangle
from segment import Segment
from point import Point
from mesh import Mesh
from triplet import Triplet
from math import sqrt, pow
import math
import matplotlib.pyplot as plt
from scipy.sparse import coo_matrix, linalg
import numpy as np
import matplotlib.cm as cm

import gmsh
import sys

#   element = seg ou trig
def mass_elem(element, triplets, alpha = 1.):
    if(element.name == "Triangle"): #   vérifier que c'est un trig
        Tp = float(element.area_)
        Tp /= 12
        Tp *= alpha
        #   construction matrice
        for i in range(3):
            for j in range(3):
                if i == j:
                    triplets.append(i,j,2*Tp)
                else :
                    triplets.append(i,j,Tp)

def Mass(msh, dim, physical_tag, triplets):
    if(dim == 2):
        listElements = msh.getElements(dim,physical_tag)
        for k in range(len(listElements)):
            matrice = Triplet()
            mass_elem(listElements[k],matrice)
            for i in range(3):
                I = msh.Loc2Glob(k,i)
                for j in range(3):
                    J = msh.Loc2Glob(k,j)
                    triplets.append(I,J,matrice.getElemAtIndex(i,j))

def rigidite_elem(element,triplets):
    if(element.name == "Triangle"): #   vérifier que c'est un trig
        Tp = float(element.area_)
        #   construction matrice Bp
        A = (1/element.jac())*(element.listPoint[2].y - element.listPoint[0].y)
        B = (1/element.jac())*(element.listPoint[0].y - element.listPoint[1].y)
        C = (1/element.jac())*(element.listPoint[0].x - element.listPoint[2].x)
        D = (1/element.jac())*(element.listPoint[1].x - element.listPoint[0].x)
        Bp = np.array([[A,B],[C,D]])
        BpT = Bp.transpose()
        mult = np.matmul(BpT,Bp)
        for i in range(3):
            for j in range(3):
                res = np.matmul(gradphi(element,j).transpose(),mult)
                res = np.matmul(res,gradphi(element,i))
                triplets.append(i,j,Tp*res)

def gradphi(element, i:int):
    if(element.name == "Triangle"):
        if i==0:
            return np.array([-1,-1])
        elif i == 1:
            return np.array([1,0])
        elif i == 2:
            return np.array([0,1])

def Rigidite(msh, dim, physical_tag, triplets):
    if(dim == 2):
        listElements = msh.getElements(dim,physical_tag)
        for k in range(len(listElements)):
            matrice = Triplet()
            rigidite_elem(listElements[k],matrice)
            for i in range(3):
                I = msh.Loc2Glob(k,i)
                for j in range(3):
                    J = msh.Loc2Glob(k,j)
                    triplets.append(I,J,matrice.getElemAtIndex(i,j))

def phiRef(element, i:int, param:[float]):
    if(element.name == "Triangle"):
        if i == 0:
            return 1 - param[0] - param[1]
        elif i == 1:
            return param[0]
        elif i ==2 :
            return param[1]

def Integrale(msh:Mesh, dim:int, physical_tag:int, f, B:np.array, order = 2):
    if(dim == 2):
        listElements = msh.getElements(dim,physical_tag)
        for k in range(len(listElements)):
            coeff = listElements[k].jac()
            (w,ksi,eta,x,y) =listElements[k].gaussPoint(order)
            for i in range(3):
                I = msh.Loc2Glob(k,i)
                for m in range(len(w)):
                    B[I] +=  coeff * w[m] * f(x[m],y[m]) * phiRef(listElements[k],i,[ksi[m],eta[m]])

def Dirichlet(msh, dim, physical_tag, g, triplets, B):
    nodes = msh.getPoints(dim,physical_tag)
    for i in range(len(nodes)):
        id = nodes[i].id
        for j in range(len(triplets.data[0])):
            if(triplets.data[1][0][j] == id):
                triplets.data[0][j] = 0
        triplets.append(id,id,1)
        B[id] = g(nodes[i].x,nodes[i].y)

def f(x,y):
 return 0
