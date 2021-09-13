#The imports
from tkinter import *
import sys

#variables
#Font="Algerian"
Font="Times_New_Roman"
#Font=""

#Size=14
#Size=10
Size=8

FBG="White"
LBG="grey"
WFG="black"
FFG="blue"
LFG="white"
F1=FLAT
F1T=GROOVE
F1b=GROOVE
F1q=FLAT

hfDE="blue"
hbDE="green"
hfEN="blue"
hbEN="green"
hfFR="blue"
hbFR="green"
hfES="blue"
hbES="green"
hfq="blue"
hbq="green"
##2CDF85
#Initialising the window
fenetre = Tk()
fenetre['bg']='white'
fenetre.title("Language:")
fenetre.geometry("600x200")
fenetre.minsize(600,200)
#fenetre.iconbitmap("the icone of the software in.ico")
fenetre.config(background="#00b8bb")

def alert():
    showinfo("alerte", "Bravo!")

def WD():
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
def DW():
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
def WT():
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
def TW():
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
def WTD():
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
def WDT():
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
def TWD():
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
def TDW():
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
def DTW():
	print("hi")
def DWT():
	print("hi")
def V():
	print("hi")
def OST():
	print("hi")
def OAT():
	print("hi")
def ET():
	print("hi")
def FT():
	print("hi")
def WCLT():
	print("hi")
def EVE():
	print("hi")
def Author():
	print("hi")
def Watermarks():
	print("hi")
def Score():
	print("hi")
def TS():
	print("hi")
def COS():
	print("hi")
def HELPERS():
	print("hi")
def HT():
	print("hi")
def HID():
	print("hi")
def AS():
	print("hi")
def Ss():
	print("hi")
def FS():
	print("hi")
def AV():
	print("hi")
def SV():
	print("hi")
def FV():
	print("hi")
def TS():
	print("hi")

menubar = Menu(fenetre)

menu0 = Menu(menubar, tearoff=0)
menu0.add_separator()
menu0.add_command(label="Back to Main Menu", command=fenetre.quit)
menubar.add_cascade(label="Files", menu=menu0)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Words then the definition", command=WD)
menu1.add_command(label="Definition then the words", command=DW)
menubar.add_cascade(label="Words and definitions", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Words then their tenses", command=WT)
menu2.add_command(label="Tenses then the words", command=TW)
menubar.add_cascade(label="Words and tenses", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Words, tenses then definition", command=WTD)
menu3.add_command(label="Words, definition then tenses", command=WDT)
menu3.add_command(label="Tenses, words then definiton", command=TWD)
menu3.add_command(label="Tenses, definition then words", command=TDW)
menu3.add_command(label="Definition, tenses then words", command=DTW)
menu3.add_command(label="Definition, words then tenses", command=DWT)
menubar.add_cascade(label="Words, Tenses & definition", menu=menu3)


menu4 = Menu(menubar, tearoff=0)
menu4.add_command(label="Verbs", command=V)
#menu4.add_command(label="Tenses", command=alert)
submenu4 = Menu(menu4, tearoff=0)
submenu4.add_command(label="Of a specific tense", command=OST)
submenu4.add_command(label="Of all the tenses", command=OAT)
menu4.add_cascade(label="Tenses", menu=submenu4)
menu4.add_command(label="English translation", command=ET)
menu4.add_command(label="French translation", command=FT)
menu4.add_command(label="The words and the chosen language for the translation", command=WCLT)
menu4.add_command(label="Everything", command=EVE)
menubar.add_cascade(label="Overview", menu=menu4)

menu5 = Menu(menubar, tearoff=0)
menu5.add_command(label="The author", command=Author)
#menu5.add_command(label="...", command=alert)
submenu5 = Menu(menu5, tearoff=0)
submenu5.add_command(label="My Watermarks", command=Watermarks)
submenu5.add_command(label="You're score", command=Score)
submenu5.add_command(label="Time spent", command=TS)
submenu5.add_command(label="Current OS", command=COS)
submenu5.add_command(label="Helpers", command=HELPERS)
menu5.add_cascade(label="...", menu=submenu5)
menu5.add_command(label="How to", command=HT)
menu5.add_separator()
menu5.add_command(label="Hidden", command=HID)
menu5.add_separator()
sub1menu5 = Menu(menu5, tearoff=0)
sub1menu5.add_command(label="All the sounds", command=AS)
sub1menu5.add_command(label="Specific sound", command=Ss)
sub1menu5.add_command(label="Where to find the sounds", command=FS)
sub1menu5.add_separator()
sub1menu5.add_command(label="All the videos", command=AV)
sub1menu5.add_command(label="Specific video", command=SV)
sub1menu5.add_command(label="Where to find the videos", command=FV)
sub1menu5.add_separator()
sub1menu5.add_command(label="...", command=TS)
menu5.add_cascade(label="Sound", menu=sub1menu5)
menubar.add_cascade(label="About", menu=menu5)

fenetre.config(menu=menubar)

fenetre.mainloop()
