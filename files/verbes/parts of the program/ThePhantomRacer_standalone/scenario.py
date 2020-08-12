import pygame
import thorpy
import parameters

TCOLOR = (255,0,0)

from thorpy.gamestools.writing import LargeTextManager

t = LargeTextManager()
t.paragraph("He raised me from the dead")
t.paragraph("I did not really want to... However, I cannot say I had no choice. ")
t.more("This would be a lie. Lies led me to death.")
t.paragraph("For decades, I have been living ruthlessly, in the immorality, ")
t.more("the crime and all the possible disrespect for any form of life, including mine.")
t.paragraph("I was about to die when the wizard came and suspended my last breath.")
t.more("He proposed a deal. Considering my actions, I deserved the Great Void ")
t.more("which was waiting for me, he said, altough his considerable power could")
t.more("have saved me ; but he did not want to extend such a miserable life in this world anymore.")
t.more("Nevertheless, he could send me to another world, a world which would better fit my poor")
t.more("morality, a world to which he would not regret to raise me from the dead. ")
t.more("Moreover, he said, if I accepted the deal, then I would be a 'kind of gladiator' performing for his 'company'.")
t.paragraph("The dilemma was the following: either I died in my current state of unfamous,"+\
            " unloved, botched and wicked human, ")
t.more("or I accepted to go and live in this vicious other world, where I would have no freedom...")
INTRO = t.get_all()

t = LargeTextManager()
t.paragraph("He raised me from the dead, and I did regret my choice.")
t.paragraph("This ignominious world was full of creatures more vicious and more disgusting "+\
           "than I even was before. Terrifying machines made of steel and fire were racing everywhere.")
t.paragraph("The kind of gladiator I was supposed to be was very different than what I imagined... "+\
           "The company first employed me as a slave. Then, months after months, I was forced to learn how "+\
           "to drive the flying machines. They organized races. Racing competitions seem to be a religion here. " +\
           "As a counter part, they gave me money, with which I was free to improve my personal race machine.")
t.paragraph("However the most important was the following: each year, freedom was given back to the winner "+\
           "of the Intergalactic Racing League.")
INTRO2 = t.get_all()

def launch_intro_text():
    S = parameters.W
    screen = thorpy.get_screen()
    title_text = "The beginning"
    title = thorpy.make_text(title_text, thorpy.style.TITLE_FONT_SIZE, TCOLOR)

    end_text = "... I accepted the deal as the lesser of two evils."
    end_text = thorpy.pack_text(400,end_text)
    end = thorpy.make_text(end_text, thorpy.style.TITLE_FONT_SIZE, TCOLOR)
    letter = thorpy.make_text(thorpy.pack_text(int(0.7*S),INTRO))
    w = letter.get_fus_rect().w + 10
    boxletter = thorpy.Box.make([letter],(w,S//2))
    boxletter.refresh_lift()
    thorpy.style.BOX_RADIUS += 10
    background = thorpy.load_image("PaulinaRiva.png")
    background = thorpy.get_resized_image(background,
                                                    (parameters.W,parameters.H//2),
                                                    type_=max)
##    background = thorpy.Background.make(image=background)
    thorpy.get_screen().blit(background,(0,0))
    pygame.display.flip()
    box = thorpy.make_ok_box([title,boxletter,end],"Ok")
    box.e_ok.user_func = thorpy.functions.quit_menu_func
    box.e_ok.user_params = {}
    boxletter.set_main_color((200,200,200,50))
    box.set_main_color((200,200,255,100))
    box.center()
    thorpy.style.BOX_RADIUS -= 10
    launch(box)

def launch_intro_text2():
    S = parameters.W
    screen = thorpy.get_screen()
    title_text = "The beginning (2)"
    title = thorpy.make_text(title_text, thorpy.style.TITLE_FONT_SIZE, TCOLOR)
    end_text = "... My only hope now is to become the greatest racer.."
    end_text = thorpy.pack_text(400,end_text)
    end = thorpy.make_text(end_text, thorpy.style.TITLE_FONT_SIZE, TCOLOR)
    letter = thorpy.make_text(thorpy.pack_text(int(0.7*S),INTRO2))
    w = letter.get_fus_rect().w + 10
    boxletter = thorpy.Box.make([letter],(w,S//2))
    boxletter.refresh_lift()
    thorpy.style.BOX_RADIUS += 10
    background = thorpy.load_image("PaulinaRiva.png")
    background = thorpy.get_resized_image(background,
                                                    (parameters.W,parameters.H//2),
                                                    type_=max)
##    background = thorpy.Background.make(image=background)
    thorpy.get_screen().blit(background,(0,0))
    pygame.display.flip()
    box = thorpy.make_ok_box([title,boxletter,end],"Ok")
    box.e_ok.user_func = thorpy.functions.quit_menu_func
    box.e_ok.user_params = {}
    boxletter.set_main_color((200,200,200,50))
    box.set_main_color((200,200,255,100))
    box.center()
    thorpy.style.BOX_RADIUS -= 10
    launch(box)

def launch_end():
    S = parameters.W
    screen = thorpy.get_screen()
    title_text = "The End"
    title = thorpy.make_text(title_text, thorpy.style.TITLE_FONT_SIZE, TCOLOR)
    text = "You are the first of the Intergalatic Ranking."
    end_text = "... You are free now."
    end_text = thorpy.pack_text(400,end_text)
    end = thorpy.make_text(end_text, thorpy.style.TITLE_FONT_SIZE, TCOLOR)
    letter = thorpy.make_text(thorpy.pack_text(int(0.7*S),text))
    w = letter.get_fus_rect().w + 10
    boxletter = thorpy.Box.make([letter],(w,S//2))
    boxletter.refresh_lift()
    thorpy.style.BOX_RADIUS += 10
    background = thorpy.load_image("PaulinaRiva.png")
    background = thorpy.get_resized_image(background,
                                                    (parameters.W,parameters.H//2),
                                                    type_=max)
##    background = thorpy.Background.make(image=background)
    thorpy.get_screen().blit(background,(0,0))
    pygame.display.flip()
    box = thorpy.make_ok_box([title,boxletter,end],"Ok")
    box.e_ok.user_func = thorpy.functions.quit_menu_func
    box.e_ok.user_params = {}
    boxletter.set_main_color((200,200,200,50))
    box.set_main_color((200,200,255,100))
    box.center()
    thorpy.style.BOX_RADIUS -= 10
    launch(box)

def make_instruction(text):
    S = parameters.W
    splits = text.split(":")
    title, corpus = splits[0], "".join(splits[1:])
    corpus = thorpy.pack_text(int(0.4*S), corpus)
    etitle = thorpy.make_text(title, font_color=(255,0,0))
    ecorpus = thorpy.Element.make(corpus)
    return thorpy.make_group([etitle, ecorpus])

def launch_help(func=None):
    S = parameters.W
    title = thorpy.make_text("Instructions", thorpy.style.TITLE_FONT_SIZE,
                                TCOLOR)
    elements = []
    #
    text = "SPACE BAR : Accelerate (this uses fuel)"
    elements.append(make_instruction(text))
    text = "LEFT/RIGHT/UP/DOWN : Change way (turn left/right/up/down)"
    elements.append(make_instruction(text))
    text = "Race: The goal of a race is to reach the finish line as fast as possible.\n"+\
            "If your vessel is destructed or if you cannot reach the finish line, you loose the race."
    elements.append(make_instruction(text))
    text = "Obstacles: Obstacles are on the track. Some of them can move and rotate. Obstacles damage your vessel and slow it down."
    elements.append(make_instruction(text))
    text = "Vessel: A vessel is constituted of a nose, a cockpit, a tail, two wings and one engine.\n"+\
            "These parts determine how fast the vessel can run, how well it turns and how resistant it is to obstacles."
    elements.append(make_instruction(text))
    text = "Life: The current damage state of your vessel in indicated on the top-left of the HUD. "+\
            "The more you damage your vessel, the more you will pay for repairing it."
    elements.append(make_instruction(text))
    text = "Garage: You prepare the next race in your garage. You can buy/sell parts and modify/repair your vessel."
    elements.append(make_instruction(text))
    text = "Ranking: The Intergalactic Ranking works as follow - the winner of each race wins a point and the loser loses one point.\n"+\
            "The Intergalactif League is subdivided in three categories: national, international and intergalactic. "+\
            "Note that the money prize of each race is determined by the category."
    elements.append(make_instruction(text))
    #
    thorpy.style.BOX_RADIUS += 10
    boxletter = thorpy.Box.make(elements,(int(0.75*S),int(0.85*parameters.H)))
    boxletter.refresh_lift()
    box = thorpy.make_ok_box([title,boxletter])
    box.e_ok.user_func = thorpy.functions.quit_menu_func
    box.e_ok.user_params = {}
##    boxletter.set_main_color((200,200,200,50))
    box.set_main_color((200,200,255,100))
    box.center()
    thorpy.style.BOX_RADIUS -= 10
    background = thorpy.load_image("PaulinaRiva.png")
    background = thorpy.get_resized_image(background,
                                                    (parameters.W,parameters.H//2),
                                                    type_=max)
##    background = thorpy.Background.make(image=background)
    thorpy.get_screen().blit(background,(0,0))
    pygame.display.flip()
    launch(box)
    if func:
        func()


def launch(e, func=None):
    if not isinstance(e, thorpy.Ghost):#dirty hack because I'm lazy
        e = e.instructions
    print("launching",e)
    m = thorpy.Menu(e)
    m.play()
    if func:
        func()
