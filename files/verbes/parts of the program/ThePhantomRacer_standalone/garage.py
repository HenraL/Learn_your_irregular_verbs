from __future__ import print_function
import random
import pygame
from pygame.math import Vector3 as V3
import thorpy
import core3d, parameters, camera, light, primitivemeshes
from light import Material

#f(M) = 1.
#f(m) = 0.

MAX_POWER = parameters.MAX_POWER*parameters.ENGINE_POWER
MIN_POWER = parameters.MIN_POWER*parameters.ENGINE_POWER

def get_vessel_element(v):
    red = (255,50,50)
    green = (50,255,50)
    f = round(v.engine.force * 10000 * 1.5)
    c = round(v.engine.max_fuel/100.)
    t = round(v.turn * 100)
    d = round(v.friction * 100,2)
    m = round(v.mass * 4000)
    e_engine = thorpy.SkillBar.make("Power: "+str(f)+" kW",MIN_POWER,MAX_POWER,
                                    green, size=(150,30))
    e_engine.set_life(v.engine.force)
##    e_engine = thorpy.make_text("Power: "+str(f)+" kW")
    e_turn = thorpy.SkillBar.make("Agility: "+str(t), parameters.MIN_TURN,
                                    parameters.MAX_TURN, green, size=(150,30))
    e_turn.set_life(v.turn/parameters.TURN/5.) #!!
##    e_turn = thorpy.make_text("Agility: "+str(t))
    e_consumption = thorpy.SkillBar.make("Max fuel: "+str(c)+" L",
                            parameters.MIN_FUEL, parameters.MAX_FUEL, green,
                            size=(150,30))
    e_consumption.set_life(v.engine.max_fuel)
##    e_consumption = thorpy.make_text("Consumption: "+str(c)+" kW/L")
    e_friction = thorpy.SkillBar.make("Friction: "+str(d), 0., 1., red, size=(150,30))
    e_friction.set_life(v.friction/parameters.FRICTION/5.)
##    e_friction = thorpy.make_text("Friction: "+str(d))
    e_mass = thorpy.SkillBar.make("Mass: "+str(m)+" kg", parameters.MIN_MASS,
                                        parameters.MAX_MASS, red, size=(150,30))
    e_mass.set_life(v.mass/parameters.MASS/5.)
##    e_mass = thorpy.make_text("Mass: "+str(m)+" kg")
    box = thorpy.Box.make([e_engine,e_turn,e_consumption,e_friction,e_mass])
    thorpy.store(box,align="right",x=box.get_fus_rect().right-3,y=10)
    box.fit_children()
    return box

def get_random_element():
    parts = {"tail":["agility","friction","mass"],
             "nose":["agility","friction","mass"],
             "cockpit":["agility","friction","mass"],
             "wings":["agility","friction","mass"],
             "engine":["power","max_fuel"]}
    bfactor = {"agility":1.,"friction":-1.,"mass":-1.,"power":1.,"max_fuel":1.}
    print("Choices", list(parts.keys()))
    part = random.choice(list(parts.keys()))
##    part_arg = part[0].lower() + part[1:]
##    part_arg = getattr(parameters.player.vessel, part_arg)
    MAX_BONUS = 0.3
    bonus = [-MAX_BONUS + random.random()*2.*MAX_BONUS for skill in parts[part]]
    for i,skill in enumerate(parts[part]):
        bonus[i] *= bfactor[skill]
    text = ""
    skills = [part]
    price = sum(bonus)
    for i,b in enumerate(bonus):
        increase = "Lower "
        skill = parts[part][i]
        skills.append((skill,b))
        if b > 0:
            increase = "Increase "
        else:
            b *= -1.
        text += increase + "your overall " + skill.replace("_"," ") + " by " + \
                str(round(b*100)) + " %.\n\n"
    ok_text = "buy"
    cost = "cost: "
    if price < 0:
        text += "You can earn money by exchanging your current " + part + " against this less performant one."
        ok_text = "exchange"
        cost = "gain: "
    text = thorpy.pack_text(300,text)
    price_int = int(price*parameters.PRICE)
    price = " ("+cost+str(abs(price_int)) + " $)"
    box = thorpy.make_textbox("New "+part+":",text,ok_text=ok_text+price)
    print("hu0",box)
    if "gain" in cost:
        box.e_ok.set_main_color((0,255,0))
    else:
        box.e_ok.set_main_color((255,0,0))
    return box, skills, price_int


def color_glasses(model, glass_color):
    tail, nose, cock = [], [], []
    for t in model.original_triangles:
        x = [p.x for p in t.vertices()]
        if max(x) <= -2.:
            tail.append(t)
        elif min(x) >= 2.:
            nose.append(t)
        else:
            cock.append(t)
##    tail = core3d.ManualObject3D(tail)
##    nose = core3d.ManualObject3D(nose)
##    cock = core3d.ManualObject3D(cock)
    for t in cock:
        if sum([abs(value)>1e-6 for value in t.compute_normal()]) > 1:
            t.color = glass_color


def cut_object(filename, color, glass_color):
   model = core3d.Object3D(filename)
   model.set_color(color)
   model.rotate_around_center_x(-90)
   model.from_init_rot = V3()
   tail, nose, cock = [], [], []
   for t in model.triangles:
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
   return [tail, nose, cock]

def buy_part(parent):
    background = thorpy.load_image("background_garage.jpg")
    background = thorpy.get_resized_image(background,
                                                    (parameters.W,parameters.H),
                                                    type_=max)
    thorpy.get_screen().blit(background,(0,0))
    pygame.display.flip()
    title = thorpy.make_text("Vessel merchant", thorpy.style.TITLE_FONT_SIZE+4, (255,0,0))
    hbar = thorpy.Line.make(200, "h")
    intro = "Hello, "+str(parameters.player.name)+"."+\
                                    "\nHere is what I have to sell today:"
    intro = thorpy.make_text(intro, thorpy.style.TITLE_FONT_SIZE, thorpy.style.TITLE_FONT_COLOR)
    #
    money = thorpy.Element(thorpy.pack_text(200,"Your money: "+str(parameters.player.money)+" $."))
    money.set_painter(thorpy.functions.obtain_valid_painter(thorpy.painterstyle.DEF_PAINTER,
                                                 pressed=True))
    money.finish()
    money.scale_to_title()
    #
    info = thorpy.Element(thorpy.pack_text(200,"Remember that any part you buy will replace your current one."))
    info.set_painter(thorpy.functions.obtain_valid_painter(thorpy.painterstyle.DEF_PAINTER,
                                                 pressed=True))
    info.finish()
    info.scale_to_title()
    money_info = thorpy.Ghost.make([info, money])
    thorpy.store(money_info, mode="h")
    money_info.fit_children()
    #
    part1, skills1, price1 = get_random_element()
    part2, skills2, price2 = get_random_element()
    choices = thorpy.Ghost.make(elements=[part1,part2])
    thorpy.store(choices, mode="h")
    choices.fit_children()
    cancel = thorpy.make_button("No, thanks", thorpy.functions.quit_menu_func)
    #
    def buy(part, cost):
        if cost > parameters.player.money:
            thorpy.launch_blocking_alert("Not enough money",
            "You don't have enough money to buy this part.",transp=False)
            box.unblit_and_reblit()
        else:
            parameters.player.money -= cost
            name = part.pop(0)
            if name == "wings":
                parts = [getattr(parameters.player.vessel, "lwing"),
                         getattr(parameters.player.vessel, "rwing")]
            else:
                parts = [getattr(parameters.player.vessel, name)]
            for part_obj in parts:
                for skillname, factor in part:
                    if skillname == "agility": skillname = "turn"
                    elif skillname == "power":
                        parameters.player.vessel.engine_force *= (1.+factor)
                    elif skillname == "max_fuel":
                        parameters.player.vessel.engine.max_fuel *= (1.+factor)
                    elif skillname == "mass":
                        parameters.player.vessel.engine_force *= parameters.player.vessel.mass
                        parameters.player.vessel.mass *= (1.+factor)
                        parameters.player.vessel.engine_force /= parameters.player.vessel.mass
                        parameters.player.vessel.max_life = int(parameters.player.vessel.mass * parameters.LIFE_FACTOR)
                    else:
                        current_value = getattr(parameters.player.vessel, skillname)
                        new_value = current_value + factor*current_value/6.
                        setattr(parameters.player.vessel, skillname, new_value)
            thorpy.functions.quit_menu_func()
    part1.e_ok.user_func = buy
    part1.e_ok.user_params = {"part":skills1, "cost":price1}
    part2.e_ok.user_func = buy
    part2.e_ok.user_params = {"part":skills2, "cost":price2}
    #
    box = thorpy.Box.make([title,hbar,intro,money_info,choices,cancel])
    box.center()
    thorpy.launch_blocking(box)
##    thorpy.launch_blocking_choices(text, choices, parent,
##                    thorpy.style.TITLE_FONT_SIZE+2, thorpy.style.TITLE_FONT_COLOR)


def generate_vessel(color, glass_color):
    t = random.choice(parameters.MODELS)+".stl"
    n = random.choice(parameters.MODELS)+".stl"
    c = random.choice(parameters.MODELS)+".stl"
    print(t,n,c)
    #
    to =  cut_object(t,color,glass_color)[0]
    no =  cut_object(n,color,glass_color)[1]
    co =  cut_object(c,color,glass_color)[2]
    return to, no, co

def generate_part(color, glass_color):
    if random.random() < 0.75:
        mesh = random.choice(parameters.MODELS)+".stl"
        part_number = random.randint(0,2)
        part = cut_object(mesh, color, glass_color)[part_number]
        obj = core3d.ManualObject3D(part.triangles)
    else:
        w = garage.wings_free(1.3,1.5,0.2,-0.5,1.,rest,5.,y=0.)



def wings_rect(a,b,color,x=0.,y=0.,angle=0.):
    w = primitivemeshes.rectangle(a,b,color)
    w.rotate_around_center_x(-90)
    w.from_init_rot = V3()
    w2 = w.get_copy()
##    w.move(V3(0,-a,0)) #biplan
##    w2.move(V3(0,a,0))
    w.move(V3(x,y,-b/2-1)) #monoplan
    w.rotate_around_center_x(angle)
    w2.move(V3(x,y,b/2+1))
    w2.rotate_around_center_x(-angle)
    w.from_init = V3()
    w2.from_init = V3()
##    w = w.get_splitted_copy()
    return w,w2

def wings_free(a,b,c,d,fleche,color,angle=0.,y=0,sym=True):
    assert d < 0
    assert a > 0
    p1 = V3()
    p2 = p1 + V3(0,0,a)
    p3 = p2 + V3(b,0,-fleche)
    p4 = p3 + V3(c,0,d)
##    if p4.z > p2.z:
##        print("correction")
##        p4.z = p2.z-0.2
##    mesh = core3d.Area3D([p1,p2,p3,p4],color)
    if sym:
        t1 = core3d.Triangle(p1,p2,p3)
        t2 = core3d.Triangle(p1,p3,p4)
    else:
        t1 = core3d.Triangle(p3,p2,p1)
        t2 = core3d.Triangle(p4,p3,p1)
    mesh = core3d.ManualObject3D([t1,t2])
    mesh.refresh_normals()
    mesh.refresh()
    mesh.rotate_around_center_y(90)
    delta = -1
    if not sym: delta*=-1
    mesh.move(V3(-1,y,delta))
    mesh.from_init = V3()
    mesh.rotate_around_center_x(angle)
    mesh.from_init_rot = V3()
    mesh.set_color(color)
    #
    if sym:
        return mesh, wings_free(a,-b,-c,d,fleche,color,-angle,y,False)
    else:
        return mesh

def rand(a,b):
    return a + random.random()*(b-a)

def random_wing(color):
    a = rand(0.5,2.) #semi corde
    b = 1.8 #envergure
    c = rand(-0.3,0.3) #pointe
    d = rand(-0.5,-0.3) #autre semi corde
    fleche = rand(0.,2.)
    angle = rand(-8.,8.)
    y = 0.2
    return wings_free(a,b,c,d,fleche,color,angle,y)

##import vessel
# def build_all_parts():
#    parameters.canonic_vessels = {}
#    color = Material((200,200,200))
#    glass = Material((0,0,0))
#    files = ["Aerocrush","BangDynamics"]
#    for f in files:
#        parts = wings_free(1.3,3.,0.2,-0.5,1.,color,10.,y=0.)
#        triangles = []
#        for p in parts:
#            triangles += p.triangles
#        parameters.canonic_vessels[f] = vessel.Vessel(f+".stl",triangles)

def get_rankings_box():
    elements = []
    import gamelogic
    gamelogic.refresh_ranking()
    t1 = "    ---- "
    t2 = " ----    "
    fs = thorpy.style.FONT_SIZE - 2
    for i,p in enumerate(parameters.players):
        if i == 0:
            elements.append(thorpy.make_text(t1+parameters.CATEGORIES[0]+t2,fs,(0,155,0)))
        elif i == parameters.NPLAYERS//3:
            elements.append(thorpy.make_text(t1+parameters.CATEGORIES[1]+t2,fs,(0,155,0)))
        elif i == 2*parameters.NPLAYERS//3:
            elements.append(thorpy.make_text(t1+parameters.CATEGORIES[2]+t2,fs,(0,155,0)))
        if p == parameters.player:
            elements.append(thorpy.make_text("("+str(p.points)+")  "+p.name,fs,(255,0,0)))
        else:
            elements.append(thorpy.make_text("("+str(p.points)+")  "+p.name,fs,(0,0,0)))
    box = thorpy.Box.make(elements,size=(300,300))
    box.refresh_lift()
    return box

def launch_rankings(garage):
    box = get_rankings_box()
##    box2 = thorpy.make_ok_box([box])
    box2 = thorpy.make_textbox("Rankings","",elements=[box])
##    box.set_size((300,300))
##    box.refresh_lift()
##    thorpy.launch(box2)
    box2.center()
##    thorpy.launch_blocking(box2,garage.e_bckgr)
    thorpy.launch_nonblocking(box2,launching=garage.e_bckgr)

def quit_game():
    thorpy.functions.quit_func()


class Garage:

    def __init__(self):
##        if not parameters.canonic_vessels:
##            get_all_parts()
        self.vessel = parameters.player.vessel.get_copy()
        self.ovessel = parameters.player.vessel
        self.screen = thorpy.get_screen()
        #
        light_pos = V3(0,1000,-1000)
        light_m = V3(20,20,20)
        light_M = V3(200,200,200)
        self.light = light.Light(light_pos, light_m, light_M)
        #
        self.e_bckgr = thorpy.Background.make((255,255,255))
        self.vessel.set_pos(parameters.GARAGE_POS)
        reaction =  thorpy.ConstantReaction(thorpy.THORPY_EVENT,
                                            self.refresh_display,
                                            {"id":thorpy.constants.EVENT_TIME})
        self.e_bckgr.add_reaction(reaction)
        reaction = thorpy.Reaction(pygame.MOUSEMOTION, self.mousemotion)
        self.e_bckgr.add_reaction(reaction)
        #
        self.viewport = pygame.Surface((400,400))
        self.viewport_color = (200,200,200)
        self.viewport_rect = pygame.Rect((0,0),self.viewport.get_size())
        self.viewport_rect.right = parameters.W - 20
        self.viewport_rect.centery = parameters.H//2
        self.cam = camera.Camera(self.viewport, fov=512, d=2, objs=[])
        #
        #
        #
        self.e_ok = thorpy.make_button("Go to next race", func=thorpy.functions.quit_menu_func)
        self.e_ok.set_main_color((0,255,0))
        self.e_ok.set_font_size(thorpy.style.FONT_SIZE+3)
        self.e_ok.scale_to_title()
        #
        #
        def refresh_repair():
            damages = str(round(100.*(1. - self.ovessel.life/self.ovessel.max_life)))
            self.e_damage.set_text("Vessel damages: " + damages + "%")
            self.e_money.set_text("Money: "+str(parameters.player.money)+" $")
        def choice_repair():
            cost = (self.ovessel.max_life - self.ovessel.life)*300
            if cost <= parameters.player.money:
                if thorpy.launch_binary_choice("Are you sure? This will cost "+\
                                                str(cost)+"$"):
                    self.ovessel.life = self.ovessel.max_life
                    parameters.player.money -= cost
                    refresh_repair()
            elif thorpy.launch_binary_choice("Repairing costs "+str(cost)+\
                                            " $. You don't have enough money.\n"+\
                                            "Do you want to use all your money for"+\
                                            " repairing as much as possible?"):
                    #(after_repair - self.ovessel.life)*300 = money
                    #==> after_repair = money/300 + self.ovessel.life
                    repaired = int(parameters.player.money/300. + self.ovessel.life)
                    parameters.player.money -= (repaired - self.ovessel.life)*300
                    self.ovessel.life = repaired
                    refresh_repair()
            self.e_bckgr.blit()
            self.refresh_display()
            pygame.display.flip()
        self.e_repair = thorpy.make_button("Repair vessel",choice_repair)
        #
        damages = str(round(100.*(1. - self.ovessel.life/self.ovessel.max_life)))
        self.e_damage = thorpy.make_text("Vessel damages: " + damages + "%")
        self.e_ranking = thorpy.make_button("See rankings", launch_rankings, {"garage":self})
##        self.e_ranking = get_rankings_box()
        def quit_forever():
            if thorpy.launch_binary_choice("Are you sure ?"):
                thorpy.functions.quit_func()
            else:
                self.e_bckgr.unblit_and_reblit()
        self.e_menu = thorpy.make_button("Stop career and die (forever)",
                                        func=quit_forever)
        self.e_menu.set_main_color((255,0,0))
        self.e_menu.set_font_size(thorpy.style.FONT_SIZE-2)
        self.e_menu.scale_to_title()
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
        import hud
        fuel = str(round(100*self.ovessel.engine.fuel/self.ovessel.engine.max_fuel))
        self.e_fuel = hud.LifeBar("Fuel: "+fuel+" %",text_color=(255,0,0),size=(100,30))
        self.e_fuel.set_life(self.ovessel.engine.fuel/self.ovessel.engine.max_fuel)
        def refresh_refuel():
            life = self.ovessel.engine.fuel / self.ovessel.engine.max_fuel
            self.e_fuel.set_life(life)
            self.e_fuel.set_text("Fuel: "+str(round(life*100))+" %")
            self.e_money.set_text("Money: "+str(parameters.player.money)+" $")
        def choice_refuel():
            cost = (self.ovessel.engine.max_fuel - self.ovessel.engine.fuel)//2
            if cost <= parameters.player.money:
                if thorpy.launch_binary_choice("Are you sure? This will cost "+\
                                                str(cost)+"$"):
                    self.ovessel.engine.fuel = self.ovessel.engine.max_fuel
                    parameters.player.money -= cost
                    refresh_refuel()
##                    self.e_fuel.set_life(1.)
##                    self.e_fuel.set_life_text("Fuel: 100 %")
##                    parameters.player.money -= cost
##                    self.e_money.set_text("Money: "+str(parameters.player.money)+" $")
##                    self.ovessel.engine.fuel = self.ovessel.engine.max_fuel
            elif thorpy.launch_binary_choice("Refueling costs "+str(cost)+" $. You don't have enough money.\n"+\
                                        "Do you want to spend all your money to refuel as much as possible?"):
                #cost = (newfuel - fuel)//2 ==> 2*cost + fuel = newfuel
                self.ovessel.engine.fuel += 2*parameters.player.money
                parameters.player.money = 0
                refresh_refuel()
##                thorpy.launch_blocking_alert("Refueling costs "+str(cost)+" $. You don't have enough money.")
            self.e_bckgr.blit()
            self.refresh_display()
            pygame.display.flip()
        self.e_refuel = thorpy.make_button("Refuel",choice_refuel)
        self.e_money = thorpy.make_text("Money: "+str(parameters.player.money)+" $",
                                        thorpy.style.TITLE_FONT_SIZE,(255,0,0))
        self.e_money.stick_to("screen","top","top")
        self.e_money.move((0,30))
        #
        self.e_box = thorpy.Box.make([self.e_damage,self.e_repair,
                                    thorpy.Line.make(100,"h"),self.e_fuel,
                                    self.e_refuel,
                                    thorpy.Line.make(100,"h"),
                                    self.e_ranking,self.e_ok])
        self.e_bckgr.add_elements([self.e_box,self.e_menu])
        thorpy.store(self.e_bckgr, x = 200)
        self.e_skills = get_vessel_element(parameters.player.vessel)
        self.e_bckgr.add_elements([self.e_viewport_frame,self.e_money,
                                    self.e_skills])
        self.e_menu.move((0,30))
        self.e_skills.stick_to(self.e_viewport_frame, "left", "right")
        self.i = 0



    def derotate(self):
        pass
##        self.vessel.rotate_around_center_y(-self.i)
##        self.i = 0

    def refresh_display(self):
        self.vessel.rotate_around_center_y(1)
        self.viewport.fill(self.viewport_color)
        self.vessel.refresh_and_draw(self.cam, self.light)
        self.screen.blit(self.viewport,self.viewport_rect)
        pygame.display.update(self.viewport_rect)
##        pygame.display.flip()

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
                self.vessel.rotate_around_center_x(rotate_x)
                self.vessel.rotate_around_center_y(rotate_y)
                self.vessel.rotate_around_center_z(rotate_z)
        else:
            thorpy.change_cursor(thorpy.constants.CURSOR_NORMAL)
##            self.refresh_parts()

    def play(self):
        m = thorpy.Menu(self.e_bckgr)
        m.play()




##class Garage:
##
##    def __init__(self):
####        if not parameters.canonic_vessels:
####            get_all_parts()
##        self.vessel = parameters.player.vessel
##        self.screen = thorpy.get_screen()
##        #
##        light_pos = V3(0,1000,-1000)
##        light_m = V3(20,20,20)
##        light_M = V3(200,200,200)
##        self.light = light.Light(light_pos, light_m, light_M)
##        #
##        self.e_bckgr = thorpy.Background.make((255,255,255))
##        self.t, self.n, self.c = cut_object("BangDynamics.stl",
##                                            Material((0,0,255)),
##                                            Material((0,0,0)))
##        self.w = wings_rect(1.5,2.5,self.t.triangles[0].color,
##                            y=0.5,
##                            angle=10.)
##        self.w = wings_free(1.3,3.,0.2,-0.5,1.,self.t.triangles[0].color, 10., y=0.)
##        self.parts = [self.t, self.n, self.c, self.w[0], self.w[1]]
##        self.triangles = []
##        for p in self.parts:
##            self.triangles += p.triangles
##        for p in self.parts:
##            p.move(parameters.GARAGE_POS)
##        reaction =  thorpy.ConstantReaction(thorpy.THORPY_EVENT,
##                                            self.refresh_display,
##                                            {"id":thorpy.constants.EVENT_TIME})
##        self.e_bckgr.add_reaction(reaction)
##        reaction = thorpy.Reaction(pygame.MOUSEMOTION, self.mousemotion)
##        self.e_bckgr.add_reaction(reaction)
##        #
##        self.viewport = pygame.Surface((400,400))
##        self.viewport_color = (200,200,200)
##        self.viewport_rect = pygame.Rect((0,0),self.viewport.get_size())
##        self.viewport_rect.right = parameters.W - 20
##        self.viewport_rect.centery = parameters.H//2
##        self.cam = camera.Camera(self.viewport, fov=512, d=2, objs=[])
##        #
##        #
##        #
##        self.e_ok = thorpy.make_button("Done", func=thorpy.functions.quit_menu_func)
##        #
####        names = [thorpy.make_button(name) for name in parameters.player.parts]
####        self.e_names = thorpy.Box.make(names)
####        self.e_names.stick_to(self.viewport_rect,"left","right")
####        self.e_sell = thorpy.make_button("Sell vessel")
####        self.e_buy = thorpy.make_button("Buy vessel")
##        def choice_repair():
##            cost = self.vessel.max_life - self.vessel.life
##            if cost <= parameters.player.money:
##                if thorpy.launch_binary_choice("Are you sure? This will cost "+\
##                                                str(cost)+"$"):
##                    print("repair")
##                else:
##                    print("don't repair")
##            else:
##                thorpy.launch_alert("Repairing costs "+str(cost)+"$. You don't have enough money.")
##            self.e_bckgr.blit()
##            self.refresh_display()
##            pygame.display.flip()
##        self.e_repair = thorpy.make_button("Repair vessel",choice_repair)
##        #
##        vw,vh = self.viewport_rect.size
##        self.e_viewport_frame = thorpy.Element()
##        painter = thorpy.painterstyle.ClassicFrame((vw+3,vh+3),
##                                                    color=self.viewport_color,
##                                                    pressed=True)
##        self.e_viewport_frame.set_painter(painter)
##        self.e_viewport_frame.finish()
##        self.e_viewport_frame.set_center(self.viewport_rect.center)
##        #
##        self.e_bckgr.add_elements([self.e_ok,self.e_repair,self.e_viewport_frame])
##        thorpy.store(self.e_bckgr, [self.e_ok,self.e_repair], x = 100)
##
##
##    def refresh_parts(self):
##        self.parts = [self.t, self.n, self.c, self.w[0], self.w[1]]
##        self.triangles = []
##        for p in self.parts:
##            self.triangles += p.triangles
##
##    def refresh_display(self):
##        for p in self.parts:
##            p.rotate_around_center_y(1)
##        self.viewport.fill(self.viewport_color)
####        self.screen.fill((255,255,255))
####            p.refresh_and_draw(self.cam, self.light)
##        for t in self.triangles:
##            t.refresh_cd()
##        for t in self.triangles:
##            t.refresh_pd()
##        self.triangles.sort(key=lambda x:x.pd, reverse=True)
##        for t in self.triangles:
##            if t.c.z > 1 and t.c.z < parameters.VISIBILITY: #c denotes the center coordinate
##                p = []
##                for v in t.vertices():
##                    x,y = self.cam.project(v)
##                    if abs(x) < parameters.W and abs(y) < parameters.H:
##                        p.append((int(x),int(y)))
##                    else:
##                        break
##                if len(p) == 3:
##                    color = self.light.get_color(t)
##                    self.cam.draw_object(self.viewport, p, color)
##        self.screen.blit(self.viewport,self.viewport_rect)
##        pygame.display.update(self.viewport_rect)
####        pygame.display.flip()
##
##    def mousemotion(self,e):
##        if pygame.mouse.get_pressed()[0]:
##            dcx = e.pos[0] - self.viewport_rect.centerx#parameters.W//2
##            dcy = e.pos[1] - self.viewport_rect.centery#parameters.H//2
##            dist = dcx*dcx + dcy*dcy
##            k = -1.
##            #a*rotate_z + (1-a)*rotate_x = k*rel.y
##            #rotate_y = k*rel.x
##            #dist grand : a grand
##            a = dist / float(parameters.W//2)**2
##            rotate_z = a * k * e.rel[1]
##            rotate_x = (1.-a) * k * e.rel[1]
##            rotate_y = k * e.rel[0]
##            for p in self.parts:
##                p.rotate_around_center_x(rotate_x)
##                p.rotate_around_center_y(rotate_y)
##                p.rotate_around_center_z(rotate_z)
##            self.refresh_parts()
##
##    def play(self):
##        m = thorpy.Menu(self.e_bckgr)
##        m.play()
