import random
import pygame
from pygame.math import Vector3 as V3
import thorpy
import parameters, drawing, light, camera
import alphabet, scenario
from garage import get_vessel_element


wordgen1 = alphabet.Dictionnary("thorn.txt","thorn_precisions.txt")
namel = 3
nameL = 8

def get_etitle(name,rect="screen"):
    e = thorpy.make_text(name,thorpy.style.FONT_SIZE+8,(255,255,0))
    e.stick_to(rect,"top","top")
    e.move((0,20))
    return e

def get_eok(name, rect="screen"):
    e = thorpy.make_button(name,thorpy.functions.quit_menu_func)
    e.stick_to(rect,"bottom","bottom")
    e.move((0,-20))
    return e

def refresh_ranking():
    parameters.players.sort(key=lambda x:x.points, reverse=True)
    for i,p in enumerate(parameters.players):
        p.ranking = i+1


def get_display_options():
    varset = thorpy.VarSet()
    varset.add("aa", True, "Anti-aliasing: ")
    varset.add("visibility", parameters.VISIBILITY, "Max display distance: ", [200,3000])
    e = thorpy.ParamSetterLauncher.make([varset], "Display options", "Display options")
    return e, varset

def launch_ingame_options():
    thorpy.set_theme("classic")
    def func():
        parameters.scene.refresh_display()
        box.blit()
        pygame.display.flip()
    e, varset = get_display_options()
    e2 = thorpy.make_button("Show help",scenario.launch_help,{"func":func})
    def leave():
        if thorpy.launch_binary_choice("Are you sure?"):
            parameters.scene.abandon = True
            thorpy.functions.quit_menu_func()
        func()
    q = thorpy.make_button("Abandon",leave)
    box = thorpy.make_ok_box([thorpy.make_text("Pause"),thorpy.Line.make(100,"h"), e,e2,q])
    box.e_ok.user_func = thorpy.functions.quit_menu_func
    box.e_ok.user_params = {}
##    boxletter.set_main_color((200,200,200,50))
    box.set_main_color((200,200,255,200))
    box.center()
    scenario.launch(box)
    parameters.scene.cam.set_aa(varset.get_value("aa"))
    parameters.VISIBILITY = varset.get_value("visibility")
    thorpy.set_theme(parameters.THEME)


##    varset = thorpy.VarSet()
##    varset.add("name", name, "Name: ")
##    varset.add("type", ["Human","Beginner", "Normal", "Hard"],
##                            "Type: ")
##    color=(0,255,0) if name=="Player 1" else (0,0,255)
##    varset.add("color", color, "Color: ")
##    e = thorpy.ParamSetterLauncher.make([varset], name, name+" options")
##    return varset, e
##    ps = thorpy.ParamSetterLauncher()
##    e = thorpy.Box()

def get_category(position):
    k = parameters.NPLAYERS // 3
    if position < k:
        return parameters.CATEGORIES[0],3
    elif position < 2*k:
        return parameters.CATEGORIES[1],2
    return parameters.CATEGORIES[2],1

class Player:

    def __init__(self, name=None, color=None, money=1000, ranking=None, points=None):
        self.name = name
        if name is None:
            self.name =  wordgen1.genWord(random.randint(namel,nameL))
        #
        self.color = color
        if color is None:
            self.color = light.Material(random.choice(drawing.colors))
        self.money = money
        self.vessel = None
        self.ranking = ranking
        self.points = points
        if self.points is None:
            self.points = random.randint(0,parameters.NPLAYERS)

    def get_element(self,prename=""):
        fs = thorpy.style.FONT_SIZE
        ename = thorpy.make_text(prename+self.name,fs+4,(255,0,0))
        emoney = thorpy.make_text("Money: "+str(self.money))
        eranking = thorpy.make_text("Intergalactic Ranking: "+str(self.ranking))
        eranking = thorpy.make_text("Intergalactic Points: "+str(self.points))
        box = thorpy.Box.make([ename,emoney,eranking])
        return box

    def get_nearest_players(self):
        refresh_ranking()
        for i,p in enumerate(parameters.players):
            if p is self:
                print(i)
                if i == parameters.NPLAYERS-1:
                    p1 = parameters.players[i-2]
                    p2 = parameters.players[i-1]
                elif i == 0:
                    p1 = parameters.players[1]
                    p2 = parameters.players[2]
                else:
                    p1 = parameters.players[i-1]
                    p2 = parameters.players[i+1]
                assert p1 is not p2
                return p1,p2
        raise Exception("Couldnt find nearest players")


class ShowRanking:

    def __init__(self, title, ok_text, ranking, results=False, choosevessel=False):
        refresh_ranking()
         #
        light_pos = V3(0,1000,-1000)
        light_m = V3(20,20,20)
        light_M = V3(200,200,200)
        self.light = light.Light(light_pos, light_m, light_M)
        self.viewport = pygame.Surface((400,int(parameters.H*0.6)))
        self.viewport_color = (200,200,200)
        self.viewport.fill(self.viewport_color)
        self.viewport_rect = pygame.Rect((0,0),self.viewport.get_size())
        self.viewport_rect.centerx = parameters.W // 2 + 100
        self.viewport_rect.centery = parameters.H//2
        self.cam = camera.Camera(self.viewport, fov=512, d=2, objs=[])
        self.screen = thorpy.get_screen()
        self.displayed_vessel = None
        self.i = 0
        #
        if results:
            ranking[0].points += 1
            ranking[0].money += 300 + (parameters.NPLAYERS-ranking[0].ranking)*100
            ranking[2].points -= 1
            ranking[2].money += 100
            ranking[1].money += 200
            if ranking[2].points < 0: ranking[2].points = 0
        #
        self.trophy = None
        if choosevessel:
            self.e_players = []
            def other_vessel():
                self.vessels[0] = create_vessel(parameters.HERO_COLOR)
                self.vessels[0].set_pos(V3(0,-1*4.5,20))
                self.vessels[0].move(V3(0,4,0))
                self.displayed_vessel = self.vessels[0]
                #replace self.ve
                new_ve = get_vessel_element(self.vessels[0])
                self.e_bckgr.replace_element(self.ve, new_ve)
                thorpy.functions.refresh_current_menu()
                self.ve = new_ve
                self.e_bckgr.unblit_and_reblit()
            b = thorpy.make_button("Generate another vessel", other_vessel)
            c = thorpy.make_button("Done", thorpy.functions.quit_menu_func)
            self.e_players.append(b)
            self.e_players.append(c)
            from main import create_vessel
            self.vessels = [create_vessel(parameters.HERO_COLOR)]
            self.displayed_vessel = self.vessels[0].get_copy()
            self.ve = get_vessel_element(self.vessels[0])
            self.e_players.append(self.ve)
        else:
            if results:
                self.e_players = [p.get_element(str(i+1)+") ") for i,p in enumerate(ranking)]
            else:
                self.e_players = [p.get_element() for i,p in enumerate(ranking)]
            self.vessels = [p.vessel.get_copy() for p in ranking]
            if results:
                import core3d
                from light import Material
                self.trophy = core3d.Object3D("trophy1.stl")
                self.trophy.set_color(Material((255,215,0)))
##                    self.trophy.set_color((255,255,0))
                self.trophy.set_pos(V3(5.,-0*4.5-0.2,15))
                self.trophy.rotate_around_center_z(90.)
                self.trophy.rotate_around_center_x(-65.)
                self.trophy.move(V3(0,4,0))
        self.background = thorpy.load_image("background1.jpg")
        self.background = thorpy.get_resized_image(self.background,
                                                (parameters.W,parameters.H//2),
                                                type_=max)
        self.e_bckgr = thorpy.Background.make(image=self.background,
                                            elements=self.e_players)
        #
        vw,vh = self.viewport_rect.size
        self.e_viewport_frame = thorpy.Element()
        painter = thorpy.painterstyle.ClassicFrame((vw+3,vh+3),
                                                    color=self.viewport_color,
                                                    pressed=True)
        self.e_viewport_frame.set_painter(painter)
        self.e_viewport_frame.finish()
        self.e_viewport_frame.set_center(self.viewport_rect.center)
        #
        reaction =  thorpy.ConstantReaction(thorpy.THORPY_EVENT,
                                            self.refresh_display,
                                            {"id":thorpy.constants.EVENT_TIME})
        self.e_bckgr.add_reaction(reaction)
        if not choosevessel:
            for i,v in enumerate(self.vessels):
                pos = self.e_players[i].get_fus_rect().center
                v.set_pos(V3(0,-i*4.5,20))
                v.move(V3(0,4,0))
        else:
            self.vessels[0].set_pos(V3(0,-1*4.5,20))
            self.vessels[0].move(V3(0,4,0))
            #
            self.displayed_vessel.set_pos(V3(0,-1*4.5,20))
            self.displayed_vessel.move(V3(0,4,0))
        #
        thorpy.store(self.e_bckgr,gap=40)
        for e in self.e_players:
            e.stick_to(self.viewport_rect,"left","right",align=False)
            e.move((-5,0))
        self.e_title = get_etitle(title)
        if not choosevessel:
            self.e_ok = get_eok(ok_text)
            self.e_bckgr.add_elements([self.e_viewport_frame,self.e_title,self.e_ok])
        else:
            self.e_bckgr.add_elements([self.e_viewport_frame,self.e_title])
        self.goback = False
        def return_garage():
            self.derotate()
            self.goback=True
            thorpy.functions.quit_menu_func()
        if not results and not choosevessel:
            self.e_back = thorpy.make_button("Return to garage", return_garage)
            self.e_back.stick_to(self.e_ok, "left", "right")
            self.e_back.move((-20,0))
            self.e_bckgr.add_elements([self.e_back])
        if not results:
            reaction = thorpy.Reaction(pygame.MOUSEMOTION, self.mousemotion)
            self.e_bckgr.add_reaction(reaction)
        m = thorpy.Menu(self.e_bckgr)
        m.play()

    def derotate(self):
        pass
##        for e in self.vessels:
##                e.rotate_around_center_y(-self.i)
##        if self.displayed_vessel:
##            self.displayed_vessel.rotate_around_center_y(-self.i)
##        self.i = 0

    def refresh_display(self):
        self.viewport.fill(self.viewport_color)
        if self.displayed_vessel:
            self.displayed_vessel.rotate_around_center_y(1)
            self.displayed_vessel.refresh_and_draw(self.cam,self.light)
        else:
            for v in self.vessels:
                v.rotate_around_center_y(1)
                v.refresh_and_draw(self.cam,self.light)
            if self.trophy:
                self.trophy.rotate_around_center_y(1)
                self.trophy.refresh_and_draw(self.cam, self.light)
        self.screen.blit(self.viewport,self.viewport_rect)
        pygame.display.update(self.viewport_rect)
        self.i += 1

    def mousemotion(self,e):
        if self.viewport_rect.collidepoint(pygame.mouse.get_pos()):
            thorpy.change_cursor(thorpy.constants.CURSOR_BROKEN)
            if pygame.mouse.get_pressed()[0]:
                dcx = e.pos[0] - self.viewport_rect.centerx#parameters.W//2
                dcy = e.pos[1] - self.viewport_rect.centery#parameters.H//2
                dist = dcx*dcx + dcy*dcy
                k = -1.
                #a*rotate_z + (1-a)*rotate_x = k*rel.y
                #rotate_y = k*rel.x
                #dist grand : a grand
                a = dist / float(parameters.W//2)**2
                rotate_z = a * k * e.rel[1]
                rotate_x = (1.-a) * k * e.rel[1]
                rotate_y = k * e.rel[0]
                if self.displayed_vessel:
                    self.displayed_vessel.rotate_around_center_x(rotate_x)
                    self.displayed_vessel.rotate_around_center_y(rotate_y)
                    self.displayed_vessel.rotate_around_center_z(rotate_z)
        else:
            thorpy.change_cursor(thorpy.constants.CURSOR_NORMAL)
