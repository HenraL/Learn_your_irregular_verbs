from pygame.math import Vector3 as V3
import drawing, parameters

class Camera:

    def __init__(self, screen, fov, d, objs):
        self.screen = screen
        self.w = screen.get_width()/2.
        self.h = screen.get_height()/2.
        self.fov = fov
        self.d = d
        self.objs = objs
        #
        self.aa = parameters.AA
        self.set_aa(True)
        self.draw_object = None
        self.draw_filled_polygon = None
        self.draw_polygon = None
        self.draw_path = None
        #
        self.from_init = V3()
        self.set_aa(True)

    def set_aa(self, aa):
        self.aa = aa
        if self.aa:
            self.draw_object = drawing.draw_aa
            self.draw_filled_polygon = drawing.draw_filled_polygon_aa
##            self.draw_polygon = drawing.draw_polygon_aa #bug...
            self.draw_polygon = drawing.draw_polygon_normal
##            self.draw_path = drawing.draw_lines_aa #too thick
            self.draw_path = drawing.draw_lines_normal
        else:
            self.draw_object = drawing.draw_normal
            self.draw_filled_polygon = drawing.draw_filled_polygon_normal
            self.draw_polygon = drawing.draw_polygon_normal
            self.draw_path = drawing.draw_lines_normal

    def project(self, v): #perspective projection
        denom = self.d + v.z
        if denom < 1:
            denom = 1
        factor = self.fov / denom
        x = v.x * factor + self.w
        y = -v.y * factor + self.h
        return x, y

    def move(self, delta):
        delta = V3(delta)
        self.from_init += delta
        delta *= -1.
        for o in self.objs:
            o.move(delta)

    def set_pos(self, pos):
        delta = pos - self.from_init
        self.move(delta)

    def rotate(self, axis, angle): #a optimiser
        angle *= -1.
        func = "rotate_"+axis
        for o in self.objs:
            getattr(o,func)(angle)