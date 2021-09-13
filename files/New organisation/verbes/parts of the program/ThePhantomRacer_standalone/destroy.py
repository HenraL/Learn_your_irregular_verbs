from pygame.math import Vector3 as V3
import parameters, random, primitivemeshes


def get_debris(obj):
    a,b = parameters.DEBRIS_SIZE
    d = primitivemeshes.a_rectangle(a,b,obj.color,(0,0,0))
    d.move(obj.from_init)
    return d


class Physics:

    def __init__(self, vel):
        self.vel = V3(vel) + V3([random.randint(-2,2) for i in range(3)])
        self.rot = random.randint(4,8)

class DestroyPath: #doesnt work with Path3D

##    def __init__(self, obj):
##        self.obj = obj
##        if len(self.obj.triangles) < parameters.N_DESTROY:
##            while len(self.obj.triangles):
##                self.obj = self.obj.get_splitted_copy(refresh_normals=False,
##                                                        threshold=0.5)
##            self.obj.refresh_normals()
##        for t in self.obj.triangles:
##            setattr(t, "physics", physics.Physics())

    def __init__(self, obj, vel, n):
        debris = get_debris(obj)
        size = (obj.box.x[1]-obj.box.x[0])//2
        self.debris = [debris.get_copy() for i in range(n)]
        self.rotations = [random.randint(0,2) for i in range(n)]
        for t in self.debris:
            t.physics = Physics(vel)
            t.move(V3([random.randint(-size,size) for i in range(3)]))
        self.cam = parameters.scene.cam
        self.light = parameters.scene.light
        self.i = 0


    def refresh(self):
        if self.i > parameters.DEBRIS_ITER:
            parameters.scene.debris.remove(self)
        for i,d in enumerate(self.debris):
            vel = d.physics.vel
            d.move(vel-parameters.scene.hero.dyn.velocity)
##            vel -= 0.1*vel
            vel *= 0.9
            d.rotations[self.rotations[i]](d.physics.rot)
            d.refresh_and_draw(self.cam, self.light)
        self.i += 1
