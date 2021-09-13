from pygame.math import Vector3 as V3
import obstacle
import core3d, parameters

def get_positive(x):
    if x < 0:
        return -x
    return x

def get_negative(x):
    if x > 0:
        return -x
    return x

class Obstacle:

    def __init__(self, damage, x, y, z, obj):
        self.railx, self.raily, self.z = x, y, z
        self.obj = obj
        parameters.scene.objs.append(obj)
        obj.set_pos(parameters.scene.track.rails[x,y].get_middlepos(z))
        parameters.scene.track.obstacles.append(self)
        self.obj.compute_box3D()
        self.box = self.obj.box
        self.living = True
        self.damage = damage
        #
        self.movement_x = 0
        self.movement_y = 0
        self.rotation_x = None
        self.rotation_y = None
        #
        self.W = parameters.RAILW*parameters.scene.track.nx
        self.H = parameters.RAILH*parameters.scene.track.ny

    def refresh(self): #get_rail_from_pos
        if self.rotation_x:
            self.obj.rotate_around_center_x(self.rotation_x)
        elif self.rotation_y:
            self.obj.rotate_around_center_y(self.rotation_y)
        #
        if self.movement_x:
            shift = parameters.scene.cam.from_init
            if self.box.x[0] + shift.x < 0:
                self.movement_x = get_positive(self.movement_x)
            elif self.box.x[1] + shift.x> self.W:
                self.movement_x = get_negative(self.movement_x)
            self.obj.move(V3(self.movement_x,0,0))
        if self.movement_y:
            shift = parameters.scene.cam.from_init
            if self.box.y[0] + shift.y < 0:
                self.movement_y = get_positive(self.movement_y)
            elif self.box.y[1] + shift.y> self.W:
                self.movement_y = get_negative(self.movement_y)
            self.obj.move(V3(0,self.movement_y,0))
