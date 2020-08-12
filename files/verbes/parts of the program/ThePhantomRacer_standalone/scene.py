import random
from pygame.math import Vector3 as V3
import pygame.gfxdraw as gfx
import pygame
import thorpy
import parameters, vessel, hud, primitivemeshes, destroy



class Scene:

    def __init__(self):
        self.players = None
        self.light = None
        self.objs = []
        self.hero = None
        self.track = None
        self.opponents = None
        self.cam = None
        self.screen = thorpy.get_screen()
        self.screen_rect = self.screen.get_rect().move((0,parameters.H//2))
        self.i = 0 #frame
        self.vessels = []
        self.background = thorpy.load_image(parameters.BACKGROUNDS[parameters.CURRENT_QUALITY])
        self.background = thorpy.get_resized_image(self.background,
                                                (parameters.W,parameters.H//2),
                                                type_=max)
        self.hud = hud.HUD()
        self.debris = []
##        self.background = pygame.transform.smoothscale(self.background, (parameters.W,parameters.H//2))
        self.start_i = 5
        self.start_delay = 10 + int(random.random()*1000)//40
        self.ranking = []
        self.hero_dead = None
        self.abandon = False


    def refresh_vessels(self):
        self.vessels = self.opponents + [self.hero]

    def refresh_display(self):
        #in replay mode, sort according to length, not z!!!
##        self.objs.sort(key=lambda x:x.from_init.length(), reverse=True)
        self.objs.sort(key=lambda x:x.from_init.z, reverse=True)
        #
##        self.screen.fill((0,0,155))
        self.screen.blit(self.background, (0,0))
        self.screen.fill((0,200,0),self.screen_rect)
        #
        self.track.refresh_and_draw_things(self.cam, self.light)
        for d in self.debris:
            d.refresh()
        for obj in self.objs:
            if obj.visible:
                obj.refresh_and_draw(self.cam, self.light)
        #
        self.hud.draw()
        if self.start_i >= 0:
            self.show_start()
        pygame.display.flip()


    def treat_commands(self): #a unifier (facile) et utiliser dans collisions
        press = pygame.key.get_pressed()
        if press[pygame.K_RIGHT]:
            r=self.hero.change_rail(1,0)
        elif press[pygame.K_LEFT]:
            self.hero.change_rail(-1,0)
        if press[pygame.K_UP]:
            self.hero.change_rail(0,1)
        elif press[pygame.K_DOWN]:
            self.hero.change_rail(0,-1)
        if press[pygame.K_SPACE]:
            self.hero.boost()
        if press[pygame.K_ESCAPE]:
            import gamelogic
            gamelogic.launch_ingame_options()

    def show_start(self):
        spacing = 50
        r = 20
        n = 5 #! must be equal to self.start_i
        w = (n-1)*spacing + 2*r
        x = (parameters.W - w) // 2
        if self.start_i >= 0:
            for i in range(self.start_i):
                x += spacing
                y = 150
                gfx.filled_circle(self.screen,x,y,r,(60,60,60))
                gfx.aacircle(self.screen,x,y,r,(0,0,0))
            for i in range(n - self.start_i):
                x += spacing
                y = 150
                gfx.filled_circle(self.screen,x,y,r,(255,0,0))
                gfx.aacircle(self.screen,x,y,r,(0,0,0))
        else:
            for i in range(n):
                x += spacing
                y = 150
                gfx.filled_circle(self.screen,x,y,r,(60,60,60))
                gfx.aacircle(self.screen,x,y,r,(0,0,0))
        if self.i % self.start_delay == 0:
            self.start_i -= 1



    def func_time(self):
##        self.start_i = -1
        self.i += 1
        if self.start_i < 0:
##            if self.i%10 == 0:
##                print(self.hero)
##                if self.hero.colliding_with:
##                    print(self.hero.colliding_with.id)
##                else:
##                    print("rien")
            self.treat_commands()
            # dynamics
            self.refresh_opponents()
            prev = self.hero.dyn.velocity.z
            self.hero.dyn.refresh()
            a = prev - self.hero.dyn.velocity.z
            self.move_hero(self.hero.dyn.velocity)
            parameters.HERO_POS.z = parameters.ORIGINAL_HERO_POS.z + a*70.
            self.hero.refresh_angle_h()
            self.hero.refresh_angle_v()
            # collisions
            for o in self.track.obstacles:
                o.refresh()
            self.obstacles_collisions()
            self.vessel_collisions()
            finisher = self.check_finish()
            if self.abandon:
                thorpy.launch_blocking_alert("You abandoned.","")
                thorpy.functions.quit_menu_func()
            if finisher:
                print("FINISHING:",finisher.player.name, finisher)
                finisher.finished = True
                self.ranking.append(finisher)
                if len(self.ranking) == 3:
                    print("YOU LOOSE")
                    thorpy.launch_blocking_alert("You are the last of this race.","")
                    thorpy.functions.quit_menu_func()
                elif finisher is self.hero:
                    print("YOU WIN")
                    thorpy.functions.quit_menu_func()
            if self.hero.dyn.velocity.z < 0.1 and self.hero.engine.fuel <= 0:
                self.hero.box.z[0] = -1000
                thorpy.launch_blocking_alert("You have no fuel... Use the competition prize to buy fuel","")
                thorpy.functions.quit_menu_func()
            if self.hero.life <= 0:
                if not self.hero_dead:
                    self.hero_dead = self.i
                    self.debris.append(destroy.DestroyPath(self.hero, self.hero.dyn.velocity, 200))
                    self.hero.visible = False
                elif self.i - self.hero_dead > 30:
                    self.hero.box.z[0] = -1000
                    thorpy.launch_blocking_alert("You completely destroyed your vessel.",None)
                    thorpy.functions.quit_menu_func()
            # display
            self.hide_useless_obstacles()
        self.refresh_display()
##        for o in self.cam.objs + [o.obj for o in self.track.obstacles]:
##            if o.obj_id == 430: #329 ??
##                print(o, o.__class__, o.player.name)
##                assert False

    def refresh_opponents(self):
        for o in self.opponents:
            #handle opponents ia here
##            ia.play(o)
            o.ia.make_choice()
            o.boost() #goes into ia
            o.dyn.refresh()
            o.move(o.dyn.velocity)
            o.refresh_angle_h()
            o.refresh_angle_v()

    def refresh_cam(self):
        self.cam.objs = self.objs + self.track.get_all_objs()

    def move_hero(self, delta):
        self.cam.move(delta)
        self.hero.set_pos(parameters.HERO_POS)

    def set_hero_pos(self, pos):
        delta = pos - self.hero.from_init
        self.move_hero(delta)

    def put_hero_on_rail(self, railx, raily, z=0):
        pos = self.track.rails[railx,raily].get_middlepos(z)
        print("put hero", pos)
        self.set_hero_pos(pos)
        self.hero.railx = railx
        self.hero.raily = raily

    def put_opponent_on_rail(self, opponent, railx, raily, z=0):
        pos = self.track.rails[railx,raily].middlepos
        pos = self.relative_to_cam(pos)
        pos.z = z
        print("put opponent", railx, raily, pos)
        opponent.set_pos(pos)
        opponent.railx = railx
        opponent.raily = raily

    def relative_to_cam(self, pos):
        return pos - self.cam.from_init

    def check_finish(self):
        zfinish = self.track.zfinish - self.cam.from_init.z
        for o in self.vessels:
            if not o.finished:
                if o.box.z[1] > zfinish:
                    return o

    def obstacles_collisions(self):
        for v in self.opponents+[self.hero]:
            for o in self.track.obstacles:
                if o.living:
                    if o.box.collide(v.box):
                        print(self.i,"collision",v)
                        v.obstacle_collision(o)

    def vessel_collisions(self): #opti semiboucle
        for o in self.vessels:
            for o2 in self.vessels:
                if o.should_collide(o2):
                    vessel.collision(o,o2)

    def hide_useless_obstacles(self):
        for o in self.track.obstacles:
            if o.living:
                if o.box.z[0] <= self.hero.box.z[1]:
                    o.obj.visible = False

    def get_current_ranking(self):
        return sorted(self.vessels, key=lambda x:x.box.z[0], reverse=True)

    def get_current_ranking_players(self):
        return [v.player for v in self.get_current_ranking()]


    def get_obj_by_id(self,id_):
        for o in self.cam.objs + self.track.obstacles:
            if o.obj_id == id_:
                return o
