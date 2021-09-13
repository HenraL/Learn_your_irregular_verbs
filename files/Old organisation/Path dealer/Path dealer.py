import os
import glob
import platform
import pygame
import shutil
import German_Words
def attention():
    attsing="\n           ^\n          / \\\n         / _ \\\n        / | | \\\n       /  | |  \\\n      /   | |   \\\n     /    | |    \\\n    /     | |     \\\n   /      |_|      \\\n  /        _        \\\n /        |_|        \\\n/_____________________\\\n"
    return attsing
def pause():
    pause=input("Please press enter to continue...")
LanguageChosen="n"
while LanguageChosen!="y":
    print("What language would you like to studdy? [(De)utsch/(En)glish/(Fr)ançais/(Es)paňol]?:")
    Language="D"
    if Language=="D" or Language=="De" or Language=="DE" or Language=="de":
        Corresponds="German"
        filenames="de"
    elif Language=="E" or Language=="En" or Language=="EN" or Language=="en":
        Corresponds="English"
        filenames="en"
    elif Language=="F" or Language=="Fr" or Language=="FR" or Language=="fr":
        Corresponds="French"
        filenames="fr"
    elif Language=="Es" or Language=="ES" or Language=="es":
        Corresponds="Spanish"
        filenames="es"
    else:
        Corresponds="nothing"
    print ("Chosen letter: '{}', This letter corresponds to {}.".format(Language,Corresponds))
    if Language=="D" or Language=="De" or Language=="DE" or Language=="de":
        try:
            import German_Words.py
        except:
            print("""Please ensure that you have downloaded the file "German_Words.py"\nIf this isn't the case, you can dowload it by following this link: "" """)
        LanguageChosen="y"
    elif Language=="E" or Language=="En" or Language=="EN" or Language=="en":
        try:
            import English_Words.py
        except:
            print("""Please ensure that you have downloaded the file "English_Words.py"\nIf this isn't the case, you can dowload it by following this link: "" """)
    elif Language=="F" or Language=="Fr" or Language=="FR" or Language=="fr":
        try:
            import French_Words.py
        except:
            print("""Please ensure that you have downloaded the file "French_Words.py"\nIf this isn't the case, you can dowload it by following this link: "" """)
    elif Language=="Es"  or Language=="ES" or Language=="es":
        try:
            import Spanish_Words.py
        except:
            print("""Please ensure that you have downloaded the file "Spanish_Words.py"\nIf this isn't the case, you can dowload it by following this link: "" """)
    else:
        print("Language not found, please ensure you have entered one of the following letters:\n- De for Deutsch\n- En for English\n- Fr for Français\n- Es for Español\nYou have entered: {}".format(Language))
        pause()
sound=["Thriller.m4a"]
print ("Mainpath from getcwd: {}".format(os.getcwd()))
mainpath=os.getcwd()
print ("Mainpath variable: {}".format(mainpath))
if platform.system()=="Windows":
    mainpath+="\\"
else:
    mainpath=="/"
print("mainpath: {}".format(mainpath))
A="audio"
fullpath=mainpath+A
if os.path.exists(fullpath)==False:
    try:
        os.makedirs("audio")
        print("Created the folder Audio")
    except:
        print("Failed to create the folder audio to be able to copy the audio files")
else:
    print("Audio Path [OK]")
for a in range(len(sound)):
    if os.path.exists("{}{}".format(fullpath,sound[a])):
        print ("Sound: {}........................[OK]".format(sound[a]))
    else:
        print ("""Fatal Error: The file : "{}" does not exist in the folder Audio.\nTrying to copy from the source folder of the program""".format(sound[a]))
        try:
            filePath = shutil.copy('{}'.format(sound[a]), '{}'.format(fullpath))
            print ("Sound: {}........................[Copied]".format(sound[a]))
        except:
            print ("""{}\nLeathal Error:\nThe file : "{}" does not exist at the source of the program, please run the file {}_Sounds.exe and make sure the installation path is {}.""".format(attention(),sound[a],filenames,fullpath))
            break
pause()

# try:
#     pygame.display.set_icon(pygame.image.load("zerotwo.png"))
# except:
#     print("Please ensure you have downloaded the files")
#     print("I'll shutdown for the moment.\nPlease run the the file {}_Package.exe")
#     print("Pour me rouvrir merci de double clicker sur mon icone")
#     pygame.quit()
#     #sys.exit()
# #window = pygame.display.set_mode((720,720)
# #print ('{}'.format("path: C:\Users\Henry PC\Documents\001 Github prog Sharing\Learn_German_irregular_verbs\files\Path dealer"))
# pygame.init()