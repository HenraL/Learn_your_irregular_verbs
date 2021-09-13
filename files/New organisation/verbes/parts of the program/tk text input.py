from tkinter import*

string="ddddd"
fenetre = Tk()
fenetre['bg']='white'


Frame1=Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=30, pady=30)


value = StringVar() 
value.set("texte par défaut")
entree = Entry(Frame1, textvariable=string, width=30)
entree.pack(side=LEFT,padx=10,pady=10)
bouton=Button(Frame1, text="Valider", command=fenetre.quit)
bouton.pack(side=RIGHT,padx=10,pady=10)

fenetre.mainloop()
