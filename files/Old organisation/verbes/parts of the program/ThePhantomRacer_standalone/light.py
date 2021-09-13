from pygame.math import Vector3 as V3
def interp_lin(f,m,M):
    return f*M + (1.-f)*m

def interp_quad(f,m,M):
    ff = f*f
    return (3.*ff - 2.*ff*f)*(M-m) + m

class Light:

    def __init__(self, pos, m, M):
        self.pos = pos
        self.m = m
        self.M = M
        self.interp_func = interp_quad

    def set_interpolation(mode):
        if "quad" in mode:
            self.interp_func = interp_quad
        elif "line" in mode:
            self.interp_func = interp_lin
        else:
            raise Exception("Unknown interpolation mode")

    def interp(self,f,m,M):
        return self.interp_func(f,m,M)

    def get_color_factor(self, t):
        line = t.c - self.pos
        angle = t.n.angle_to(line)
        return angle/180.


##    def set_light(self, c, f):
##        """Modify color c to reflect light exposition f."""
##        if f > 0.5:
##            f = (f-0.5)/0.5
##            return self.interp(f,c,self.M)
##        else:
##            f = f/0.5
##            return self.interp(f,self.m,c)

    def set_light(self, mat, f): #opti: m et M sont stockes dans chaque objet/triangle...
        """Modify color c to reflect light exposition f."""
        if f > 0.5:
            f = (f-0.5)/0.5
            return self.interp(f,mat.col,mat.M)
        else:
            f = f/0.5
            return self.interp(f,mat.m,mat.col)

    def get_color(self, t):
        f = self.get_color_factor(t)
        return self.set_light(t.color,f)

def control_color(c):
    if c[0] > 255:
        c[0] = 255
    if c[1] > 255:
        c[1] = 255
    if c[2] > 255:
        c[2] = 255
    return c

hundred = V3(100,100,100)

class Material:

    def __init__(self, color, m=None, M=None):
        if isinstance(color, Material):
            m = color.m
            M = color.M
            color = color.col
        self.col = V3(color)
        self.m = m
        if self.m is None:
            self.m = self.col * 0.2
        self.M = M
        if self.M is None:
            self.M = control_color(self.col * 1.1 + hundred)

    def get_copy(self):
        return Material(V3(self.col), V3(self.m), V3(self.M))
##        return self

    def __repr__(self):
        return "MATERIAL: "+str(self.col) + "  " + str(self.m) + "  " + str(self.M)