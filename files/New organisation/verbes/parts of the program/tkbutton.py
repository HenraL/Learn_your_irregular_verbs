import thorpy, pygame, random
from tkinter import*

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

label = Label(fenetre, text="Texte par défaut", bg="yellow")
label.pack()


fenetre.mainloop()
