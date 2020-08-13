
#The imports
from tkinter import *
import sys

#Initialising the window
fenetre = Tk()
fenetre['bg']='white'
fenetre.title("Language:")
fenetre.geometry("250x200")
fenetre.minsize(250,200)
#fenetre.iconbitmap("the icone of the software in.ico")
fenetre.config(background="#2CDF85")

#The few frames
#First frame
Frame1=Frame(fenetre, borderwidth=2, relief=F1, bg=FBG)
Frame1.pack(side=LEFT, padx=10, pady=10)

#Frame1=LabelFrame(fenetre, text="Choose You're Language:", padx=10, pady=-10, bg=FBG, fg=FFG)
#Frame1.pack(fill="both",expand="yes")


#Inner Top Frame
Frame1Top=Frame(Frame1, borderwidth=2, relief=F1T, bg=FBG)
Frame1Top.pack(side=TOP, padx=10, pady=10, expand=YES)


#Inner middle frame
Frame1bot=Frame(Frame1,borderwidth=2, relief=F1b, bg=FBG)
Frame1bot.pack(side=BOTTOM, padx=10, pady=10, expand=YES)


#Bottom inner frame
Frame1quit=Frame(Frame1,borderwidth=2, relief=F1q, bg=FBG)
Frame1quit.pack(side=BOTTOM, padx=30, pady=10, expand=YES)

#Label, text (Inform the user of the content of the windows
label = Label(Frame1, text="Choose you're language:", font=(Font,Size), bg=LBG, fg=LFG)
label.pack(side=TOP, pady=10, expand=YES,fill=X)#padx=5)

#Buttons
DE=Button(Frame1, text="German", font=(Font,Size), bg=WBG, fg=WFG, command=languageDE ,activebackground=hbDE, activeforeground=hfDE)#, value="D")
DE.pack(side=RIGHT,pady=0, expand=YES,padx=5)#fill=X)

EN=Button(Frame1,text="English", font=(Font,Size), bg=WBG, fg=WFG, command=languageE ,activebackground=hbEN, activeforeground=hfEN)#, value="E")
EN.pack(side=RIGHT,pady=0, expand=YES,padx=5)#fill=X)

FR=Button(Frame1,text="French", font=(Font,Size), bg=WBG, fg=WFG, command=languageF ,activebackground=hbFR, activeforeground=hfFR)#, value="F")
FR.pack(side=RIGHT,pady=0, expand=YES,padx=5)#fill=X)

ES=Button(Frame1,text="Spanish", font=(Font,Size), bg=WBG, fg=WFG, command=languageES ,activebackground=hbES, activeforeground=hfES)#, value="ES")
ES.pack(side=RIGHT,pady=0, expand=YES,padx=5)#fill=X)

bouton=Button(Frame1quit, text="Quit", font=(Font,Size), bg=WBG, fg=WFG, command=languagequit ,activebackground=hbq, activeforeground=hfq)
bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)
