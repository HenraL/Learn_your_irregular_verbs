from pygame.math import Vector3 as V3
import math
import random
import parameters
from light import Material


def get_splitted_triangles(triangles, k, threshold):
    new_triangles = []
    for t in triangles:
        splitted = t.split(k,threshold)
        if splitted:
            new_triangles += splitted
        else:
            new_triangles.append(t)
    return new_triangles

def get_stl_lines(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return [line.replace("\n","") for line in lines]

def get_vertex(line):
    if "vertex" in line:
        line = line.split(" ")
        while '' in line:
            line.remove('')
        x, y, z = line[-3],line[-2],line[-1]
        return V3(float(x),float(y),float(z)), "v"
    elif "normal" in line:
        line = line.split(" ")
        while '' in line:
            line.remove('')
        x, y, z = line[-3],line[-2],line[-1]
        return V3(float(x),float(y),float(z)), "n"
    return False

def get_triangles(lines):
    triangles = []
    k = 0
    vertices = [None, None, None]
    normal = None
    for line in lines:
        v = get_vertex(line)
        if v:
            if v[1] == "v":
                vertices[k] = v[0]
                k += 1
            elif v[1] == "n":
                normal = v[0]
        if k == 3:
            t = Triangle(vertices[0],vertices[1],vertices[2])
            t.n = normal
            triangles.append(t)
            assert t.n is not None
            k = 0
    assert k == 0
    return triangles


##def get_hitbox1D_points(points):
##    zlist = [p[2] for p in points]
##    return min(zlist), max(zlist)
##
##class Box1D: #z-limits of the object
##
##    def __init__(self, obj):
##        self.obj = obj
##        if obj is not None:
##            self.zmin, self.zmax = get_hitbox1D_points(obj.get_vertices())
##        else:
##            self.zmin, self.zmax = None, None
##
##    def collide_point(self, z):
##        return self.zmin < z < self.zmax
##
##    def collide_box(self, b):
##        if self.collide_point(b.zmin):
##            return True
##        else:
##            return self.collide_point(b.zmax)
##
##    def move(self, delta):
##        self.zmin += delta
##        self.zmax += delta

def get_hitbox3D_points(points):
    mins = [float("inf")]*3
    maxs = [-float("inf")]*3
    for p in points:
        for i in range(3):
            if p[i] < mins[i]:
                mins[i] = p[i]
            elif p[i] > maxs[i]:
                maxs[i] = p[i]
    if maxs[2] == mins[2]:
        maxs[2] += parameters.MIN_BOX_THICKNESS
    return [mins[0],maxs[0]], [mins[1],maxs[1]], [mins[2],maxs[2]]

class Box3D: #nb: if vessels grossly remains in the same direction, do not need to recompute box

    def __init__(self, obj):
        self.obj = obj
        self.x, self.y, self.z = get_hitbox3D_points(obj.get_vertices())
        self.points = []
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    self.points.append(V3(self.x[i],self.y[j],self.z[k]))

    def move(self, delta):
        self.x[0] += delta[0]
        self.x[1] += delta[0]
        self.y[0] += delta[1]
        self.y[1] += delta[1]
        self.z[0] += delta[2]
        self.z[1] += delta[2]

    def __repr__(self):
        return str(self.x) + str(self.y) + str(self.z)

    def collide(self, other):
        z = self.z[0] <= other.z[1] <= self.z[1]
        if z:
            x1 = self.x[0] <= other.x[0] <= self.x[1]
            x2 = self.x[0] <= other.x[1] <= self.x[1]
            if x1 or x2:
                y1 = self.y[0] <= other.y[0] <= self.y[1]
                y2 = self.y[0] <= other.y[1] <= self.y[1]
                if y1 or y2:
                    return True
        return False



#les triangles font des references a des points, qui eux subissent les transfos!
class Triangle:

    def __init__(self, v1, v2, v3, color=None):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.n = None
        self.c = None
        self.color = color
        if color is None:
##            self.color = V3(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            rand = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            self.color = Material(rand)
        self.neighs = []
        self.pd = None

    def move(self, delta):
        self.v1 += delta
        self.v2 += delta
        self.v3 += delta

    def rotate_x(self, angle):
        self.v1.rotate_x_ip(angle)
        self.v2.rotate_x_ip(angle)
        self.v3.rotate_x_ip(angle)

    def rotate_y(self, angle):
        self.v1.rotate_y_ip(angle)
        self.v2.rotate_y_ip(angle)
        self.v3.rotate_y_ip(angle)

    def rotate_z(self, angle):
        self.v1.rotate_z_ip(angle)
        self.v2.rotate_z_ip(angle)
        self.v3.rotate_z_ip(angle)

    def copy(self):
        t = Triangle(V3(self.v1), V3(self.v2), V3(self.v3), self.color.get_copy())
        t.n = self.n
        t.c = self.c
        t.d = self.pd
        return t

    def get_edges(self):
        e1 = self.v2 - self.v1
        e2 = self.v3 - self.v1
        e3 = self.v3 - self.v2
        return [e1,e2,e3]

    #e1-e2 has v1 in common, e1-e3 has v2 in common, e2-e3 has v3 in common
    def get_common_point(self, i1, i2):
        if (i1==0 and i2==1) or (i1==1 and i2==0):
            return self.v1
        elif (i1==0 and i2==2) or (i1==2 and i2==0):
            return self.v2
        else:
            return self.v3

    def compute_normal(self):
        e1 = self.v2 - self.v1
        e2 = self.v3 - self.v1
##        print(self.v1,self.v2,self.v3)
##        print(e1,e2,e1.cross(e2))
##        e3 = self.p3 - self.p2
        n1 = e1.cross(e2)
##        n2 = e1.cross(e3)
##        n3 = e2.cross(e3)
        #n1,n2,n3 yield the same result
        return n1

    def refresh_normal(self):
        self.n = self.compute_normal().normalize()

    def vertices(self):
        yield self.v1
        yield self.v2
        yield self.v3

##    def refresh_cd(self):
##        self.c = (self.v1 + self.v2 + self.v3)/3.
##        self.d = self.c.length_squared()

    def refresh_cd(self):
        self.c = (self.v1 + self.v2 + self.v3)/3.
        self.d = self.c.length_squared()

    def refresh_center(self):
        self.c = (self.v1 + self.v2 + self.v3)/3.

    def refresh_pd(self):
        self.pd = self.d
        counter = 1
        for buddy in self.neighs:
            a = self.n.angle_to(buddy.n)
            if a == 0:
                counter += 1
                self.pd += buddy.d
        self.pd /= counter

    def split(self, k, threshold):
        e12 = self.v2 - self.v1
        e13 = self.v3 - self.v1
        e23 = self.v3 - self.v2
        l12 = e12.length_squared()
        l13 = e13.length_squared()
        l23 = e23.length_squared()
        if l12>threshold or l13>threshold or l23>threshold:
            if l12 > l13:
                if l13 > l23: #longest are l12 and l13, join on v1
                    p1 = self.v1
                    p2 = self.v1 + k*e12 #-?
                    p3 = self.v1 + k*e13
                    t1 = Triangle(p1, p2, p3, self.color)
                    t2 = Triangle(p3, p2, self.v2, self.color)
                    t3 = Triangle(self.v2, self.v3, p3, self.color)
                else:         #longest are l12 and l23, join on v2
                    p1 = self.v2
                    p2 = self.v2 + k*e23
                    p3 = self.v2 - k*e12
                    t1 = Triangle(p1, p2, p3, self.color)
                    t2 = Triangle(p2, self.v1, p3, self.color)
                    t3 = Triangle(self.v1, p2, self.v3, self.color)
            else:
                if l12 > l23: #longest are l12 and l13, join on v1
                    p1 = self.v1
                    p2 = self.v1 + k*e12 #-?
                    p3 = self.v1 + k*e13
                    t1 = Triangle(p1, p2, p3, self.color)
                    t2 = Triangle(p3, p2, self.v2, self.color)
                    t3 = Triangle(self.v2, self.v3, p3, self.color)
                else:         #longest are l13 and l23, join on v3
                    p1 = self.v3
                    p2 = self.v3 - k*e13
                    p3 = self.v3 - k*e23
                    t1 = Triangle(p1, p2, p3, self.color)
                    t2 = Triangle(p3, p2, self.v1, self.color)
                    t3 = Triangle(self.v1, self.v2, p3, self.color)
            return [t1, t2, t3]


class Path3D:
    obj_id = 0

    def __init__(self, points, closed, color):
        self.points = points #list of vectors
        self.closed = closed
        self.visible = True
        self.from_init = V3()
        self.from_init_rot = V3()
        self.color = color
        self.filled = False
        self.box = None
        self.edges = None
        self.rotations = [self.rotate_around_center_x,
                            self.rotate_around_center_y,
                            self.rotate_around_center_z]
        self.obj_id = Path3D.obj_id
        Path3D.obj_id += 1

    def reset(self):
        self.move(-self.from_init)

    def compute_box3D(self):
        self.box = Box3D(self)

##    def compute_box1D(self):
##        self.box = Box1D(self)

    def move(self, delta):
        for v in self.points:
            v += delta
        self.from_init += delta
        if self.box:
            self.box.move(delta)

    def set_pos(self, pos):
        delta = pos - self.from_init
        self.move(delta)

    def rotate_x(self, angle, refresh=True):
        for v in self.points:
            v.rotate_x_ip(angle)
        self.from_init_rot.x += angle

    def rotate_around_center_x(self, angle, refresh=True):
        tmp = V3(self.from_init)
        self.move(-tmp)
        self.rotate_x(angle, refresh)
        self.move(tmp)

    def rotate_y(self, angle, refresh=True):
        for v in self.points:
            v.rotate_y_ip(angle)
        self.from_init_rot.y += angle

    def rotate_around_center_y(self, angle, refresh=True):
        tmp = V3(self.from_init)
        self.move(-tmp)
        self.rotate_y(angle, refresh)
        self.move(tmp)

    def rotate_z(self, angle, refresh=True):
        for v in self.points:
            v.rotate_z_ip(angle)
        self.from_init_rot.x += angle

    def rotate_around_center_z(self, angle, refresh=True):
        tmp = V3(self.from_init)
        self.move(-tmp)
        self.rotate_z(angle, refresh)
        self.move(tmp)

    def scale(self, factor): #account for this for rotations!
        for v in self.points:
            v *= factor

    def get_copy(self):
        points = [V3(t) for t in self.points]
        cop = Path3D(points, self.closed, self.color.get_copy())
        cop.from_init = V3(self.from_init)
        if self.edges is not None:
            cop.edges = V3(self.edges)
        cop.filled = self.filled
        return cop

    def set_color(self, color):
        self.color = color

    def refresh_and_draw(self, cam, light):
        p = []
        for t in self.points:
            if t.z > 1 and t.z < parameters.VISIBILITY:
                x,y = cam.project(t)
                p.append((int(x),int(y)))
        if self.closed:
            if len(p) > 2:
                if self.filled:
                    cam.draw_filled_polygon(cam.screen, p, self.color.col)
                    if self.edges is not None:
                        cam.draw_polygon(cam.screen, p, self.edges)
                else:
                    cam.draw_polygon(cam.screen, p, self.color.col)

    def get_vertices(self):
        return self.points

    def collide(self, obj):
        return self.box.collide_box(obj.box)

##    def refresh(self):
##        pass

class Area3D(Path3D):

    def __init__(self, points, color):
        assert len(points) > 2
        Path3D.__init__(self, points, True, color)
        self.filled = True
        self.closed = True
        self.triangle = None
        self.refresh_triangle()

    def get_copy(self):
        points = [V3(t) for t in self.points]
        cop = Area3D(points, self.color.get_copy())
        cop.from_init = V3(self.from_init)
        cop.refresh_triangle()
        if self.edges is not None:
            cop.edges = V3(self.edges)
        return cop

    def refresh_and_draw(self, cam, light):
        p = []
        for t in self.points:
            if t.z > 1 and t.z < parameters.VISIBILITY:
                x,y = cam.project(t)
                p.append((int(x),int(y)))
        if len(p) > 2:
            color = light.get_color(self.triangle)
            cam.draw_filled_polygon(cam.screen, p, color)
            if self.edges is not None:
                cam.draw_polygon(cam.screen, p, self.edges)

    def refresh_triangle(self):
        self.triangle = Triangle(self.points[0],self.points[1],self.points[2],
                                    self.color)
        self.triangle.refresh_normal()
        self.triangle.refresh_center()

    def rotate_x(self, angle, refresh=True):
        for v in self.points:
            v.rotate_x_ip(angle)
        if refresh:
            self.refresh_triangle()
        self.from_init_rot.x += angle

    def rotate_around_center_x(self, angle, refresh=True):
        tmp = V3(self.from_init)
        self.move(-tmp)
        self.rotate_x(angle, refresh)
        self.move(tmp)

    def rotate_y(self, angle, refresh=True):
        for v in self.points:
            v.rotate_y_ip(angle)
        if refresh:
            self.refresh_triangle()
        self.from_init_rot.x += angle

    def rotate_around_center_y(self, angle, refresh=True):
        tmp = V3(self.from_init)
        self.move(-tmp)
        self.rotate_y(angle, refresh)
        self.move(tmp)

    def rotate_z(self, angle, refresh=True):
        for v in self.points:
            v.rotate_z_ip(angle)
        if refresh:
            self.refresh_triangle()
        self.from_init_rot.x += angle

    def rotate_around_center_z(self, angle, refresh=True):
        tmp = V3(self.from_init)
        self.move(-tmp)
        self.rotate_z(angle, refresh)
        self.move(tmp)



## #############################################################################
class Object3D(Path3D):

    def __init__(self, filename, more_triangles=None):
        self.filename = filename
        if filename:
            self.lines = get_stl_lines(filename)
            self.triangles = get_triangles(self.lines) #triangles are unique
            self.original_triangles = list(self.triangles)
        else:
            self.triangles = []
            self.original_triangles = []
        if more_triangles:
            self.triangles += more_triangles
        self.from_init = V3()
        self.from_init_rot = V3()
        vset = self.get_vertices_set()
        self.vertices = {val:V3(val) for val in vset} #vertice are duplicate now
        self.compactize() #...and now they are not
        self.visible = True
        self.box = None
        self.color = Material((255,255,255))

    def reset_from_triangles(self,triangles):
        self.triangles = triangles
        vset = self.get_vertices_set()
        self.vertices = {val:V3(val) for val in vset} #vertice are duplicate now
        self.compactize() #...and now they are not

    def get_vertices(self):
        return self.vertices.values()

    def compute_neighbours(self):
        for t1 in self.triangles:
            for t2 in self.triangles:
                if t1 != t2:
                    counter = 0
                    for v in t1.vertices():
                        if v == t2.v1:
                            counter += 1
                        elif v == t2.v2:
                            counter += 1
                        elif v == t2.v3:
                            counter += 1
                    if counter > 1:
                        t1.neighs.append(t2)

    def compactize(self):
        for t in self.triangles:
            t.v1 = self.vertices[tuple(t.v1)]
            t.v2 = self.vertices[tuple(t.v2)]
            t.v3 = self.vertices[tuple(t.v3)]

    def move(self, delta):
        for v in self.vertices.values():
            v += delta
        self.from_init += delta
        if self.box:
            self.box.move(delta)

    def rotate_x(self, angle, refresh=True):
        for v in self.vertices.values():
            v.rotate_x_ip(angle)
        if refresh:
            self.refresh_normals()
        self.from_init_rot.x += angle

    def rotate_around_center_x(self, angle, refresh=True):
        tmp = V3(self.from_init)
        self.move(-tmp)
        self.rotate_x(angle, refresh)
        self.move(tmp)

    def rotate_y(self, angle, refresh=True):
        for v in self.vertices.values():
            v.rotate_y_ip(angle)
        if refresh:
            self.refresh_normals()
        self.from_init_rot.x += angle

    def rotate_around_center_y(self, angle, refresh=True):
        tmp = V3(self.from_init)
        self.move(-tmp)
        self.rotate_y(angle, refresh)
        self.move(tmp)

    def rotate_z(self, angle, refresh=True):
        for v in self.vertices.values():
            v.rotate_z_ip(angle)
        if refresh:
            self.refresh_normals()
        self.from_init_rot.x += angle

    def rotate_around_center_z(self, angle, refresh=True):
        tmp = V3(self.from_init)
        self.move(-tmp)
        self.rotate_z(angle, refresh)
        self.move(tmp)

    def refresh_normals(self):
        for t in self.triangles:
            t.refresh_normal()

    def scale(self, factor, refresh_normals=False): #account for this for rotations!
        for v in self.vertices.values():
            v *= factor
        if refresh_normals:
            self.refresh_normals()

    def scale_x(self, factor, refresh_normals=False):
        for v in self.vertices.values():
            v.x *= factor
        if refresh_normals:
            self.refresh_normals()

    def scale_y(self, factor, refresh_normals=False):
        for v in self.vertices.values():
            v.x *= factor
        if refresh_normals:
            self.refresh_normals()

    def scale_z(self, factor, refresh_normals=False):
        for v in self.vertices.values():
            v.x *= factor
        if refresh_normals:
            self.refresh_normals()

    def refresh(self):
        #version originale
        for t in self.triangles:
            t.refresh_cd()
        for t in self.triangles:
            t.refresh_pd()
        self.triangles.sort(key=lambda x:x.pd, reverse=True)
        #Version GRU
##        for t in self.triangles:
##            t.refresh_center()
##        self.triangles.sort(key=lambda x:x.c.z,reverse=True)

    def get_vertices_set(self):
        vset = set()
        for t in self.triangles:
            for v in[t.v1,t.v2,t.v3]:
                vset.add(tuple(v))
        return vset

    def get_splitted_copy(self, refresh_normals=True, k=0.65, threshold=-0.85):
        """Negative threshold means iterative split until |threshold| is
        obtained for each edge."""
        again = False
        if threshold < 0:
            again = True
            threshold *= -1.
        triangles = get_splitted_triangles(self.triangles, k, threshold)
        if again:
            while True:
                print("     more")
                before = len(triangles)
                triangles = get_splitted_triangles(triangles, k, threshold)
                if before == len(triangles):
                    break
        #
        cop = ManualObject3D(triangles)
        cop.from_init = V3(self.from_init)
        if refresh_normals:
            cop.refresh_normals()
        return cop #! font forget to refresh normals before first display!

    def get_copy(self, refresh_normals=True):
        triangles = [t.copy() for t in self.triangles]
        cop = ManualObject3D(triangles)
        cop.from_init = V3(self.from_init)
        cop.from_init_rot = V3(self.from_init_rot)
        if refresh_normals:
            cop.refresh_normals()
        return cop

    def set_color(self, color):
        for t in self.triangles:
            t.color = color
        self.color = color

    def refresh_and_draw(self, cam, light):
        self.refresh()
        for t in self.triangles:
            if t.c.z > 1 and t.c.z < parameters.VISIBILITY: #c denotes the center coordinate
                p = []
                for v in t.vertices():
                    x,y = cam.project(v)
                    if abs(x) < parameters.W and abs(y) < parameters.H:
                        p.append((int(x),int(y)))
                    else:
                        break
                if len(p) == 3:
##                    print(self.id, self.color, t.color)
                    color = light.get_color(t)
                    cam.draw_object(cam.screen, p, color)

class ManualObject3D(Object3D):

    def __init__(self, triangles):
        self.triangles = triangles
        self.from_init = V3()
        self.from_init_rot = V3()
        vset = self.get_vertices_set()
        self.vertices = {val:V3(val) for val in vset}
        self.compactize()
        self.visible = True
        self.box = None
