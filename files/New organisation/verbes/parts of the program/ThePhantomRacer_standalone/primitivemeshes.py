from core3d import ManualObject3D, Object3D, Triangle, Path3D, Area3D
from pygame.math import Vector3 as V3
from light import Material

def rectangle(a,b,color=(0,0,0)):
    t1 = ManualObject3D([Triangle(V3(0,0,0), V3(a,0,0), V3(a,b,0),
                                            color=Material(color)),
                            Triangle(V3(0,0,0), V3(a,b,0), V3(0,b,0),
                                            color=Material(color))])
    t1.move(V3(-a/2,-b/2,0))
    t1.from_init = V3()
    t1.refresh_normals()
    return t1

def triangle(a,color=(0,0,0)):
    t1 = ManualObject3D([Triangle(a*V3(-1,0,0), a*V3(1,0,0), a*V3(0,1,0),
                                            color=Material(color))])
    t1.refresh_normals()
    return t1

def cube(a, color=(0,0,0)):
    cube = Object3D("cube_ascii.stl")
    cube.scale(a)
    cube.refresh_normals()
    cube.set_color(Material(color))
    return cube

#path meshes "P"

class PathBuilder:

    def __init__(self, path):
        self.path = path

    def go(self, x,y,z):
        if len(self.path) == 0:
            self.path = [V3(x,y,z)]
        self.path.append(self.path[-1]+(x,y,z))

def p_triangle(a,filled=True,color=(0,0,0)):
##    a = V3(a,0,0)
##    p1 = a.rotate_z(60)
##    p2 = p1.rotate_z(60)
##    p3 = p1.rotate_z(60)
##    p = Path3D([p1,p2,p3], True, color)
##    p.filled = filled
##    return p
    p = Path3D([V3(-a,0,0), V3(a,0), V3(0,a,0)], True, Material(color))
    p.filled = filled
    return p

def p_disk(a,filled=True,color=(0,0,0),n=10):
    v0 = V3(a,0,0)
    path = [v0.rotate_z(angle) for angle in range(0, 360, 360//n)]
    p = Path3D(path, True, Material(color))
    p.filled = filled
    return p

def p_arrow_line(a, b, c, color=(0,0,0)):
    path = PathBuilder([V3(-a,0,0)])
    path.go(2*a,0,0)
    path.go(0,0,b)
    path.go(c,0,0)
    path.go(-c-a,0,c)#middle
    path.go(-c-a,0,-c)
    path.go(c,0,0)
    path.go(0,0,-b)
    p = Path3D(path.path, True, Material(color))
    p.filled = False
    return p

def p_arrow(a,b,c,color=(0,0,0)):
    rect = p_rectangle(a,b,color)
    triangle = Path3D([V3(2*c,b,0),V3(0,b+3*c,0),V3(-2*c,b,0)],True,
                        Material(color))
    triangle.move(V3(0,-b/2,0))
    triangle.from_init = V3()
    triangle.filled = True
    return rect, triangle

def p_line(frompos, topos, color=(0,0,0)):
    p = Path3D([frompos, topos], False, Material(color))
    p.filled = False
    return p

def p_rectangle(a, b, color=(0,0,0), edges=None, filled=True):
    points = [V3(0,0,0), V3(a,0,0), V3(a,b,0), V3(0,b,0)]
    area = Path3D(points,True,color=Material(color))
    if edges:
        area.edges = V3(edges)
    area.move(V3(-a/2,-b/2,0))
    area.from_init = V3()
    area.filled = filled
    return area



################################################################################

def a_rectangle(a,b,color=(0,0,0),edges=None):
    points = [V3(0,0,0), V3(a,0,0), V3(a,b,0), V3(0,b,0)]
    area = Area3D(points,color=Material(color))
    if edges:
        area.edges = V3(edges)
    area.move(V3(-a/2,-b/2,0))
    area.from_init = V3()
    area.refresh_triangle()
    return area