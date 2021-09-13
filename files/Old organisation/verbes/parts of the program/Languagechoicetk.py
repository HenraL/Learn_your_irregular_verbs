from tkinter import *
import sys
#import webbrowser

def pause():
    pause=input("Please press enter to continue...")
print ("pause................................[OK]")
def languageDE():
    Language="D"
    Corresponds="German"
    filenames="de"
    print(Language, Corresponds, filenames)
    return Language, Corresponds, filenames
def languageE():
    Language="E"
    Corresponds="English"
    filenames="en"
    print(Language, Corresponds, filenames)
    return Language, Corresponds, filenames
def languageF():
    Language="F"
    Corresponds="French"
    filenames="fr"
    print(Language, Corresponds, filenames)
    return Language, Corresponds, filenames
def languageES():
    Language="ES"
    Corresponds="Spanish"
    filenames="es"
    print(Language, Corresponds, filenames)
    return Language, Corresponds, filenames

def TlanguageE():
    TLanguage="E"
    chosen_language(Language)
    print(TLanguage, Corresponds, filenames)
    return TLanguage, Corresponds, filenames
def TlanguageF():
    TLanguage="F"
    chosen_language(Language)
    print(TLanguage, Corresponds, filenames)
    return TLanguage, Corresponds, filenames

def languagequit():
    fenetre.destroy()
    print("Goodbye, See you next time")
    aaaa = Tk()
    aaaa['bg']='white'
    aaaa.title("Language:")
    aaaa.geometry("250x200")
    aaaa.minsize(250,200)
    #aaaa.iconbitmap("the icone of the software in.ico")
    aaaa.config(background="#2CDF85")
    label = Label(aaaa, text="Goodbye, see you next time. :-)", font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=10, expand=YES,fill=X)#padx=5)
    bouton=Button(aaaa, text="close", font=(Font,Size), bg=WBG, fg=WFG, command=aaaa.destroy ,activebackground=hbq, activeforeground=hfq)
    bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)


    aaaa.mainloop()
    sys.exit(0)
#Font="Algerian"
Font="Times_New_Roman"
#Font=""

#Size=14
#Size=10
Size=8

WBG="Orange"

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


fenetre = Tk()
fenetre['bg']='white'
fenetre.title("Language:")
fenetre.geometry("250x200")
fenetre.minsize(250,200)
#fenetre.iconbitmap("the icone of the software in.ico")
fenetre.config(background="#2CDF85")

Frame1=Frame(fenetre, borderwidth=2, relief=F1, bg=FBG)
Frame1.pack(side=LEFT, padx=10, pady=10)

#Frame1=LabelFrame(fenetre, text="Choose You're Language:", padx=10, pady=-10, bg=FBG, fg=FFG)
#Frame1.pack(fill="both",expand="yes")

Frame1Top=Frame(Frame1, borderwidth=2, relief=F1T, bg=FBG)
Frame1Top.pack(side=TOP, padx=10, pady=10, expand=YES)

Frame1bot=Frame(Frame1,borderwidth=2, relief=F1b, bg=FBG)
Frame1bot.pack(side=BOTTOM, padx=10, pady=10, expand=YES)

Frame1quit=Frame(Frame1,borderwidth=2, relief=F1q, bg=FBG)
Frame1quit.pack(side=BOTTOM, padx=30, pady=10, expand=YES)

label = Label(Frame1, text="Choose you're language:", font=(Font,Size), bg=LBG, fg=LFG)
label.pack(side=TOP, pady=10, expand=YES,fill=X)#padx=5)

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


fenetre.mainloop()
def pause():
    pause=input("Please press enter to continue...")
print ("pause................................[OK]")

print(Corresponds, filenames)

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
    elif language=="quit":
            print("Goodbye, See you next time")
            sys.exit(0)
    else:
        Corresponds="nothing"
        print("Language not found, please ensure you have entered one of the following letters:\n- De for Deutsch\n- En for English\n- Fr for Français\n- Es for Español\nYou have entered: {}".format(Language))
        print ("Chosen letter: '{}', This letter corresponds to {}.".format(Language,Corresponds))


