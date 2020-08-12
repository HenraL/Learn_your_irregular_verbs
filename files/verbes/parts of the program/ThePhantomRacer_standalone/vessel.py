import math
from pygame.math import Vector3 as V3
import thorpy
import core3d, parameters, ia, destroy


class Move:

    def __init__(self, fighter, type_):
        self.vel = fighter.turn
        self.original_vel = fighter.turn
        self.delta = None
        self.last_pressed = 0
##        if type_ == "h":
##            self.refresh = self.refresh_x
##        elif type_ == "v":
##            self.refresh = self.refresh_y
##        else:
##            raise Exception("Uknown type",type_)


    def move(self, delta, i):
        """Returns True if the vessel can START moving"""
        if i > self.last_pressed + parameters.MOVE_DELTA_I:
            self.delta = delta
            self.last_pressed = i
            self.vel = sign(delta)*self.original_vel
            return True
        return False

    def refresh(self):
        """Return the current velocity"""
        if self.delta is not None:
            if abs(self.delta) < abs(self.vel):
                tmp = self.delta
                self.delta = 0
                return tmp
            else:
                self.delta -= self.vel
                return self.vel
        return 0.


class Dynamics:

    def __init__(self, fighter):
        self.h = Move(fighter, "h")
        self.v = Move(fighter, "v")
        self.velocity = V3()
        self.friction = fighter.friction

    def refresh(self):
        self.velocity.x = self.h.refresh()
        self.velocity.y = self.v.refresh()
        self.velocity.z -= self.friction*self.velocity.z

    def reset(self):
        self.velocity = V3()
        self.h.last_pressed = 0
        self.v.last_pressed = 0


class Part:

    def __init__(self, triangles, turn, friction, mass):
        self.triangles = triangles
        self.turn = turn
        self.friction = friction
        self.mass = mass

class Engine(Part):

    def __init__(self, max_fuel, force):
        Part.__init__(self, [], 1., 1., 1.)
        self.fuel = max_fuel
        self.max_fuel = max_fuel
        self.force = force#parameters.ENGINE_POWER

def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    return 0

def invsign(x):
    if x < 0:
        return 1
    elif x > 0:
        return -1
    return 0

def collision(v1,v2):
    if v1.mass > v2.mass:
        lightest = v2
        heaviest = v1
    else:
        lightest = v1
        heaviest = v2
    #
    vel = lightest.dyn.velocity
    can = lightest.change_rail(invsign(vel.x),invsign(vel.y))
    if not can:
        vel = heaviest.dyn.velocity
        can = heaviest.change_rail(invsign(vel.x),invsign(vel.y))
        if not can:
            #NB : plutot faire un echange de vitesse du plus grand au + petit!
            if vel.z > lightest.dyn.velocity.z: #lightest is overtaken
                tmp = vel.z
                vel.z = lightest.dyn.velocity.z
                lightest.dyn.velocity.z = tmp
            else: #lightest is overtaking
                lightest.dyn.velocity.z = vel.z*parameters.OVERTAKE_SLOWER
        else:
            heaviest.colliding_with = lightest
    else:
        lightest.colliding_with = heaviest#NB: to reset



class Vessel(core3d.Object3D):
    current_id = 0

    def __init__(self, filename, more_triangles=None):
        core3d.Object3D.__init__(self, filename, more_triangles)
        import garage, light
        self.dyn = None
        self.railx = None
        self.raily = None
        self.is_hero = False
        self.colliding_with = None
        #
        self.turn = None
        self.friction = None
        self.mass = None
        self.engine_force = None
        #
        self.nose = None
        self.cockpit = None
        self.tail = None
        self.lwing = None
        self.rwing = None
        self.engine = None
##        self.parts = []
        #
        self.name = "no name"
        #
        self.ia = None
        self.life = None
        self.max_life = None
        self.finished = False
        #
        self.id = Vessel.current_id
        Vessel.current_id += 1
        #
        self.angle_x = 0.
        self.angle_z = 0.
        self.to_move_x = 0
        self.to_move_y = 0

    def reset(self):
        self.dyn.reset()
        self.rotate_around_center_x(-self.angle_x) #new!
        self.rotate_around_center_z(-self.angle_z)
##        self.rotate_around_center_z(-self.from_init_rot[2])
##        self.rotate_around_center_y(-self.from_init_rot[1])
##        self.rotate_around_center_x(-self.from_init_rot[0])
        self.angle_x = 0.
        self.angle_z = 0.
        self.to_move_x = 0
        self.to_move_y = 0
        self.finished = False
        self.colliding_with = None
        self.move(-self.from_init)
##        if parameters.player.vessel is not self:
##            self.life = self.max_life

    def attach_to_player(self, player, reset_color=False):
        if reset_color:
            self.set_color(player.color)
        self.player = player
        player.vessel = self

    def set_ia(self, near, spontaneous):
        self.ia = ia.IA(self, near, spontaneous)

    def change_rail(self, deltax, deltay): #delta changes if not self.hero
        if deltax:
            track = parameters.scene.track
            newx = self.railx + deltax
            if -1 < newx < track.nx:
                dest = track.rails[newx,self.raily].middlepos.x
                delta = dest - parameters.scene.cam.from_init.x - self.from_init.x
                if self.dyn.h.move(delta, parameters.scene.i):
                    self.railx += deltax
                    return True
        if deltay:
            track = parameters.scene.track
            newy = self.raily + deltay
            if -1 < newy < track.ny:
                dest = track.rails[self.railx,newy].middlepos.y
                delta = dest - parameters.scene.cam.from_init.y - self.from_init.y
                if self.dyn.v.move(delta, parameters.scene.i):
                    self.raily += deltay
                    return True
        return False

    def refresh_angle_h(self):
        if self.angle_x == 0:
            if self.dyn.h.delta:
                d = abs(self.dyn.h.delta)
                if self.to_move_x < d:
                    self.to_move_x = d
                value = invsign(self.dyn.velocity.x)*parameters.ANGLE_TURN
                if d <= self.to_move_x//2:
                    value *= -1
                self.rotate_around_center_z(value)
                self.angle_z += value
            else: #reset to 0
                if self.angle_z != 0:
                    self.to_move_x = 0
                    self.rotate_around_center_z(-self.angle_z)
                    self.angle_z = 0

    def refresh_angle_v(self):
        if self.angle_z == 0:
            if self.dyn.v.delta:
                d = abs(self.dyn.v.delta)
                if self.to_move_y < d:
                    self.to_move_y = d
                value = invsign(self.dyn.velocity.y)*parameters.ANGLE_TURN_V
                if d <= self.to_move_y//2:
                    value *= -1
                self.rotate_around_center_x(value)
                self.angle_x += value
            else:
                if self.angle_x != 0:
                    self.to_move_y = 0
                    self.rotate_around_center_x(-self.angle_x)
                    self.angle_x = 0

    def should_collide(self, other):
        if other.id > self.id: #check self != other and forbids double-side collision
            if self.colliding_with is not other: #check that this collision not already currently treated
                if self.box.collide(other.box): #finally check the collision
                    return True
                elif other.box.collide(self.box):
                    return True
                else:
                    self.colliding_with = None
        return False


    def obstacle_collision(self, obstacle):
        obstacle.obj.visible = False
        obstacle.living = False
        self.life -= obstacle.damage
        self.dyn.velocity.z /= 2.
##        parameters.scene.track.obstacles.remove(obstacle)
        #
        parameters.scene.debris.append(destroy.DestroyPath(obstacle.obj, self.dyn.velocity, parameters.N_DEBRIS))
##        if self.is_hero:
##            if self.life <= 0:
##                parameters.scene.debris.append(destroy.DestroyPath(self, self.dyn.velocity, 100))
##                self.visible = False
##                print("DEAD")

    def vessel_collision(self, vessel):
        if random.random() < 0.5:
            vessel.change_rail(2*random.randint(0,1) - 1,
                                2*random.randint(0,1) - 1)
        if self.dyn.velocity.x != 0:
            self.dyn.velocity.x *= -10
        elif self.dyn.velocity.y != 0:
            self.dyn.velocity.y *= -1
        elif self.dyn.velocity.z > vessel.dyn.velocity.z:
            if vessel.is_hero:
                self.move(V3(0,0,-20))
            else:
                vessel.move(V3(0,0,20))
        else:
            if vessel.is_hero:
                self.move(V3(0,0,-20))
            else:
                vessel.move(V3(0,0,20))
        #cam move et enlever l'assymetrie?

    def get_parts(self):
        return [self.nose, self.cockpit, self.tail, self.lwing, self.rwing,
                self.engine]

    def compute_dynamics(self):
        parts = self.get_parts()
        self.turn = sum([p.turn for p in parts]) * parameters.TURN
        self.friction = sum([p.friction for p in parts]) * parameters.FRICTION
        self.mass = sum([p.mass for p in parts]) * parameters.MASS
        self.dyn = Dynamics(self)
        self.engine_force = self.engine.force/self.mass
        self.life = int(self.mass * parameters.LIFE_FACTOR)
        self.max_life = self.life


    def boost(self):
        if self.engine.fuel > 0:
            self.engine.fuel -= 1
            self.dyn.velocity.z += self.engine_force
        else:
            return 0.

    def refresh_mesh(self):
        triangles = []
        for p in self.get_parts():
            triangles += p.triangles
        self.reset_from_triangles(triangles)

    def extract_tnc(self, glass_color):
        tail, nose, cock = [], [], []
        for t in self.triangles:
            x = [p.x for p in t.vertices()]
            if max(x) <= -2.:
                tail.append(t)
            elif min(x) >= 2.:
                nose.append(t)
            else:
                cock.append(t)
        tail = core3d.ManualObject3D(tail)
        nose = core3d.ManualObject3D(nose)
        cock = core3d.ManualObject3D(cock)
        for t in cock.triangles:
            if sum([abs(value)>1e-6 for value in t.compute_normal()]) > 1:
                t.color = glass_color
        return tail, nose, cock