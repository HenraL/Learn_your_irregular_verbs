import thorpy, pygame
def my_func_reaction(event):#Reactions functions must take an event as first arg
    print("My reaction displays the pos of event:", event.pos)

#We declare a Reaction. Note that we do not filter the event here.
my_reaction = thorpy.Reaction(reacts_to=pygame.MOUSEBUTTONDOWN,
                              reac_func=my_func_reaction)

application = thorpy.Application(size=(300, 300), caption="Reaction tuto")

background = thorpy.Background(color=(255,255,255))
background.add_reaction(my_reaction) #add my_reaction to background's reactions

menu = thorpy.Menu(background) #create a menu for auto events handling
menu.play() #launch the menu

application.quit()