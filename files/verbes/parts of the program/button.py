#button1 = thorpy.make_image_button(root+normal, root+pressed, root+hover,
#                                    alpha=255, #opaque
#                                    colorkey=(255,255,255)) #white=transparent

"""Show how to use image to make buttons. Here 2 buttons are created."""

import thorpy, pygame, random

application = thorpy.Application((500,500), "Image buttons")

#root = "../documentation/examples/"
#normal, pressed, hover = "normal.png", "pressed.png", "hover.png"

#button1 = thorpy.make_image_button(root+normal, root+pressed, root+hover,
#                                    alpha=255, #opaque
#                                    colorkey=(255,255,255)) #white=transparent

#this time a very simple button, with a text (only 1 image)
#button2 = thorpy.make_image_button(root+hover, colorkey=False, text="Hello")

#w,h=70,35
DE=thorpy.make_button("German")
#DE.set_size((w,h))
#thorpy.store(DE, y=1000)

EN=thorpy.make_button("English")
#EN.set_size((w,h))

FR=thorpy.make_button("French")
#FR.set_size((w,h))

ES=thorpy.make_button("Spanish")
#ES.set_size((w,h))

button3=thorpy.make_button(text="Hello")#,color=(254,200,250))
elements=[button3,DE,EN,FR,ES]
for e in elements:
    w, h = e.get_rect().size
    w, h = w*(1+random.random()/2.), h*(1+random.random()/2.)
    e.set_size((w,h))

#background = thorpy.Background(image=thorpy.style.EXAMPLE_IMG,elements=[button1, button2])
background=thorpy.Background(color=(200,200,255),elements=elements)
thorpy.store(background, elements[0:4], x=380, y=10, margin=0, gap=0, align="right")
#thorpy.store(background, elements[1:1], x=10, y=10, margin=0, gap=0, align="left")
#thorpy.store(background, elements[2:2], x=20, y=200, margin=0, gap=0, align="center")
#thorpy.store(background, elements[3:3], x=30, y=300, margin=0, gap=0, align="top")
#thorpy.store(background, elements[4:4], x=40, y=300, margin=0, gap=0, align="bottom")


thorpy.store(background)

menu = thorpy.Menu(background)
menu.play()

application.quit()
