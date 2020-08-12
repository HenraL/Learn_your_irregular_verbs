import pygame, thorpy
def pause():
    pause=input("Please press enter to continue...")
print ("pause................................[OK]")

application = thorpy.Application(size=(300, 300), caption="Hello world")
w=70
h=35
DE=thorpy.make_button("German")
DE.set_size((w,h))
#thorpy.store(DE, y=1000)

EN=thorpy.make_button("English")
EN.set_size((w,h))

FR=thorpy.make_button("French")
FR.set_size((w,h))

ES=thorpy.make_button("Spanish")
ES.set_size((w,h))
buttons=[DE,EN,FR,ES]
elements=[DE,EN,FR,ES]
background = thorpy.Background(color=(200, 200, 255),elements=[DE,EN,FR,ES])
thorpy.store(background, elements[0], x=380, y=10, margin=0, gap=0, align="right")
thorpy.store(background, elements[1], x=10, y=10, margin=0, gap=0, align="left")
thorpy.store(background, elements[2], x=20, y=200, margin=0, gap=0, align="center")
thorpy.store(background, elements[3], x=30, y=300, margin=0, gap=0, align="top")

#background = thorpy.Background(color=(200, 200, 255),elements=buttons)
#thorpy.store(background, buttons[0], x=380, y=10, align="right")
#thorpy.store(background, buttons[1], x=10, y=10, align="left", gap=0)
#thorpy.store(background, buttons[2], mode="h", y=200)
#thorpy.store(background, buttons[3], mode="h", y=300, align="top")
#my_button = thorpy.make_button("Hello, world!") #just a useless button
#my_button.center() #center the element on the screen
#thorpy.store(DE, y=0, x=10)
menu = thorpy.Menu(background) #create a menu for auto events handling
menu.play() #launch the menu

application.quit()

LanguageChosen="n"
while LanguageChosen!="y":
    print("What language would you like to studdy? [(De)utsch/(En)glish/(Fr)ançais/(Es)paňol]?:")
    # Language="D"
    if Language=="D" or Language=="De" or Language=="DE" or Language=="de":
        Corresponds="German"
        filenames="de"
        LanguageChosen="y"
    elif Language=="E" or Language=="En" or Language=="EN" or Language=="en":
        Corresponds="English"
        filenames="en"
        LanguageChosen="y"
    elif Language=="F" or Language=="Fr" or Language=="FR" or Language=="fr":
        Corresponds="French"
        filenames="fr"
        LanguageChosen="y"
    elif Language=="Es" or Language=="ES" or Language=="es":
        Corresponds="Spanish"
        filenames="es"
        LanguageChosen="y"
    else:
        Corresponds="nothing"
        print("Language not found, please ensure you have entered one of the following letters:\n- De for Deutsch\n- En for English\n- Fr for Français\n- Es for Español\nYou have entered: {}".format(Language))
    print ("Chosen letter: '{}', This letter corresponds to {}.".format(Language,Corresponds))
    pause()
