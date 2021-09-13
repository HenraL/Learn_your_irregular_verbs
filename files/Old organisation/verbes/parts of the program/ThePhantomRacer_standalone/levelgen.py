import random

import parameters
import track
import obstacle

class LevelGenerator:

    def __init__(self, zfinish, nx, ny):
        self.zfinish = zfinish
        self.nx = nx
        self.ny = ny
        self.track = track.Track(zfinish,nx,ny)
        parameters.scene.track = self.track

    def add_static_obstacles(self, density, zmin, zmax, objects):
        """Density: average number of obstacles per 100 m"""
        n = density * self.zfinish / 100.
        done = set([])
        i = 0
        while i < n:
            x = random.randint(0,self.nx-1)
            y = random.randint(0,self.ny-1)
            z = random.randint(zmin,zmax)
            if (x,y,z) not in done:
                done.add((x,y,z))
                obj = random.choice(objects).get_copy()
                damage = 1
                obstacle.Obstacle(damage,x,y,z,obj)
                i += 1

    def random_gen(self, nparts, objects, min_density=0.1, max_density=1.8):
        zpart = self.zfinish // nparts
        for i in range(nparts):
            density = random.random()*(max_density-min_density) + min_density
            print("random gen", density)
            if i == 0:
                begin = 50
            else:
                begin = i*zpart
            self.add_static_obstacles(density, begin, (i+1)*zpart, objects)

