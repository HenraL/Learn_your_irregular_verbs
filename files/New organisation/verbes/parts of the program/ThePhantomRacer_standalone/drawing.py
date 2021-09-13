import pygame.gfxdraw as gfx
import pygame
from pygame.math import Vector3 as V3

colors = [(255,0,0),(255,0,0),
            (0,200,0),(0,200,0),
            (0,0,255),(0,0,255),
            (255,255,0),(255,255,0),
            (255,0,255),(255,0,255),
            (255,255,255),(255,255,255)]
colors = [V3(c) for c in colors]
def colorize(obj):
    for i,t in enumerate(obj.triangles):
        t.color = colors[::2][i%6]

def draw_aa(screen, p, color):
    try:
        gfx.filled_trigon(screen,
                            p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1],
                            color)
    except:
        print("points", p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1])
        print(color)
    gfx.aatrigon(screen,
                    p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1],
                    color)

def draw_normal(screen, p, color):
    gfx.filled_trigon(screen,
                        p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1],
                        color)

def draw_filled_polygon_aa(screen, p, color):
    gfx.filled_polygon(screen, p, color)
    gfx.aapolygon(screen, p, color)

def draw_filled_polygon_normal(screen, p, color):
    gfx.filled_polygon(screen, p, color)

def draw_polygon_aa(screen, p, color):
    gfx.aapolygon(screen, p, color)

def draw_polygon_normal(screen, p, color):
    gfx.polygon(screen, p, color)

def draw_lines_aa(screen, p, color):
    pygame.draw.aalines(screen, color, False, p)

def draw_lines_normal(screen, p, color):
    pygame.draw.lines(screen, color, True, p)