import parameters, random

class IA:

    def __init__(self, vessel, near, spontaneous):
        self.track = parameters.scene.track
        self.vessel = vessel
        self.near = near
        self.spontaneous = spontaneous

    def go_to_random_rail(self):
        newx = 2*random.randint(0,1) - 1
        newy = 2*random.randint(0,1) - 1
        self.vessel.change_rail(newx,newy)

    def make_choice(self):
        if random.random() < self.spontaneous:
            self.go_to_random_rail()
            return
        for o in self.track.obstacles:
            if o.living:
                if o.railx == self.vessel.railx and o.raily == self.vessel.raily:
                    dist = o.box.z[0] - self.vessel.box.z[0]
                    if dist < self.near and dist > 0:
                        self.go_to_random_rail()
                        return

