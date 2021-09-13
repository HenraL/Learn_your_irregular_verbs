from pygame.math import Vector3 as V3
import thorpy
import primitivemeshes
from core3d import Path3D, Object3D, ManualObject3D, Area3D
import parameters
from light import Material

def nothing():
    pass

def get_type(thing):
    if isinstance(thing, Object3D) or isinstance(thing, ManualObject3D):
        return "o"
    elif isinstance(thing, Area3D):
        raise Exception("Not implemented yet")
    elif isinstance(thing, Path3D):
        return "p"
    else:
        raise Exception("Unknown type")

class Rail:

    def __init__(self, track, x, y):
        self.track = track
        self.x = x
        self.y = y
        self.obstacles = []
        self.pos = V3(x*track.railw, y*track.railh, 0)
        self.middlepos = self.pos + V3(self.track.railw//2,self.track.railh//2,0)

    def get_pos(self,z):
        pos = V3(self.pos)
        pos.z = z
        return pos

    def get_middlepos(self,z):
        pos = V3(self.middlepos)
        pos.z = z
        return pos


class ThingManager:

    def __init__(self, n, maxn, spacing):
        self.n = n
        self.maxn = maxn
        self.spacing = spacing
        self.spacing_move = V3(0,0,maxn*spacing)
        self.counter = 0

    def increment(self):
        self.counter += 1

    def get_remaining(self):
        return self.n - self.counter

    def should_continue(self):
        remaining = self.n - self.counter
        return remaining > self.maxn

class Track: #store end

    def __init__(self, zfinish, nx=3, ny=1):
        self.things_objects = []
        self.things_paths = []
        self.obstacles = []
        #
        railw, railh = parameters.RAILW, parameters.RAILH
        self.x1 = 0
        self.x2 = railw*nx
        self.y1 = 0
        self.y2 = railh*ny
        #
        self.nx, self.ny = nx, ny
        self.zfinish = zfinish
        self.railw, self.railh = railw, railh
        self.rails = thorpy.gamestools.basegrid.BaseGrid(nx,ny)
        for x,y in self.rails:
            self.rails[x,y] = Rail(self,x,y)
        self.functions_things = nothing

    def add_visual_rails(self,color=(0,0,0)):
        for x in range(self.nx+1):
            xrail = x*self.railw
            for y in range(self.ny+1):
                yrail = y*self.railh
                p1 = parameters.scene.relative_to_cam(V3(xrail,yrail,0))
                p2 = parameters.scene.relative_to_cam(V3(xrail,yrail,
                                                    parameters.VISURAIL_LENGTH))
                path = Path3D([p1,p2],False,Material(color))
##                path = Path3D([V3(xrail,yrail,0),V3(xrail,yrail,30)],False,color)
                self.add_thing(path,0,self.zfinish,parameters.VISURAIL_SPACE,
                                    parameters.VISURAIL_NMAX)


    def add_thing(self, thing, frompos, topos, spacing, maxn=None):
        n = (topos-frompos)//spacing
        if maxn is None:
            maxn = n
        manager = ThingManager(n, maxn, spacing)
        type_ = get_type(thing)
        actual_number_drawn = min(n,maxn)
        copies = []
        for i in range(actual_number_drawn):
            cpy = thing.get_copy()
            cpy.move(V3(0,0,frompos+i*spacing))
            cpy.manager = manager
            if type_ == "p":
                self.things_paths.append(cpy)
            else:
                self.things_objects.append(cpy)
            copies.append(cpy)
        return copies

    def add_thing_on_rail(self, x, y, thing, frompos, topos, spacing, maxn=None):
        thing.set_pos(parameters.scene.relative_to_cam(self.rails[x,y].get_pos(0)))
        self.add_thing(thing, frompos, topos, spacing, maxn)

    def get_all_objs(self):
        return self.things_objects + self.things_paths


    def refresh_and_draw_things(self, cam, light):
        self.functions_things()
        #things never overlap, and can never appear in front of an object
        for thing in self.things_objects:
            if thing.visible:
                print(thing.obj_id, thing.__class__)
                thing.refresh()
                for t in thing.triangles:
                    if t.c.z > 0 and t.c.z < parameters.VISIBILITY: #c denotes the center coordinate
                        p = []
                        for v in t.vertices():
                            x,y = cam.project(v)
                            p.append((int(x),int(y)))
                            color = light.get_color(t)
                        cam.draw_object(cam.screen, p, color)
                    elif thing.manager.should_continue():
                        thing.move(thing.manager.spacing_move)
                        thing.manager.increment()
        for thing in self.things_paths:
            if thing.visible:
                p = []
                for t in thing.points:
                    if t.z > 0 and t.z < parameters.VISIBILITY:
                        x,y = cam.project(t)
                        p.append((int(x),int(y)))
                        if thing.closed:
                            if len(p) == len(thing.points):
                                if thing.filled:
                                    cam.draw_filled_polygon(cam.screen, p, thing.color.col)
                                    if thing.edges is not None:
                                        cam.draw_polygon(cam.screen, p, thing.edges)
                                else:
                                    cam.draw_polygon(cam.screen, p, thing.color.col)
                        else:
                            if len(p) == len(thing.points):
                                cam.draw_path(cam.screen, p, thing.color.col)
                    elif thing.manager.should_continue():
                        thing.move(thing.manager.spacing_move)
                        thing.manager.increment()

    def rail_centers(self):
        for rail in self.rails.itercells():
            yield V3(rail.middlepos)

##    def monitor(self):
##        monitor.show("abc")
##
##
##import time
##class Monitor:
##
##    def append(self, name):
##        if not hasattr(self, name):
##            setattr(self, name, [time.clock()])
##        else:
##            getattr(self,name).append(time.clock())
##
##    def show(self, letters):
##        tot = [0.]*len(letters)
##        L = len(getattr(self,letters[0]))
##        for i in range(1,len(letters)):
##            for k in range(L):
##                diff = getattr(self,letters[i])[k] - getattr(self,letters[i-1])[k]
##                tot[i] += diff
##        for i in range(1,len(tot)):
##            print(letters[i-1]+"->"+letters[i]+": "+str(tot[i]))
##
##monitor = Monitor()