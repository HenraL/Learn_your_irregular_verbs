# *=================================================================*
# |                        Creating the defs                        |
# *=================================================================*
def attention():
    attsing="\n           ^\n          / \\\n         / _ \\\n        / | | \\\n       /  | |  \\\n      /   | |   \\\n     /    | |    \\\n    /     | |     \\\n   /      |_|      \\\n  /        _        \\\n /        |_|        \\\n/_____________________\\\n"
    return attsing
print ("attention............................[OK]")
def pause():
    pause=input("Please press enter to continue...")
print ("pause................................[OK]")
def installer(a):
    os.system("{}".format(a))
print("installer............................[OK]")
def watermarkf(s):
    print("\ncreated by Henry Letellier\n ._____. \n |.   .| \n |  |  | \n |\___/| \n |_____| ")
    sleep(s)
print("watermarkf...........................[OK]")
def watermarkat(s):
    print("*=============================================================================================================*\n|      @@@@@@@@   @@@@@@   @@@@@@@@        @@      @@@@@@@@  @@@@@@@@  @@@@@@@@      @@@@@@@@  @@       @@    |\n|      @@        @      @  @@             @  @        @@     @@        @@      @     @@      @  @@     @@     |\n|      @@        @      @  @@            @    @       @@     @@        @@      @     @@      @   @@   @@      |\n|      @@        @@@@@@@   @@@@@@@@     @@@@@@@@      @@     @@@@@@@@  @@      @     @@@@@@@@     @@ @@       |\n|      @@        @  @      @@          @        @     @@     @@        @@      @     @@      @     @@@        |\n|      @@        @   @     @@         @          @    @@     @@        @@      @     @@      @     @@         |\n|      @@@@@@@@  @    @    @@@@@@@@  @            @   @@     @@@@@@@@  @@@@@@@@      @@@@@@@@     @@          |\n|                                                                                                             |\n|              @@       @@  @@@@@@@@@  @@      @@  @@@@@@@@   @@       @@                                     |\n|              @@       @@  @@         @@@     @@  @@       @  @@     @@                                      |\n|              @@       @@  @@         @@ @    @@  @@       @   @@   @@                                       |\n|              @@@@@@@@@@@  @@@@@@@@@  @@  @   @@  @@@@@@@@@     @@ @@                                        |\n|              @@       @@  @@         @@   @  @@  @@    @        @@@                                         |\n|              @@       @@  @@         @@    @ @@  @@     @       @@                                          |\n|              @@       @@  @@@@@@@@@  @@     @@@  @@      @     @@                                           |\n|                                                                                                             |\n|      @@         @@@@@@@@  @@@@@@@@@@@  @@@@@@@@@@@  @@         @@         @@@@@@@@   @@@@@@@  @@@@@@@@      |\n|      @@         @@            @@       @@           @@         @@            @@      @@       @@       @    |\n|      @@         @@            @@       @@           @@         @@            @@      @@       @@       @    |\n|      @@         @@@@@@@@      @@       @@@@@@@@@@@  @@         @@            @@      @@@@@@@  @@@@@@@@@     |\n|      @@         @@            @@       @@           @@         @@            @@      @@       @@   @        |\n|      @@         @@            @@       @@           @@         @@            @@      @@       @@    @       |\n|      @@@@@@@@@  @@@@@@@@      @@       @@@@@@@@@@@  @@@@@@@@@  @@@@@@@@@@ @@@@@@@@   @@@@@@@  @@     @      |\n.=============================================================================================================.")
    sleep(s)
print("watermarkat..........................[OK]")
def web(url):
    webbrowser.open_new("{}".format(url))
print ("webbrowser..........................[OK]")
# *=================================================================*
# |                    Important message                            |
# *=================================================================*
print("{}\nBefore we start:\n- Please make sure that you are running this program with admin rights\n- Please make sure you have installed pip on you're computer.\nIf this is not the case, you can download and install it here: https://bit.ly/3fNqe3F".format(attention()))
pause()
pause()
pause()

# *=================================================================*
# |                       Importing libraries                       |
# *=================================================================*

try:
    installer("pip install pip")
    print ("pip.................................[OK]")
    succespip="T"
except:
    print ("pip.................................[Fail]")
    succespip="F"

try:
    import os
    print ("os..................................[OK]")
    succeso="T"
except:
    print ("os..................................[Fail]")
    succeso="F"
try:
    import glob
    print ("glob................................[OK]")
    succesg="T"
except:
    print ("glob................................[Fail]")
    succesg="F"
try:
    import platform
    print ("platform............................[OK]")
    succespl="T"
except:
    print ("platform............................[Fail]")
    succespl="F"
try:
    import pygame
    print ("pygame..............................[OK]")
    succespy="T"
except:
    print("pygame..............................[Installing]")
    try:
        installer("py -m pip install -U pygame --user")
        print ("pygame..............................[Installed]")
        try:
            print("keys to play the game:\n    - space to shoot\n    - right arrow to go right\n    - left arrow to go left")
            pause()
            pause()
            installer("py -m pygame.examples.aliens")
            print("testing..............................[Success]")
            succespy="T"
        except:
            print("testing..............................[Fail]")
            succespy="F"
    except:
        print ("pygame..............................[Installation Failed]")
        print ("pygame..............................[Fail]")
        succespy="F"  
try:
    import shutil
    print ("shutil..............................[OK]")
    success="T"
except:
    print ("shutil..............................[Fail]")
    success="F"
try:
    from time import sleep
    print ("time................................[OK]")
    succesti="T"
except:
    print ("time................................[Fail]")
    succesti="F"

try:
    import thorpy
    print ("thorpy..............................[OK]")
    succesthor="T"
except:
    print("thorpy.............................[Installing]")
    try:
        installer("py -m pip install -U thorpy --user")
        print ("thorpy.............................[Installed]")
        succesthor="T"
    except:
        print ("thorpy..............................[Installation Failed]")
        print ("thorpy..............................[Fail]")
        succesthor="F"

try:
    import webbrowser
    print ("webbrowser..........................[OK]")
    succesweb="T"
except:
    print ("webbrowser..........................[Fail]")
    succesweb="F"

if succespip=="T" and succeso=="T" and succeso=="T" and succesg=="T" and succespl=="T" and succespy=="T" and success=="T" and succesti=="T" and succesthor=="T" and succesweb=="T":
    print ("Libraries...........................[OK]")
else:
    print ("Libraries...........................[Fail]")
    pause()
# *=================================================================*
# |                    Creating the German list                     |
# *=================================================================*

irregular_DE=[
    {"inf":"an/fangen","pras":"fängt...an","prat":"fing...an","perf":"hat angefangen","trad_fr":"commencer","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"befehlen","pras":"befiehlt","prat":"befahl","perf":"hat befohlen","trad_fr":"ordonner","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"beginnen","pras":"beginnt","prat":"begann","perf":"hat begonnen","trad_fr":"commencer","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"betrügen","pras":"betrügt","prat":"betrog","perf":"hat betrogen","trad_fr":"tromper","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"bewerben","pras":"bewirbt sich","prat":"bewarb sich","perf":"hat sich beworben","trad_fr":"être candidat","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"bieten","pras":"bietet","prat":"bot","perf":"hat geboten","trad_fr":"offrir","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"bitten","pras":"bittet","prat":"bat","perf":"hat gebeten","trad_fr":"demander","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"bleiben","pras":"bleibt","prat":"blieb","perf":"ist geblieben","trad_fr":"rester","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"brechen","pras":"bricht","prat":"brach","perf":"hat gebrochen","trad_fr":"briser","hint_fr":"(casser/tomber en panne/...)","trad_eng":"to shatter","hint_eng":"(to break/to break down/...)"},
    {"inf":"dürfen","pras":"darf","prat":"durfte","perf":"hat gedurft","trad_fr":"avoir l'autorisation de","hint_fr":"(quelqu'un/quelquechose)","trad_eng":"to be authorised to","hint_eng":"(do something), may/must/shall"},
    {"inf":"ein/laden","pras":"lädt...ein","prat":"lud...ein","perf":"hat eingeladen","trad_fr":"inviter","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"ein/treten","pras":"tritt...ein","prat":"trat...ein","perf":"ist eingetreten","trad_fr":"enter","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"empfangen","pras":"empfägnt","prat":"empfing","perf":"hat empfangen","trad_fr":"recevoir","hint_fr":"(quelquechose)","trad_eng":"to receive","hint_eng":"(a present/a bike/love/a parsel/a pastel/...)"},
    {"inf":"empfehlen","pras":"empfiehlt","prat":"empfahl","perf":"hat empfohlen","trad_fr":"recommander","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"empfinden","pras":"empfindet","prat":"empfand","perf":"hat empfunden","trad_fr":"ressentir","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"erschrecken","pras":"erschrickt","prat":"erschrak","perf":"ist erschrocken","trad_fr":"s'effrayer","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"essen","pras":"isst","prat":"ass","perf":"hat gegessen","trad_fr":"manger","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"fahren","pras":"fährt","prat":"fuhr","perf":"ist gefahren","trad_fr":"conduire","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"fallen","pras":"fällt","prat":"fiel","perf":"ist gefallen","trad_fr":"tomber","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"finden","pras":"findet","prat":"fand","perf":"hat gefunden","trad_fr":"trouver","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"fliegen","pras":"fliegt","prat":"flog","perf":"ist geflogen","trad_fr":"voler","hint_fr":"(en avion)","trad_eng":"","hint_eng":""},
    {"inf":"fliehen","pras":"flieht","prat":"floh","perf":"ist geflohen","trad_fr":"s'enfuir","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"fliessen","pras":"fliesst","prat":"floss","perf":"ist geflossen","trad_fr":"couler","hint_fr":"(pour quelqu'un/un bateau/...)","trad_eng":"to sink","hint_eng":"(for a boat/a person/...)"},
    {"inf":"fressen","pras":"frisst","prat":"frass","perf":"hat gefressen","trad_fr":"manger","hint_fr":"(pour les animaux)","trad_eng":"","hint_eng":""},
    {"inf":"frieren","pras":"friert","prat":"fror","perf":"hat gefroren","trad_fr":"geler","hint_fr":"geler, avoir froid","trad_eng":"","hint_eng":""},
    {"inf":"geben","pras":"gibt","prat":"gab","perf":"hat gegeben","trad_fr":"donner","hint_fr":"quelquechose","trad_eng":"","hint_eng":""},
    {"inf":"gehen","pras":"geht","prat":"ging","perf":"ist gegangen","trad_fr":"aller","hint_fr":"à pied","trad_eng":"","hint_eng":""},
    {"inf":"geniessen","pras":"geniesst","prat":"genoss","perf":"hat genossen","trad_fr":"jouir de","hint_fr":"(profiter de)","trad_eng":"to enjoy","hint_eng":""},
    {"inf":"gelingen","pras":"gelingt","prat":"gelang","perf":"ist gelungen","trad_fr":"réussir","hint_fr":"quelquechose/dans la vie/...","trad_eng":"","hint_eng":""},
    {"inf":"geschehen","pras":"geschieht","prat":"geschah","perf":"ist geschehen","trad_fr":"se produire","hint_fr":"","trad_eng":"","hint_eng":""},
    {"inf":"gewinnen","pras":"gewinnt","prat":"gewann","perf":"hat gewonnen","trad_fr":"gagner","hint_fr":"de l'argent","trad_en":"to win","hint_en":"something"},
    {"inf":"greifen","pras":"greift","prat":"griff","perf":"hat gegriffen","trad_fr":"saisir","hint_fr":"attraper quelquechose","trad_eng":"to acces","hint_eng":"to grasp"},
    {"inf":"haben","pras":"hat","prat":"hatte","perf":"hat gehabt","trad_fr":"avoir","hint_fr":"(quelquechose/quelqu'un/...)","trad_eng":"to have","hint_eng":"(something/somebody/...)"},
    {"inf":"halten","pras":"hält","prat":"hielt","perf":"hat geahlten","trad_fr":"s'arrêter","hint_fr":"tenir","trad_eng":"to stop","hint_eng":""},
    {"inf":"hängen","pras":"hängt","prat":"hing","perf":"hat gehangen","trad_fr":"accrocher","hint_fr":"dépendre de","trad_eng":"to hang","hint_eng":"to depend on"},
    {"inf":"heissen","pras":"heisst","prat":"hiess","perf":"hat geheissen","trad_fr":"s'appeler","hint_fr":"(le nom)","trad_eng":"to be called","hint_eng":"(your name)"},
    {"inf":"helfen","pras":"hilft","prat":"half","perf":"hat geholfen","trad_fr":"aider","hint_fr":"quelqu'un/quelquechose","trad_eng":"to help","hint_eng":"something/somebody"},
    {"inf":"kommen","pras":"kommt","prat":"kam","perf":"ist gekommen","trad_fr":"venir","hint_fr":"","trad_eng":"to come","hint_eng":""},
    {"inf":"können","pras":"kann","prat":"konnte","perf":"hat gekonnt","trad_fr":"pouvoir","hint_fr":"(être capable de/avoir le droit)","trad_eng":"to be able to","hint_eng":"(to be authorised to"},
    {"inf":"kriechen","pras":"kriecht","prat":"kroch","perf":"ist gekrochen","trad_fr":"ramper","hint_fr":"","trad_eng":"to crawl","hint_eng":""},
    {"inf":"laden","pras":"lädt","prat":"lud","perf":"hat geladen","trad_fr":"charger","hint_fr":"(télécharger/charger quelquechose)","trad_eng":"to load","hint_eng":"(to download/to upload/...)"},
    {"inf":"lassen","pras":"lässt","prat":"liess","perf":"hat gelassen","trad_fr":"laisser","hint_fr":"quelquechose","trad_eng":"to leave","hint_eng":"something"},
    {"inf":"laufen","pras":"läuft","prat":"lief","perf":"ist gelaufen","trad_fr":"courir","hint_fr":"","trad_eng":"to run","hint_eng":"somwhere"},
    {"inf":"leiden","pras":"leidet","prat":"litt","perf":"hat gelitten","trad_fr":"souffrir","hint_fr":"","trad_eng":"to suffer","hint_eng":""},
    {"inf":"leihen","pras":"leiht","prat":"lieh","perf":"hat geliehen","trad_fr":"prêter","hint_fr":"(quelquechose)","trad_eng":"to lend","hint_eng":"(something)"},
    {"inf":"lesen","pras":"liest","prat":"las","perf":"hat gelesen","trad_fr":"lire","hint_fr":"(ex: un livre)","trad_eng":"to read","hint_eng":"a book"},
    {"inf":"liegen","pras":"liegt","prat":"lag","perf":"hat gelegen","trad_fr":"être couché","hint_fr":"allongé","trad_eng":"to lie","hint_eng":"(down)"},
    {"inf":"lügen","pras":"lügt","prat":"log","perf":"hat gelogen","trad_fr":"mentir","hint_fr":"","trad_eng":"to lie","hint_eng":"about something"},
    {"inf":"mögen","pras":"mag","prat":"mochte","perf":"hat gemocht","trad_fr":"aimer","hint_fr":"(quelquechose/souhaiter)","trad_eng":"to like","hint_eng":"(to hope)"},
    {"inf":"müssen","pras":"muss","prat":"musste","perf":"hat gemusst","trad_fr":"être obligé","hint_fr":"(de/à/de faire quelquechose/à aller chez quelqu'un/...)","trad_eng":"to be obliged to","hint_eng":"(to have to go to somebody/to have to do someting)"},
    {"inf":"nehmen","pras":"nimmt","prat":"nahm","perf":"hat genomen","trad_fr":"prendre","hint_fr":"quelquechose","trad_eng":"to take","hint_eng":"something"},
    {"inf":"pfeifen","pras":"pfeift","prat":"pfiff","perf":"hat gepfiffen","trad_fr":"siffler","hint_fr":"(un air/action de siffler/...)","trad_eng":"to whistle","hint_eng":"(to call you're dog/to whistle a tune/...)"},
    {"inf":"raten","pras":"rät","prat":"riet","perf":"hat geraten","trad_fr":"conseiller","hint_fr":"quelqu'un/sur quelquechose","trad_eng":"to suggest","hint_eng":"something (to someody)"},
    {"inf":"reissen","pras":"reisst","prat":"riss","perf":"hat gerissen","perf2":"ist gerissen","trad_fr":"araché","hint_fr":"(rusé)","trad_eng":"snached","hint_eng":"(smart)"},
    {"inf":"reiten","pras":"reitet","prat":"ritt","perf":"ist geritten","trad_fr":"faire du cheval","hint_fr":"(aller à cheval)","trad_eng":"horse riding","hint_eng":"(to ride a horse)"},
    {"inf":"riechen","pras":"riecht","prat":"roch","perf":"hat gerochen","trad_fr":"sentir","hint_fr":"(Quelque chose)","trad_eng":"Something","hint_eng":""},
    {"inf":"rufen","pras":"ruft","prat":"rief","perf":"hat gerufen","trad_fr":"appeler","hint_fr":"(crier)","trad_eng":"to call","hint_eng":"scream"},
    {"inf":"scheinen","pras":"scheint","prat":"schein","perf":"hat geschienen","trad_fr":"briller","hint_fr":"sembler","trad_eng":"to appear","hint_eng":"to seem"},
    {"inf":"schiessen","pras":"schiesst","prat":"schoss","perf":"hat geschossen","trad_fr":"tirer","hint_fr":"(avec une arme)","trad_eng":"to shoot","hint_eng":""},
    {"inf":"schliessen","pras":"schliesst","prat":"schloss","perf":"hat geschlossen","trad_fr":"fermer","hint_fr":"conclure","trad_eng":"to end","hint_eng":"to conclude"},
    {"inf":"scheiben","pras":"scheibt","prat":"schob","perf":"hat geschoben","trad_fr":"pousser","hint_fr":"(quelquechose)","trad_eng":"to push","hint_eng":"(Something)"},
    {"inf":"schlafen","pras":"schläft","prat":"schlief","perf":"hat geschlafen","trad_fr":"dormir","hint_fr":"","trad_eng":"to sleep","hint_eng":""},
    {"inf":"schlagen","pras":"schlägt","prat":"schlug","perf":"hat geschlagen","trad_fr":"battre","hint_fr":"quelqu'un, quelquechose","trad_eng":"to beat","hint_eng":"somthing, sombody"},
    {"inf":"schneiden","pras":"schneidet","prat":"schnitt","perf":"hat geschnitten","trad_fr":"couper","hint_fr":"(quelquechose)","trad_eng":"to cut","hint_eng":"(food/something)"},
    {"inf":"schreiben","pras":"schreibt","prat":"schrieb","perf":"hat geschreiben","trad_fr":"écrire","hint_fr":"","trad_eng":"to write","hint_eng":""},
    {"inf":"schreien","pras":"schreit","prat":"schrie","perf":"hat geschrien","trad_fr":"crier","hint_fr":"","trad_eng":"to shout","hint_eng":""},
    {"inf":"schreiten","pras":"schreitet","prat":"schritt","perf":"ist geschritten","trad_fr":"marcher","hint_fr":"","trad_eng":"to walk","hint_eng":""},
    {"inf":"schweigen","pras":"schweigt","prat":"schwieg","perf":"hat geschwiegen","trad_fr":"se taire","hint_fr":"","trad_eng":"to remain silent","hint_eng":"keep quiet"},
    {"inf":"schwimmen","pras":"schwimmt","prat":"schwamm","perf":"ist geschwommen","trad_fr":"nager","hint_fr":"","trad_eng":"to swimm","hint_eng":""},
    {"inf":"sehen","pras":"sieht","prat":"sah","perf":"hat gesehen","trad_fr":"voir","hint_fr":"","trad_eng":"to see","hint_eng":""},
    {"inf":"singen","pras":"singt","prat":"sang","perf":"hat gesungen","trad_fr":"chanter","hint_fr":"","trad_eng":"to sing","hint_eng":""},
    {"inf":"sitzen","pras":"sitzt","prat":"sass","perf":"hat gesessen","trad_fr":"être assis","hint_fr":"","trad_eng":"to sit","hint_eng":""},
    {"inf":"sprechen","pras":"spricht","prat":"sprach","perf":"hat gesprochen","trad_fr":"parler","hint_fr":"","trad_eng":"to speak","hint_eng":""},
    {"inf":"springen","pras":"springt","prat":"sprang","perf":"ist gesprungen","trad_fr":"sauter","hint_fr":"(en l'air)","trad_eng":"to jump","hint_eng":""},
    {"inf":"stehen","pras":"steht","prat":"stand","perf":"hat gestanden","trad_fr":"être debout","hint_fr":"","trad_eng":"to stand up","hint_eng":""},
    {"inf":"stehlen","pras":"stiehlt","prat":"stahl","perf":"hat gestohlen","trad_fr":"voler","hint_fr":"dérober","trad_eng":"to steal","hint_eng":"(to rob)"},
    {"inf":"steigen","pras":"steigt","prat":"stieg","perf":"ist gestiegen","trad_fr":"monter","hint_fr":"","trad_eng":"to climb","hint_eng":""},
    {"inf":"sterben","pras":"stirbt","prat":"starb","perf":"ist gestorben","trad_fr":"mourir","hint_fr":"","trad_eng":"to die","hint_eng":""},
    {"inf":"streiten","pras":"streitet","prat":"stritt","perf":"hat gestritten","trad_fr":"se disputer","hint_fr":"","trad_eng":"to fight","hint_eng":"(to bicker)"},
    {"inf":"tragen","pras":"trägt","prat":"trug","perf":"hat getragen","trad_fr":"porter","hint_fr":"","trad_eng":"to carry","hint_eng":""},
    {"inf":"treffen","pras":"trifft","prat":"traf","perf":"hat getroffen","trad_fr":"atteindre","hint_fr":"rencontrer","trad_eng":"to reach","hint_eng":"to meat"},
    {"inf":"trinken","pras":"trinkt","prat":"trank","perf":"hat getrunken","trad_fr":"boire","hint_fr":"","trad_eng":"to drink","hint_eng":""},
    {"inf":"um/ziehen","pras":"zieht...um","prat":"zog...um","perf":"ist umgezogen","trad_fr":"déménager","hint_fr":"","trad_eng":"to move","hint_eng":"(in/out)"},
    {"inf":"vergessen","pras":"vergisst","prat":"vergass","perf":"hat vergessen","trad_fr":"oublier","hint_fr":"","trad_eng":"to forget","hint_eng":""},
    {"inf":"verlieren","pras":"verliert","prat":"verlor","perf":"hat verloren","trad_fr":"perdre","hint_fr":"(quelquechose)","trad_eng":"to loose","hint_eng":"(something)"},
    {"inf":"verschwinden","pras":"verschwindet","prat":"verschwand","perf":"ist verschwunden","trad_fr":"disparaître","hint_fr":"(de quelquepart)","trad_eng":"disapear","hint_eng":"(from somewhere)"},
    {"inf":"verstehen","pras":"versteht","prat":"verstand","perf":"hat verstanden","trad_fr":"comprendre","hint_fr":"(quelquechose)","trad_eng":"to understand","hint_eng":"(something)"},
    {"inf":"vor/werfen","pras":"wirft...vor","prat":"warf...vor","perf":"hat vorgeworfen","trad_fr":"reprocher","hint_fr":"accuser quelqu'un","trad_eng":"to blame","hint_eng":"(somebody)"},
    {"inf":"wachsen","pras":"wächst","prat":"wuchs","perf":"ist gewachsen","trad_fr":"croître","hint_fr":"pousser/grandir","trad_eng":"to grow","hint_eng":""},
    {"inf":"waschen","pras":"wäscht","prat":"wusch","perf":"hat gewaschen","trad_fr":"laver","hint_fr":"(des vêtements/...)","trad_eng":"to wash","hint_eng":"(clothes/...)"},
    {"inf":"werden","pras":"wird","prat":"wurde","perf":"ist geworden","trad_fr":"devenir","hint_fr":"","trad_eng":"to become","hint_eng":""},
    {"inf":"","pras":"","prat":"","perf":"","trad_fr":"","hint_fr":"","trad_eng":"","hint_eng":""},
    ]
print ("irregular_DE........................[OK]")
# *=================================================================*
# |                    Creating the English list                    |
# *=================================================================*
print ("irregular_EN........................[OK]")
# *=================================================================*
# |                    Creating the French list                     |
# *=================================================================*
print ("irregular_FR........................[OK]")
# *=================================================================*
# |                    Creating the Spanish list                    |
# *=================================================================*
print ("irregular_ES........................[OK]")
# *=================================================================*
# |                    Asking for the wished language               |                     |
# *=================================================================*
LanguageChosen="n"
while LanguageChosen!="y":
    print("What language would you like to studdy? [(De)utsch/(En)glish/(Fr)ançais/(Es)paňol]?:")
    Language="D"
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
    # if Language=="D" or Language=="De" or Language=="DE" or Language=="de":
    #     try:
    #         import DE_verbes_irréguliers
    #         print(irregulier_DE)
    #     except:
    #         print("""Please ensure that you have downloaded the file "DE_verbes_irréguliers.py"\nIf this isn't the case, you can dowload it by following this link: "" """)
    #     LanguageChosen="y"
    # elif Language=="E" or Language=="En" or Language=="EN" or Language=="en":
    #     try:
    #         import EN_verbes_irréguliers
    #     except:
    #         print("""Please ensure that you have downloaded the file "EN_verbes_irréguliers.py"\nIf this isn't the case, you can dowload it by following this link: "" """)
    # elif Language=="F" or Language=="Fr" or Language=="FR" or Language=="fr":
    #     try:
    #         import FR_verbes_irréguliers
    #     except:
    #         print("""Please ensure that you have downloaded the file "FR_verbes_irrégulierspy"\nIf this isn't the case, you can dowload it by following this link: "" """)
    # elif Language=="Es"  or Language=="ES" or Language=="es":
    #     try:
    #         import ES_verbes_irréguliers
    #     except:
    #         print("""Please ensure that you have downloaded the file "ES_verbes_irréguliers.py"\nIf this isn't the case, you can dowload it by following this link: "" """)
    pause()
print ("Language...........................[OK]")
# *=================================================================*
# |                    Checking relative paths                     |
# *=================================================================*
try:
    print ("Mainpath from getcwd: {}".format(os.getcwd()))
    mainpath=os.getcwd()
    print ("Mainpath variable: {}".format(mainpath))
    if platform.system()=="Windows":
        mainpath+="\\"
    else:
        mainpath+="/"
    print("mainpath: {}".format(mainpath))
    print ("paths..............................[OK]")
except:
    print ("paths..............................[Fail]")
    pause()

# *=================================================================*
# |              Checking if the folder audio exists                |
# *=================================================================*
A="audio"
fullpath=mainpath+A

if os.path.exists(fullpath)==False:
    try:
        os.makedirs("audio")
        print("Created the folder Audio")
    except:
        print("Failed to create the folder audio to be able to copy the audio files")
else:
    print("Audio Path.........................[OK]")
# *=================================================================*
# |                    Checking for the audio files                 |
# *=================================================================*
#--------- Innitiating dot process for graphic agreability ----------
givenSum=36
dots=givenSum
#----------------------------- Innitiating audio list --------------
sound=["Thriller.m4a"]
files=["anfangen","ass","befahl","befehlen","befiehlt","begann","beginnen","beginnt","betrog","betrügen","betrügt","bewarb sich","bewerben","bewirb sich","bieten","bietet","bitten","bittet","bleiben","bleibt","blieb","bot","brach","brechen","bricht","darf","durfte","dürfen","einladen","eintreten","empfahl","empfand","empfangen","empfehlen","empfiehlt","empfinden","empfindet","empfing","empfägnt","erschrak","erschrecken","erschrickt","essen","fahren","fand","fiel","finden","findet","fing...an","fliegen","fliegt","fliehen","flieht","fliessen","fliesst","flog","floh","floss","frass","fressen","frieren","friert","frisst","fror","fuhr","fährt","fällt","fängt...an","gab","geben","gehen","geht","gelang","gelingen","gelingt","geniessen","geniesst","genoss","geschah","geschehen","geschieht","gewann","gewinnen","gewinnt","gibt","ging","greifen","greift","griff","haben","half","halten","hat angefangen","hat befohlen","hat betrogen","hat eingeladen","hat empfangen","hat empfohlen","hat empfunden","hat gehalten","hat gebeten","hat geboten","hat gebrochen","hat gedurft","hat gefressen","hat gefroren","hat gefunden","hat gegeben","hat gegessen","hat gegriffen","hat gehabt","hat gehangen","hat geheissen","hat geholfen","hat gekonnt","hat geladen","hat gelassen","hat gelegen","hat gelesen","hat geliehen","hat gelogen","hat gemusst","hat genocht","hat genomen","hat genossen","hat gepfiffen","hat geraten","hat gerissen","hat gerochen","hat gerufen","hat geschienen","hat geschlafen","hat geschlagen","hat geschlossen","hat geschnitten","hat geschoben","hat geschossen","hat geschreiben","hat geschrien","hat geschwiegen","hat gesehen","hat gesessen","hat gesprochen","hat gestanden","hat gestolen","hat gestritten","hat gesungen","hat getragen","hat getroffen","hat gewaschen","hat gewonnen","hat sich geworben","hat vergessen","hat verloren","hat verstanden","hat vorgeworfen","hat...begonnen","hat","hatte","heissen","heisst","helfen","hielt","hiess","hilft","hing","hält","hängen","hängt","Infinitiv","isst","ist eingetreten","ist erschrocken","ist geblieben","ist gefahren","ist gefallen","ist geflogen","ist geflohen","ist geflossen","ist gegangen","ist gekommen","ist gekrochen","ist gelaufen","ist gelitten","ist gelungen","ist geritten","ist geschehen","ist geschritten","ist geschwommen","ist gesprungen","ist gestiegen","ist gestorben","ist getrunken","ist gewachsen","ist geworden","ist umgezogen","ist verschwunden","kam","kann","kommen","kommt","konnte","kreichen","kriecht","kroch","können","laden","lag","las","lassen","laufen","leiden","leidet","leihen","lesen","lief","liegen","liegt","lieh","liess","liest","litt","log","lud...ein","lud","lädt...ein","lädt","lässt","lügen","lügt","mag","mochte","muss","musste","mögen","müssen","nahm","nehmen","nimmt","perfekt","pfeifen","pfeift","pfif","Präsen","Präteritum","raten","reissen","reisst","reiten","reitet","riechen","rief","riet","riss","ritt","roch","rufen","ruft","rät","sah","sang","sass","scheiben","schein","scheinen","scheint","schiessen","schlafen","schlagen","schlief","schliessen","schliesst","schloss","schlug","schlägt","schneiden","schneidet","schnitt","schob","schoss","schreibt","schreien","schreit","schreiten","schreitet","schrie","schrieb","schritt","schwam","schweigen","schweigt","schwieg","schwimmen","schwimmt","sehen","sieht","singen","singt","sitzen","sitzt","sprach","sprang","sprechen","spricht","springen","springt","stahl","stand","starb","stehen","stehlen","steht","steigen","steigt","sterben","stieg","stiehlt","stirbt","streiten","streitet","stritt","traf","tragen","trank","trat...ein","treffen","trifft","trinken","trinkt","tritt...ein","trug","um ziehen","vergass","vergessen","vergisst","verlieren","verliert","verlor","verschwand","verschwinden","verschwindet","verstand","verstehen","versteht","vor werfen","wachsen","warf...for","waschen","werden","wird","wirft...vor","wuchs","wurde","wusch","wäschst","wäscht","zieht...um","zog...um"]
#----------------------------- Innitiating extension list --------------
formatt=["mp4","wav","mp3"]
formaT=0
# ------- Checking if the files exist and are in the right place -------
for a in range(len(files)):
    dots=givenSum
    sums=len(files[a])+1+len(formatt[formaT])
    dot=""
    for i in range(dots-sums):
        dot+="."
    if os.path.exists("{}{}.{}".format(fullpath,files[a],formatt[formaT])):
        print ("Sound: {}.{}{}[OK]".format(files[a],formatt[formaT],dot))
    else:
        print ("""Fatal Error: The file : "{}.{}" does not exist in the folder Audio.\nTrying to copy from the source folder of the program""".format(files[a],formatt[formaT]))
        try:
            filePath = shutil.copy('{}.{}'.format(files[a],formatt[formaT]), '{}'.format(fullpath))
            print ("Sound: {}.{}{}[Copied]".format(files[a],formatt[formaT],dot))
        except:
            print ("""{}\nLeathal Error:\nThe file : "{}.{}" does not exist at the source of the program, please run the file {}_Sounds.exe and make sure the installation path is {}.""".format(attention(),files[a],formatt[formaT],filenames,fullpath))
            break
pause()
# *=================================================================*
# |                       Launching program                         |
# *=================================================================*
print ("Launching program")
for i in range(114):
    print(".",end="")


watermarkf(3)