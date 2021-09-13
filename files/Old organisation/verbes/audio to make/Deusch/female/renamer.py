import os
import platform
def pause():
    pause=input("Press enter to continue...")
files=["anfangen","ass","befahl","befehlen","befiehlt","begann","beginnen","beginnt","betrog","betrügen","betrügt","bewarb sich","bewerben","bewirb sich","bieten","bietet","bitten","bittet","bleiben","bleibt","blieb","bot","brach","brechen","bricht","darf","durfte","dürfen","einladen","eintreten","empfahl","empfand","empfangen","empfehlen","empfiehlt","empfinden","empfindet","empfing","empfägnt","erschrak","erschrecken","erschrickt","essen","fahren","fand","fiel","finden","findet","fing...an","fliegen","fliegt","fliehen","flieht","fliessen","fliesst","flog","floh","floss","frass","fressen","frieren","friert","frisst","fror","fuhr","fährt","fällt","fängt...an","gab","geben","gehen","geht","gelang","gelingen","gelingt","geniessen","geniesst","genoss","geschah","geschehen","geschieht","gewann","gewinnen","gewinnt","gibt","ging","greifen","greift","griff","haben","half","halten","hat angefangen","hat befohlen","hat betrogen","hat eingeladen","hat empfangen","hat empfohlen","hat empfunden","hat geahlten","hat gebeten","hat geboten","hat gebrochen","hat gedurft","hat gefressen","hat gefroren","hat gefunden","hat gegeben","hat gegessen","hat gegriffen","hat gehabt","hat gehangen","hat geheissen","hat geholfen","hat gekonnt","hat geladen","hat gelassen","hat gelegen","hat gelesen","hat geliehen","hat gelogen","hat gemusst","hat genocht","hat genomen","hat genossen","hat gepfiffen","hat geraten","hat gerissen","hat gerochen","hat gerufen","hat geschienen","hat geschlafen","hat geschlagen","hat geschlossen","hat geschnitten","hat geschoben","hat geschossen","hat geschreiben","hat geschrien","hat geschwiegen","hat gesehen","hat gesessen","hat gesprochen","hat gestanden","hat gestanden1","hat gestolen","hat gestritten","hat gesungen","hat getragen","hat getroffen","hat gewaschen","hat gewonnen","hat sich geworben","hat vergessen","hat verloren","hat verstanden","hat vorgeworfen","hat...begonnen","hat","hat1","hatte","heissen","heisst","helfen","hielt","hiess","hilft","hing","hält","hängen","hängt","Infinitiv","isst","ist eingetreten","ist erschrocken","ist geblieben","ist gefahren","ist gefallen","ist geflogen","ist geflohen","ist geflossen","ist gegangen","ist gekommen","ist gekrochen","ist gelaufen","ist gelitten","ist gelungen","ist geritten","ist geschehen","ist geschritten","ist geschwommen","ist gesprungen","ist gestiegen","ist gestorben","ist getrunken","ist gewachsen","ist geworden","ist umgezogen","ist verschwunden","kam","kann","kommen","kommt","konnte","kreichen","kriecht","kroch","können","laden","lag","las","lassen","laufen","leiden","leiden1","leidet","leihen","lesen","lief","liegen","liegt","lieh","liess","liest","litt","log","lud...ein","lud","lädt...ein","lädt","lässt","lässt1","lügen","lügt","mag","mochte","muss","musste","mögen","müssen","nahm","nehmen","nimmt","perfekt","perfekt1","pfeifen","pfeift","pfif","Präsen","präsen1","Präteritum","präteritum1","raten","reissen","reisst","reiten","reitet","riechen","rief","riet","riss","ritt","roch","rufen","ruft","rät","sah","sang","sass","scheiben","schein","scheinen","scheint","schiessen","schlafen","schlagen","schlief","schliessen","schliesst","schliesst1","schloss","schlug","schlägt","schneiden","schneidet","schnitt","schob","schoss","schreibt","schreien","schreit","schreiten","schreitet","schrie","schrieb","schritt","schwam","schweigen","schweigt","schwieg","schwimmen","schwimmt","sehen","sieht","singen","singt","sitzen","sitzt","sprach","sprang","sprechen","spricht","springen","springt","stahl","stand","starb","stehen","stehlen","steht","steigen","steigt","sterben","stieg","stiehlt","stirbt","streiten","streitet","stritt","traf","tragen","trank","trat...ein","treffen","trifft","trinken","trinkt","tritt...ein","trug","um ziehen","vergass","vergessen","vergisst","verlieren","verliert","verlor","verschwand","verschwinden","verschwindet","verstand","verstehen","versteht","vor werfen","wachsen","warf...for","waschen","werden","wird","wirft...vor","wuchs","wurde","wusch","wäschst","wäscht","zieht...um","zog...um"]
TypeOfVoice=["male","female"]
Language=["DE","EN","FR","ES"]
formatt=["mp4","wav"]
formaT=0
languagE=0
typeofvoicE=1
givenSum=36
dots=givenSum
# print("Files in current firectory:\n{}".format())
dot=""
try:
    print ("Mainpath from getcwd: {}".format(os.getcwd()))
    mainpath=os.getcwd()
    print ("Mainpath variable: {}".format(mainpath))
    if platform.system()=="Windows":
        mainpath+="\\"
    else:
        mainpath+="/"
    print("mainpath: {}".format(mainpath))
    print ("Mainpath....................................[OK]")
except:
    print ("Mainpath....................................[Fail]")
folder="processed"
for i in range(dots-(len(folder))):
        dot+="."
try:
    if os.path.exists("{}{}".format(mainpath,folder)):
        print("Folder:{}{}[Exists]".format(folder,dot))
    else:
        os.makedirs("processed")
        print("Creation of folder:{}{}[OK]".format(folder,dot))
    if platform.system()=="Windows":
       folder+="\\"
    else:
        folder+="/"
except:
    print("Creation of folder:{}{}[Fail]".format(folder,dot))
for Files in range(len(files)):
    dots=givenSum
    sums=len(files[Files])+1+len(formatt[formaT])
    dot=""
    for i in range(dots-sums):
        dot+="."
    if os.path.exists("{}.{}".format(files[Files],formatt[formaT])):
        print("file:{}.{}{}[exists]".format(files[Files],formatt[formaT],dot))
        try:
            os.rename("{}.{}".format(files[Files],formatt[formaT]),"{}{}{}_{}_{}.{}".format(mainpath,folder,Language[languagE],TypeOfVoice[typeofvoicE],files[Files],formatt[formaT]))
            print("file:{}.{}{}[Renamed]".format(files[Files],formatt[formaT],dot))
            print("file:{}.{}{}[OK]".format(files[Files],formatt[formaT],dot))
        except:
            print("file:{}.{}{}[Fail]".format(files[Files],formatt[formaT],dot))
    else:
        print ("""Fatal Error: The file : "{}.{}" does not exist in the folder {}.""".format(files[Files],formatt[formaT],os.path.basename(mainpath)))
pause()
pause()