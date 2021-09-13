from __future__ import division
import thorpy
import pygame
import parameters
from thorpy import LifeBar

##class LifeBar(thorpy.Element):
##
##    def __init__(self, text, color=(255,165,0), text_color=(0,0,0),
##                    size=(200,30), font_size=None):
##        thorpy.Element.__init__(self)
##        painter = thorpy.painterstyle.ClassicFrame(size,
##                                                    color=thorpy.style.DEF_COLOR,
##                                                    pressed=True)
##        self.set_painter(painter)
##        self.finish()
##        #
##        self.life_text = thorpy.make_text(text,font_color=text_color,font_size=font_size)
##        self.life_text.center(element=self)
##        self.life_color = color
##        self.add_elements([self.life_text])
##        self.life_width = size[0]-2
##        self.life_rect = pygame.Rect(1,1, self.life_width,size[1]-2)
##
##    def set_life_text(self, text):
##        self.life_text.set_text(text)
##        self.life_text.center(element=self)
##
##    def blit(self):
##        """Recursive blit"""
##        self._clip_screen()
##        for e in self._blit_before:
##            e.blit()
##        if self.visible:
##            self.solo_blit()
##            pygame.draw.rect(self.surface, self.life_color, self.life_rect)
##        for e in self._blit_after:
##            e.blit()
##        self._unclip_screen()
##
##    def move(self,shift):
##        thorpy.Element.move(self,shift)
##        self.life_rect.move_ip(shift)
##
##    def set_life(self,life):
##        self.life_rect.width = int(life*self.life_width)


class HUD:

    def __init__(self):
        self.hfull = thorpy.load_image("heart_full.png",(255,255,255))
        self.hempty = thorpy.load_image("heart_empty.png",(255,255,255))
        self.heart_size = self.hfull.get_size()
        self.heart_spacing = self.heart_size[0] + 5
        self.xlife = - self.heart_spacing + 5
        self.ylife = 5
        #
        self.e_speed = thorpy.make_text("0 km/h",
                                        thorpy.style.FONT_SIZE+8, (255,255,0))
        self.e_speed.stick_to("screen","top","top")
        self.e_speed.stick_to("screen","right","right",False)
        self.e_speed.move((-50,5))
        #
        self.e_fuel = LifeBar("Fuel",text_color=(255,0,0),
                                font_size=thorpy.style.FONT_SIZE+8)
        self.e_fuel.stick_to("screen","top","top")
        #
        self.e_pos = thorpy.make_text("Xth position",
                                        thorpy.style.FONT_SIZE+8, (255,255,0))
        self.e_pos.stick_to("screen","bottom","bottom")
        #
        self.screen = thorpy.get_screen()
        self.scene = None
        self.hero = None

    def refresh_attributes(self):
        self.scene = parameters.scene
        self.hero = parameters.scene.hero

    def draw(self):
        x = 0
        for i in range(self.hero.life):
            x += self.heart_spacing
            self.screen.blit(self.hfull,(self.xlife+x,self.ylife))
        for i in range(self.hero.max_life - self.hero.life):
            x += self.heart_spacing
            self.screen.blit(self.hempty,(self.xlife+x,self.ylife))
        vel = int(self.hero.dyn.velocity.z*parameters.SPEED_HUD)
        #
##        if self.e_speed.get_text() != vel:
        self.e_speed.set_text(str(vel)+" km/h")
        #
        hero_pos = self.scene.get_current_ranking().index(self.hero) + 1
        if hero_pos == 1:
            post = "st"
        elif hero_pos == 2:
            post = "nd"
        elif hero_pos == 3:
            post = "rd"
        else:
            post = "th"
        self.e_pos.set_text(str(hero_pos)+post+" position")
        #
        self.e_fuel.set_life(self.hero.engine.fuel/self.hero.engine.max_fuel)
        self.e_speed.blit()
        self.e_fuel.blit()
        self.e_pos.blit()
