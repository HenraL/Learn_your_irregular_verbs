__name__="Learn Your Vocab"
__Author__="Henry Letellier"
__Version__="2.0"
__Disclaimer__="This program is provided as if and without any warranty of any kind.\nThe Author of this progam cannot be Held responsible for any dammage occuring on you computer."
__annotations__="This program was created to help people Learn their irregular Verbs.\nThis program is completely free.\n"
from tkinter import *
import random, os
from datetime import datetime
try:
    from tkinter import *
except:
    from Tkinter import *
class Windows:
    def __init__(self,EN,DE,ES,FR,ColumnsLang):
        #__________________ everything is OK __________________
        self.a="GUI"
        #__________________ Default name of the current user __________________
        self.username=f"Henry Letellier (test)_{os.getlogin()}"
        #__________________ Default colours for the foreground and the Background __________________
        self.universalBackground="white"
        self.universalForeground="black"
        #__________________ Default size for tkinter windows __________________
        self.size_x=700
        self.size_y=350
        self.geometry=f"{self.size_x}x{self.size_y}"
        self.size_questions_x=self.size_x-20
        self.size_questions_y=self.size_y-100
        self.geometry_questions=f"{self.size_questions_x}x{self.size_questions_y}"
        self.size_stat_windows_x=self.size_x-20
        self.size_stat_windows_y=self.size_y-180
        self.geometry_stat_windows=f"{self.size_stat_windows_x}x{self.size_stat_windows_y}"
        self.size_small_window_x=self.size_x-550
        self.size_small_window_y=self.size_y-300
        self.geometry_small_window=f"{self.size_small_window_x}x{self.size_small_window_y}"
        #__________________ Vars for the software Icon __________________
        self.icon=""
        self.hasIcon=False
        #_________________ Watermark _________________
        self.watermark=f"{chr(169)} Created by Henry Letellier"
        self.innerPadding=5
        self.PMethod="written" #Preview Method (liked to a radio on the main menu screen)
        #_________________ Name of the folders for the different files _________________
        self.ProgressFolder="SavedProgress"
        self.logDir="logs"
        #_________________ Vars for loading from saved files _________________
        self.loadedSavedProgress=False
        self.timeInfoRestore=0

        #_________________ Gathering DATA _________________
        self.OSInfo={
            "name":os.name,
            "CPU count":os.cpu_count(),
            "Curent directory":os.curdir,
            "Directory seperator":os.altsep,
            "defpath":os.defpath,
            "devnull":os.devnull,
            "device_encoding(0)":os.device_encoding(0),
            "device_encoding(1)":os.device_encoding(1),
            "device_encoding(2)":os.device_encoding(2),
            "environement":os.environ,
            "cwd":os.getcwd(),
            "dir Content":os.listdir("./"),
            "Logged in account":os.getlogin(),
            "Current process ID":os.getpid(),
            "exstep":os.extsep,
            "F_OK":os.F_OK,
            "getcwdb":os.getcwdb(),
            "PPID":os.getppid(),
            "get_inheritable":os.get_inheritable(1),
            "supports_bytes_environ":os.supports_bytes_environ,
            "O_APPEND":os.O_APPEND,
            "O_BINARY":os.O_BINARY,
            "O_CREAT":os.O_CREAT,
            "__spec__":os.__spec__,
            "O_RDONLY":os.O_RDONLY,
            "O_WRONLY":os.O_WRONLY,
            "O_RDWR":os.O_RDWR,
            "O_EXCL":os.O_EXCL,
            "O_TRUNC":os.O_TRUNC,
            "O_NOINHERIT":os.O_NOINHERIT,
            "O_SHORT_LIVED":os.O_SHORT_LIVED,
            "O_TEMPORARY":os.O_TEMPORARY,
            "O_RANDOM":os.O_RANDOM,
            "O_SEQUENTIAL":os.O_SEQUENTIAL,
            "O_TEXT":os.O_TEXT,
            "R_OK":os.R_OK,
            "W_OK":os.W_OK,
            "X_OK":os.X_OK,
            "SEEK_SET":os.SEEK_SET,
            "SEEK_CUR":os.SEEK_CUR,
            "SEEK_END":os.SEEK_END,
            "supports_dir_fd":os.supports_dir_fd,
            "supports_effective_ids":os.supports_effective_ids,
            "supports_fd":os.supports_fd,
            "supports_follow_symlinks":os.supports_follow_symlinks,
            "P_NOWAIT":os.P_NOWAIT,
            "P_NOWAITO":os.P_NOWAITO,
            "P_WAIT":os.P_WAIT,
            "P_DETACH":os.P_DETACH,
            "P_OVERLAY":os.P_OVERLAY,
            "directory string":os.pardir,
            "separate pathname components":os.sep,
            "character seperating search paths":os.pathsep,
            "default search path":os.defpath,
            "string used to separate lines":f"\"{os.linesep}\"",
            "The files path of the null device":os.devnull
            }

        #variables
        #self.Font="Algerian"
        self.Font="Times_New_Roman"
        #self.Font=""

        #self.Size=14
        self.Size=10
        # self.Size=8
        #____________________ Window global font ____________________
        self.defaultFont=(self.Font,self.Size,"normal")
        #____________________ Language lists ____________________
        self.EN=EN
        self.DE=DE
        self.ES=ES
        self.FR=FR

        #_____________________ Default settings for the vars of the chosen language for any exercise _____________________
        self.ChosenLanguage="EN"
        self.ContentLanguage=EN
        self.ListLength=len(EN)
        self.ColumnsLang=ColumnsLang
        self.enableOrDisable={"EN":"disable","DE":"disable","ES":"disable","FR":"disable","written":"normal","radio":"disable","female":"disabled","male":"disabled"}
        self.errorColors=["red2","orange","blue","IndianRed2","DarkGoldenrod3","brown3","tomato","tomato2","tomato3","tomato4","orange red","SteelBlue3","MediumPurple4","gray29"]
        self.successColors=["sea green","forest green","green4","OliveDrab4","SpringGreen4","LightGoldenrod4","aquamarine4","dark green","dark olive green","cyan4"]
        
        #__________________________ setting all the time variables to "" __________________________
        self.microsecond=""
        self.second=""
        self.minute=""
        self.hour=""
        self.day=""
        self.month=""
        self.year=""
        self.Date=""
        self.Time=""
        self.Timep=""
        self.All=""
        self.Alls=""
        self.first_time_started=0
        #_____________________________ Audio preferences _____________________________
        self.VoiceType="Female"
        #_____________________________ Var that controls the internal gameplay _____________________________
        self.ToAdd=0
        self.InfAnswerRevealed=0
        self.PresAnswerRevealed=0
        self.PretAnswerRevealed=0
        self.PerfAnswerRevealed=0

    class SubOperations:
        def Excess(time,format):
            """Calculates the excess time so that it can be added to the time above it ms>s>minutes>h>d>months>y"""
            overflow=0
            while time>=format:
                time-=format
                overflow+=1
            return overflow,time
        def splitTime(self,Start_time,Stop_time,total_time=0):
            update.date(self)
            print(f"Start_time={Start_time},Stop_time={Stop_time}")
            st=Start_time.split("/")
            st_d=int(st.pop(0))
            st_mo=int(st.pop(0))
            st=st[0].split(":")
            st_y=int(st.pop(0))
            st=st[0].split("h")
            st_h=int(st.pop(0))
            st=st[0].split("min")
            st_min=int(st.pop(0))
            st=st[0].split("s")
            st_s=int(st.pop(0))
            st=st[0].split("m")
            st_ms=int(st.pop(0))

            et=Stop_time.split("/")
            et_d=int(et.pop(0))
            et_mo=int(et.pop(0))
            et=et[0].split(":")
            et_y=int(et.pop(0))
            et=et[0].split("h")
            et_h=int(et.pop(0))
            et=et[0].split("min")
            et_min=int(et.pop(0))
            et=et[0].split("s")
            et_s=int(et.pop(0))
            et=et[0].split("m")
            et_ms=int(et.pop(0))


            if et_ms>st_ms:
                ms=et_ms-st_ms
            else:
                ms=st_ms-et_ms
            grub=Windows.SubOperations.Excess(time=ms,format=1000)
            ms=int(grub[1])
            et_s+=int(grub[0])

            if et_s>st_s:
                s=et_s-st_s
            else:
                s=st_s-et_s
            grub=Windows.SubOperations.Excess(time=s,format=60)
            s=grub[1]
            et_min+=grub[0]
            
            if et_min>st_min:
                minute=et_min-st_min
            else:
                minute=st_min-et_min
            grub=Windows.SubOperations.Excess(time=minute,format=60)
            minute=int(grub[1])
            et_h+=int(grub[0])
            
            if et_h>st_h:
                h=et_h-st_h
            else:
                h=st_h-et_h
            grub=Windows.SubOperations.Excess(time=h,format=24)
            h=int(grub[1])
            et_d+=int(grub[0])
            
            if et_d>st_d:
                d=et_d-st_d
            else:
                d=st_d-et_d
            grub=Windows.SubOperations.Excess(time=d,format=30)
            d=int(grub[1])
            et_mo+=int(grub[0])

            if et_mo>st_mo:
                mo=et_mo-st_mo
            else:
                mo=st_mo-et_mo
            grub=Windows.SubOperations.Excess(time=mo,format=12)
            mo=int(grub[1])
            et_y+=int(grub[0])

            if et_y>st_y:
                y=et_y-st_y
            else:
                y=st_y-et_y
            
            if total_time!=0:
                print(f"total_time={total_time}")
                if total_time["ms"]>ms:
                    ms=total_time["ms"]+ms
                else:
                    ms=ms+total_time["ms"]
                grub=Windows.SubOperations.Excess(time=ms,format=1000)
                ms=int(grub[1])
                et_s+=int(grub[0])
                
                if total_time["s"]>s:
                    s=total_time["s"]+s
                else:
                    s=s+total_time["s"]
                grub=Windows.SubOperations.Excess(time=s,format=60)
                s=int(grub[1])
                et_min+=int(grub[0])
                
                if total_time["minute"]>minute:
                    minute=total_time["minute"]+minute
                else:
                    minute=minute+total_time["minute"]
                grub=Windows.SubOperations.Excess(time=minute,format=60)
                minute=int(grub[1])
                et_h+=int(grub[0])

                if total_time["h"]>h:
                    h=total_time["h"]+h
                else:
                    h=h+total_time["h"]
                grub=Windows.SubOperations.Excess(time=h,format=24)
                h=int(grub[1])
                et_d+=int(grub[0])
                
                if total_time["d"]>d:
                    d=total_time["d"]+d
                else:
                    d=d+total_time["d"]
                grub=Windows.SubOperations.Excess(time=d,format=30)
                d=int(grub[1])
                et_mo+=int(grub[0])
                
                if total_time["mo"]>mo:
                    mo=total_time["mo"]+mo
                else:
                    mo=mo+total_time["mo"]
                grub=Windows.SubOperations.Excess(time=mo,format=12)
                mo=int(grub[1])
                et_y+=int(grub[0])
                if total_time["y"]>y:
                    y=total_time["y"]+y
                else:
                    y=y+total_time["y"]
                
            print(f"d={d},type({d})={type(d)},mo={mo},type({mo})={type(mo)},y={y},type({y})={type(y)},h={h},type({h})={type(h)},minute={minute},type({minute})={type(minute)},s={s},type({s})={type(s)},ms={ms},type({ms})={type(ms)}")
            # r={"dp":int(d),"mop":int(mo),"yp":int(y),"hp":int(h),"minutep":int(minute),"sp":int(s),"msp":int(ms)}
            r={"dp":d,"mop":mo,"yp":y,"hp":h,"minutep":minute,"sp":s,"msp":ms}
            p={"dp":"","mop":"","yp":"","hp":"","minutep":"","sp":"","msp":""}
            for i in p:
                print(f"type({r[i]})=type(r[{i}])={type(r[i])}")
                e=int(r[i])
                if e>1:
                    p[i]="s"
            return {"d":d,"mo":mo,"y":y,"h":h,"minute":minute,"s":s,"ms":ms,"r":r,"p":p}
        def TrippleTermCall(self,exercise,WTOrTW=0):
            """Function for the interaction of a three entry box"""
            print(f"Tripple Term Call,exercise={exercise},WTOrTW={WTOrTW}")
            update.date(self)
            log.ExerciseStarted(self,exercise)
            start_time=self.Alls
            continueExercise=True
            index=score=0
            Windows.RestoreProgress(self,language=self.ChosenLanguage,exercise=exercise)
            print(f"\n\n\nexercise={exercise}\nstart_time={start_time}\ncontinueExercise={continueExercise}\nindex={index}\nscore={score}\nself.ListLength={self.ListLength}\n\n\nRestoredResults={self.timeInfoRestore}")
            if self.timeInfoRestore!=0:
                index=self.timeInfoRestore["index"]
                score=self.timeInfoRestore["score"]
            while continueExercise==True and index<=self.ListLength:
                print(f"\n\n\nexercise={exercise}\nstart_time={start_time}\ncontinueExercise={continueExercise}\nindex={index}\nscore={score}\nself.ListLength={self.ListLength}\n\n\n")
                # print(f"self.ContentLanguage={self.ContentLanguage}")
                current=self.ContentLanguage[index]
                term=""
                if 'trad_fr' in current:
                    term+=f"{current['trad_fr']}/"
                if 'trad_eng' in current:
                    term+=f"{current['trad_eng']}/"
                if 'trad_de' in current:
                    term+=f"{current['trad_de']}/"
                if 'trad_es' in current:
                    term+=f"{current['trad_es']}"
                if self.ChosenLanguage=='EN':
                    lang='infinitive'
                elif self.ChosenLanguage=='DE':
                    lang='inf'
                elif self.ChosenLanguage=='ES':
                    lang=''
                else:
                    lang='infinitif'
                CorrectAnswer=[]
                for i in range(2):
                    CorrectAnswer.append(current[self.ColumnsLang[self.ChosenLanguage][i]])
                if self.ChosenLanguage!="EN": 
                    CorrectAnswer.append(current[self.ColumnsLang[self.ChosenLanguage][3]])
                hintENG=hintDE=hintES=hintFR=""
                if 'hint_eng' in current:
                    hintENG=current['hint_eng']
                if 'hint_de' in current:
                    hintDE=current['hint_de']
                if 'hint_es' in current:
                    hintES=current['hint_es']
                if 'hint_fr' in current:
                    hintFR=current['hint_fr']
                if WTOrTW==0:
                    result=Windows.SubOperations.AskTripple(self,typeRequired="definition",word=term,correctAnswer=CorrectAnswer,hintFR=hintFR,hintENG=hintENG,hintDE=hintDE,hintES=hintES,WTOrTW=WTOrTW)
                else:
                    result=Windows.SubOperations.AskTripple(self,typeRequired="term",word=current[lang],correctAnswer=CorrectAnswer,hintFR=hintFR,hintENG=hintENG,hintDE=hintDE,hintES=hintES,WTOrTW=WTOrTW)
                print("################################################################################################################################################################################")
                print(f"\n\n\nexercise={exercise}\nstart_time={start_time}\ncontinueExercise={continueExercise}\nindex={index}\nscore={score}\nself.ListLength={self.ListLength}\nresult={result}\n\n\n")
                print("################################################################################################################################################################################")
                if self.ToAdd=="Stop exercise":
                    continueExercise=False
                else:
                    print(f"result={result},self.ToAdd={self.ToAdd}")
                    score+=self.ToAdd
                    index+=1
                    print(f"score={score},index={index}")
                print(f"\n\n\nexercise={exercise}\nstart_time={start_time}\ncontinueExercise={continueExercise}\nindex={index}\nscore={score}\nself.ListLength={self.ListLength}\nresult={result}\n\n\n")
                
            print("out of loop")
            update.date(self)
            log.ExerciseStopped(self,exercise)
            end_time=self.Alls
            
            if index>0 and index<self.ListLength:
                Windows.SaveProgress(self,language=self.ChosenLanguage,progress=index,score=score,exercise=exercise,time_start=start_time,time_end=end_time,total_time=self.timeInfoRestore)
            Windows.ScoreBoard(self,score=score,answ_questions=index,tot_questions=self.ListLength,exercise=exercise,time_start=start_time,time_stop=end_time,total_time=self.timeInfoRestore)
            log.questions(self,answ_questions=index,tot_questions=self.ListLength,exercise=exercise)
            log.score(self,score,exercise)
            log.Time(self,Start_time=start_time,Stop_time=end_time,exercise=exercise,total_time=self.timeInfoRestore)
        def DoubleTermCall(self,exercise,TDOrDT=0):
            update.date(self)
            log.ExerciseStarted(self,exercise)
            start_time=self.Alls
            continueExercise=True
            index=score=0
            Windows.RestoreProgress(self,language=self.ChosenLanguage,exercise=exercise)
            print(f"\n\n\nexercise={exercise}\nstart_time={start_time}\ncontinueExercise={continueExercise}\nindex={index}\nscore={score}\nself.ListLength={self.ListLength}\n\n\nRestoredResults={self.timeInfoRestore}")
            if self.timeInfoRestore!=0:
                index=self.timeInfoRestore["index"]
                score=self.timeInfoRestore["score"]
            while continueExercise==True and index<=self.ListLength:
                print(f"\n\n\nexercise={exercise}\nstart_time={start_time}\ncontinueExercise={continueExercise}\nindex={index}\nscore={score}\nself.ListLength={self.ListLength}\n\n\n")
                # print(f"self.ContentLanguage={self.ContentLanguage}")
                current=self.ContentLanguage[index]
                term=""
                if 'trad_fr' in current:
                    term+=f"{current['trad_fr']}/"
                if 'trad_eng' in current:
                    term+=f"{current['trad_eng']}/"
                if 'trad_de' in current:
                    term+=f"{current['trad_de']}/"
                if 'trad_es' in current:
                    term+=f"{current['trad_es']}"
                if self.ChosenLanguage=='EN':
                    lang='infinitive'
                elif self.ChosenLanguage=='DE':
                    lang='inf'
                elif self.ChosenLanguage=='ES':
                    lang=''
                else:
                    lang='infinitif'
                hintENG=hintDE=hintES=hintFR=""
                if 'hint_eng' in current:
                    hintENG=current['hint_eng']
                if 'hint_de' in current:
                    hintDE=current['hint_de']
                if 'hint_es' in current:
                    hintES=current['hint_es']
                if 'hint_fr' in current:
                    hintFR=current['hint_fr']
                if TDOrDT==0:
                    result=Windows.SubOperations.AskDouble(self,typeRequired="definition",word=term,correctAnswer=current[lang],hintFR=hintFR,hintENG=hintENG,hintDE=hintDE,hintES=hintES)
                else:
                    result=Windows.SubOperations.AskDouble(self,typeRequired="term",word=current[lang],correctAnswer=term,hintFR=hintFR,hintENG=hintENG,hintDE=hintDE,hintES=hintES)
                print("################################################################################################################################################################################")
                print(f"\n\n\nexercise={exercise}\nstart_time={start_time}\ncontinueExercise={continueExercise}\nindex={index}\nscore={score}\nself.ListLength={self.ListLength}\nresult={result}\n\n\n")
                print("################################################################################################################################################################################")
                if self.ToAdd=="Stop exercise":
                    continueExercise=False
                else:
                    print(f"result={result},self.ToAdd={self.ToAdd}")
                    score+=self.ToAdd
                    index+=1
                    print(f"score={score},index={index}")
                print(f"\n\n\nexercise={exercise}\nstart_time={start_time}\ncontinueExercise={continueExercise}\nindex={index}\nscore={score}\nself.ListLength={self.ListLength}\nresult={result}\n\n\n")
                
            print("out of loop")
            update.date(self)
            log.ExerciseStopped(self,exercise)
            end_time=self.Alls
            
            if index>0 and index<self.ListLength:
                Windows.SaveProgress(self,language=self.ChosenLanguage,progress=index,score=score,exercise=exercise,time_start=start_time,time_end=end_time,total_time=self.timeInfoRestore)
            Windows.ScoreBoard(self,score=score,answ_questions=index,tot_questions=self.ListLength,exercise=exercise,time_start=start_time,time_stop=end_time,total_time=self.timeInfoRestore)
            log.questions(self,answ_questions=index,tot_questions=self.ListLength,exercise=exercise)
            log.score(self,score,exercise)
            log.Time(self,Start_time=start_time,Stop_time=end_time,exercise=exercise,total_time=self.timeInfoRestore)
        def gameCheck(hintUsed,Answer,correctAnswer,AnswerRevealed,Block=None):
            total=0
            tryAgain=False
            if AnswerRevealed==1:
                total-=2
            elif hintUsed==1:
                total-=1
            else:
                pass
            if Answer in correctAnswer:
                total+=2
                returnContent="Correct"
                print(f"total={total}")
            else:
                tryAgain=True
                if Block!=None:
                    returnContent=f"Wrong Answer for {Block}, try again."
                else:
                    returnContent="Wrong Answer, try again."
            print(f"\n\n\ntotal={total}\ntryAgain={tryAgain}\nreturnContent={returnContent}\n\n\n")
            return total,tryAgain,returnContent
        def AskDouble(self,typeRequired="definition",word="ee",correctAnswer="ee",hintFR="",hintENG="",hintDE="",hintES=""):
            self.hintUsed=0
            self.AnswerRevealed=0
            self.ToAdd=0
            def submit(*args):
                GivenAnswer=entree.get()
                print(f"GivenAnswer='{GivenAnswer}',len(GivenAnswer)={len(GivenAnswer)}")
                if len(GivenAnswer)>0:
                    Verdict=Windows.SubOperations.gameCheck(self.hintUsed,GivenAnswer,correctAnswer,self.AnswerRevealed)
                else:
                    Verdict=["",True,"Please enter something in the box before pressing Submit."]
                
                print(f"\n\n\nGivenAnswer='{GivenAnswer}'\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\nVerdict={Verdict}\nVerdict[0]={Verdict[0]}\nVerdict[1]={Verdict[1]}\nVerdict[2]={Verdict[2]}\n\n\n")
                print("")

                if Verdict[1]==False:
                    LabelWrong.config(text=f"Correct.")
                    LabelWrong.config(font=(self.Font,self.Size,"bold"))
                    LabelWrong.config(fg=self.successColors[random.randint(0,len(self.successColors)-1)])
                    ButtonContinue.pack(side=LEFT,fill=X)

                    ButtonSubmit.pack_forget()
                    ButtonHintFR.pack_forget()
                    ButtonHintENG.pack_forget()
                    ButtonHintDE.pack_forget()
                    ButtonHintES.pack_forget()
                    ButtonRevealAnswer.pack_forget()
                    ButtonContinue.pack_configure(fill=X,side=BOTTOM)
                    StopButton.pack_forget()
                    print(f"\n\n\nGivenAnswer='{GivenAnswer}'\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\nVerdict={Verdict}\nVerdict[0]={Verdict[0]}\nVerdict[1]={Verdict[1]}\nVerdict[2]={Verdict[2]}\n\n\n")
                    print("")
                    self.ToAdd=Verdict[0]
                    return self.ToAdd
                else:
                    LabelWrong.config(text=Verdict[2])
                    LabelWrong.config(font=(self.Font,self.Size,"bold"))
                    LabelWrong.config(fg=self.errorColors[random.randint(0,len(self.errorColors)-1)])
                print(f"\n\n\nGivenAnswer='{GivenAnswer}'\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\nVerdict={Verdict}\n\n\n")
                print("")
            def proceed():
                TTT.destroy()
            def HintFR():
                ShowHintFR.config(text=f"French Hint: '{hintFR}'")
                self.hintUsed=1
                print(f"\ncorrectAnswer={correctAnswer}\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\n\n\n")
                print("")
            def HintENG():
                ShowHintENG.config(text=f"English Hint: '{hintENG}'")
                self.hintUsed=1
                print(f"\ncorrectAnswer={correctAnswer}\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\n\n\n")
                print("")
            def HintDE():
                ShowHintDE.config(text=f"German Hint: '{hintDE}'")
                self.hintUsed=1
                print(f"\ncorrectAnswer={correctAnswer}\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\n\n\n")
                print("")
            def HintES():
                ShowHintES.config(text=f"Spanish Hint: '{hintES}'")
                self.hintUsed=1
                print(f"\ncorrectAnswer={correctAnswer}\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\n\n\n")
                print("")
            def PackHints(hintFR,hintENG,hintDE,hintES):
                if len(hintFR)>0:
                    ButtonHintFR.pack(side=LEFT)
                    ShowHintFR.pack(side=TOP)
                if len(hintENG)>0:
                    ButtonHintENG.pack(side=LEFT)
                    ShowHintENG.pack(side=TOP)
                if len(hintDE)>0:
                    ButtonHintDE.pack(side=LEFT)
                    ShowHintDE.pack(side=TOP)
                if len(hintES)>0:
                    ButtonHintES.pack(side=LEFT)
                    ShowHintES.pack(side=TOP)
            def stopAll():
                TTT.destroy()
                self.ToAdd="Stop exercise"
                return "Stop exercise"
            def RevealAnswer(*args):
                print(f"\ncorrectAnswer={correctAnswer}\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\n\n\n")
                print("")
                entree.insert(0,f"{correctAnswer}")
                self.AnswerRevealed=1
                StopButton.place_forget()
                ButtonHintENG.pack_forget()
                ButtonHintDE.pack_forget()
                ButtonHintES.pack_forget()
                ButtonHintFR.pack_forget()
                ButtonRevealAnswer.pack_forget()
                print(f"\ncorrectAnswer={correctAnswer}\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\n\n\n")
                print("")
            
            TTT = Tk()
            geometry_questions=f"{self.size_questions_x}x{self.size_questions_y+55}"
            TTT.geometry(geometry_questions)
            TTT.minsize(self.size_questions_x,self.size_questions_y+55)
            TTT['bg']=self.universalBackground
            if self.hasIcon==True:TTT.iconbitmap=self.icon
            WordLabel=Label(TTT,text=f"What is the {typeRequired} of {word}:",bg=self.universalBackground,font=self.defaultFont,anchor="w")
            WordLabel.pack(side=TOP,fill=X)
            LabelWrong=Label(TTT,text="",bg=self.universalBackground,font=self.defaultFont,anchor="center")
            LabelWrong.pack(side=TOP,fill=X)
            Frame1=Frame(TTT, borderwidth=2, relief=GROOVE)
            Frame1.pack(side=TOP, padx=30, pady=30)
            # ContentVar = StringVar()
            # ContentVar.set("oo")
            entree = Entry(Frame1, width=30)#,text=ContentVar)
            entree.pack(side=TOP,padx=10,pady=10)
            ButtonSubmit=Button(Frame1, text="Submit", command=submit)
            ButtonSubmit.pack(side=RIGHT,padx=10,pady=10)
            ButtonContinue=Button(Frame1,text="Continue",command=proceed)
            ButtonHintFR=Button(Frame1,text="French Hint",command=HintFR)
            ButtonHintENG=Button(Frame1,text="English Hint",command=HintENG)
            ButtonHintDE=Button(Frame1,text="German Hint",command=HintDE)
            ButtonHintES=Button(Frame1,text="Spanish Hint",command=HintES)
            ButtonRevealAnswer=Button(Frame1,text="Reveal Answer",command=RevealAnswer)
            ButtonRevealAnswer.pack(side=LEFT)
            ShowHintFR=Label(TTT,text="",bg=self.universalBackground)
            ShowHintENG=Label(TTT,text="",bg=self.universalBackground)
            ShowHintDE=Label(TTT,text="",bg=self.universalBackground)
            ShowHintES=Label(TTT,text="",bg=self.universalBackground)
            StopButton=Button(TTT,text="Stop exercise!",command=stopAll)
            StopButton.pack(side=TOP, fill=X,padx=5)
            PackHints(hintFR,hintENG,hintDE,hintES)
            TTT.mainloop()
        def AskTripple(self,typeRequired,word,correctAnswer,hintFR,hintENG,hintDE,hintES,WTOrTW):
            """ This function is the one in charge of gathering the user entries for the exercise."""
            self.hintUsed=0
            self.InfAnswerRevealed=0
            self.PresAnswerRevealed=0
            self.PretAnswerRevealed=0
            self.PerfAnswerRevealed=0
            self.ToAdd=0
            def submit(*args):
                if WTOrTW==0:
                    InfEntry.config(state="normal")
                    InfAnsw=InfEntry.get()
                    if len(InfAnsw)>0:
                        InfVerdict=Windows.SubOperations.gameCheck(self.hintUsed,InfAnsw,correctAnswer[0],self.InfAnswerRevealed,Block=self.ColumnsLang[self.ChosenLanguage][0])
                    else:
                        InfVerdict=["",True,f"Please enter something in the {self.ColumnsLang[self.ChosenLanguage][0]} box before pressing Submit."]
                    PresEntry.config(state="normal")
                    PresAnsw=PresEntry.get()
                    if len(InfAnsw)>0:
                        PresVerdict=Windows.SubOperations.gameCheck(self.hintUsed,PresAnsw,correctAnswer[1],self.PresAnswerRevealed,Block=self.ColumnsLang[self.ChosenLanguage][1])
                    else:
                        PresVerdict=["",True,f"Please enter something in the {self.ColumnsLang[self.ChosenLanguage][1]} box before pressing Submit."]
                    PretEntry.config(state="normal")
                    PretAnsw=PretEntry.get()
                    if len(InfAnsw)>0:
                        PretVerdict=Windows.SubOperations.gameCheck(self.hintUsed,PretAnsw,correctAnswer[2],self.PretAnswerRevealed,Block=self.ColumnsLang[self.ChosenLanguage][2])
                    else:
                        PretVerdict=["",True,f"Please enter something in the {self.ColumnsLang[self.ChosenLanguage][2]} box before pressing Submit."]
                    if self.ChosenLanguage!="EN":
                        PerfEntry.config(state="normal")
                        PerfAnsw=PerfEntry.get()
                        if len(InfAnsw)>0:
                            PerfVerdict=Windows.SubOperations.gameCheck(self.hintUsed,PerfAnsw,correctAnswer[3],self.PerfAnswerRevealed,Block=self.ColumnsLang[self.ChosenLanguage][3])
                        else:
                            PerfVerdict=["",True,f"Please enter something in the {self.ColumnsLang[self.ChosenLanguage][3]} box before pressing Submit."]

                if (InfVerdict[1]==False and PresVerdict[1]==False and PretVerdict[1]==False) or (InfVerdict[1]==False and PresVerdict[1]==False and PretVerdict[1]==False and PerfVerdict[1]==False):
                    LabelWrong.config(text=f"Correct.")
                    LabelWrong.config(font=(self.Font,self.Size,"bold"))
                    LabelWrong.config(fg=self.successColors[random.randint(0,len(self.successColors)-1)])
                    ButtonContinue.pack(side=LEFT,fill=X)

                    ButtonSubmit.pack_forget()
                    ButtonHintFR.pack_forget()
                    ButtonHintENG.pack_forget()
                    ButtonHintDE.pack_forget()
                    ButtonHintES.pack_forget()
                    ButtonRevealAnswer.pack_forget()
                    ButtonContinue.pack_configure(fill=X,side=BOTTOM)
                    StopButton.pack_forget()
                    print(f"\n\n\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\nVerdict={Verdict}\nVerdict[0]={Verdict[0]}\nVerdict[1]={Verdict[1]}\nVerdict[2]={Verdict[2]}\n\n\n")
                    self.ToAdd=InfVerdict[0]+PresVerdict[0]+PretVerdict[0]
                    if self.ChosenLanguage!="EN":
                        self.ToAdd+=PerfVerdict[0]
                    return self.ToAdd
                else:
                    if InfVerdict[2]==f"Please enter something in the {self.ColumnsLang[self.ChosenLanguage][0]} box before pressing Submit." or InfVerdict[2]==f"Wrong Answer for {self.ColumnsLang[self.ChosenLanguage][0]}, try again.":
                        LabelWrong.config(text=InfVerdict[2])
                    elif PresVerdict[2]==f"Please enter something in the {self.ColumnsLang[self.ChosenLanguage][1]} box before pressing Submit." or InfVerdict[2]==f"Wrong Answer for {self.ColumnsLang[self.ChosenLanguage][1]}, try again.":
                        LabelWrong.config(text=PresVerdict[2])
                    elif PretVerdict[2]==f"Please enter something in the {self.ColumnsLang[self.ChosenLanguage][2]} box before pressing Submit." or InfVerdict[2]==f"Wrong Answer for {self.ColumnsLang[self.ChosenLanguage][2]}, try again.":
                        LabelWrong.config(text=PretVerdict[2])
                    elif PerfVerdict[2]==f"Please enter something in the {self.ColumnsLang[self.ChosenLanguage][3]} box before pressing Submit." or InfVerdict[2]==f"Wrong Answer for {self.ColumnsLang[self.ChosenLanguage][3]}, try again.":
                        LabelWrong.config(PerfVerdict[2])
                    else:
                        LabelWrong.config(text='Please Make sure you have entered ')
                    LabelWrong.config(font=(self.Font,self.Size,"bold"))
                    LabelWrong.config(fg=self.errorColors[random.randint(0,len(self.errorColors)-1)])
                print(f"\n\n\nGivenAnswer='{GivenAnswer}'\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\nVerdict={Verdict}\n\n\n")
                print("")
            def proceed():
                TTT.destroy()
            def HintFR():
                ShowHintFR.config(text=f"French Hint: '{hintFR}'")
                self.hintUsed=1
                print(f"\ncorrectAnswer={correctAnswer}\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\n\n\n")
                print("")
            def HintENG():
                ShowHintENG.config(text=f"English Hint: '{hintENG}'")
                self.hintUsed=1
                print(f"\ncorrectAnswer={correctAnswer}\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\n\n\n")
                print("")
            def HintDE():
                ShowHintDE.config(text=f"German Hint: '{hintDE}'")
                self.hintUsed=1
                print(f"\ncorrectAnswer={correctAnswer}\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\n\n\n")
                print("")
            def HintES():
                ShowHintES.config(text=f"Spanish Hint: '{hintES}'")
                self.hintUsed=1
                print(f"\ncorrectAnswer={correctAnswer}\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\n\n\n")
                print("")
            def PackHints(hintFR,hintENG,hintDE,hintES):
                if len(hintFR)>0:
                    ButtonHintFR.pack(side=LEFT)
                    ShowHintFR.pack(side=TOP)
                if len(hintENG)>0:
                    ButtonHintENG.pack(side=LEFT)
                    ShowHintENG.pack(side=TOP)
                if len(hintDE)>0:
                    ButtonHintDE.pack(side=LEFT)
                    ShowHintDE.pack(side=TOP)
                if len(hintES)>0:
                    ButtonHintES.pack(side=LEFT)
                    ShowHintES.pack(side=TOP)
            def stopAll():
                TTT.destroy()
                self.ToAdd="Stop exercise"
                return "Stop exercise"
            def RevealAnswer(*args):
                print(f"\ncorrectAnswer={correctAnswer}\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\n\n\n")
                print("")
                entree.insert(0,f"{correctAnswer}")
                self.AnswerRevealed=1
                StopButton.place_forget()
                ButtonHintENG.pack_forget()
                ButtonHintDE.pack_forget()
                ButtonHintES.pack_forget()
                ButtonHintFR.pack_forget()
                ButtonRevealAnswer.pack_forget()
                print(f"\ncorrectAnswer={correctAnswer}\nself.hintUsed={self.hintUsed}\nself.AnswerRevealed={self.AnswerRevealed}\ncorrectAnswer={correctAnswer}\n\n\n")
                print("")
            def RevealAnswerInf(*args):
                InfEntry.insert(0,f"{correctInfAnswer}")
                InfEntry.config(state="disabled")
                self.InfAnswerRevealed=1
            def RevealAnswerPres(*args):
                PresEntry.insert(0,f"{correctPresAnswer}")
                PresEntry.config(state="disabled")
                self.PresAnswerRevealed=1
            def RevealAnswerPret(*args):
                PretEntry.insert(0,f"{correctPretAnswer}")
                PretEntry.config(state="disabled")
                self.PretAnswerRevealed=1
            def RevealAnswerPerf(*args):
                PerfEntry.insert(0,f"{correctPerfAnswer}")
                PerfEntry.config(state="disabled")
                self.PerfAnswerRevealed=1     
               
            TTT = Tk()
            geometry_questions=f"{self.size_questions_x}x{self.size_questions_y+55}"
            TTT.geometry(geometry_questions)
            TTT.minsize(self.size_questions_x,self.size_questions_y+55)
            TTT['bg']=self.universalBackground
            if self.hasIcon==True:TTT.iconbitmap=self.icon
            WordLabel=Label(TTT,text=f"What is the {typeRequired} of {word}:",bg=self.universalBackground,font=self.defaultFont,anchor="w")
            WordLabel.pack(side=TOP,fill=X)
            LabelWrong=Label(TTT,text="",bg=self.universalBackground,font=self.defaultFont,anchor="center")
            LabelWrong.pack(side=TOP,fill=X)
            Frame1=Frame(TTT, borderwidth=2, relief=GROOVE)
            Frame1.pack(side=TOP, padx=30, pady=30)
            if WTOrTW==0:
                subFrameTOP=Frame(Frame1, borderwidth=2, relief=FLAT)
                subFrameTOP.pack(side=TOP, padx=0, pady=0,fill=X)
                subFrameMID=Frame(Frame1, borderwidth=2, relief=FLAT)
                subFrameMID.pack(side=TOP, padx=0, pady=0,fill=X)
                subFrameBOTTOM=Frame(Frame1, borderwidth=2, relief=FLAT,bg=self.universalBackground)
                subFrameBOTTOM.pack(side=TOP, padx=0, pady=0,fill=X)
                
                InfLabel=Label(subFrameTOP,text=f"{self.ColumnsLang[self.ChosenLanguage][0]}",bg=self.universalBackground,fg=self.universalForeground,font=self.defaultFont)
                InfLabel.pack(side=LEFT,padx=15)
                InfEntry=Entry(subFrameMID, width=30)#,text=ContentVar)
                InfEntry.pack(side=LEFT,padx=10,pady=10)
                ButtonInfRevAns=Button(subFrameBOTTOM,text=f"Reveal {self.ColumnsLang[self.ChosenLanguage][0]}",command=RevealAnswerInf,fg=self.universalForeground,bg=self.universalBackground)
                ButtonInfRevAns.pack(side=LEFT)
                
                PresLabel=Label(subFrameTOP,text=f"{self.ColumnsLang[self.ChosenLanguage][1]}",bg=self.universalBackground,fg=self.universalForeground,font=self.defaultFont)
                PresLabel.pack(side=LEFT,padx=15)
                PresEntry=Entry(subFrameMID, width=30)#,text=ContentVar)
                PresEntry.pack(side=LEFT,padx=10,pady=10)
                ButtonPresRevAns=Button(subFrameBOTTOM,text=f"Reveal {self.ColumnsLang[self.ChosenLanguage][1]}",command=RevealAnswerPres,fg=self.universalForeground,bg=self.universalBackground)
                ButtonPresRevAns.pack(side=LEFT)
                
                PretLabel=Label(subFrameTOP,text=f"{self.ColumnsLang[self.ChosenLanguage][2]}",bg=self.universalBackground,fg=self.universalForeground,font=self.defaultFont)
                PretLabel.pack(side=LEFT,padx=15)
                PretEntry=Entry(subFrameMID, width=30)#,text=ContentVar)
                PretEntry.pack(side=LEFT,padx=10,pady=10)
                ButtonPretRevAns=Button(subFrameBOTTOM,text=f"Reveal {self.ColumnsLang[self.ChosenLanguage][2]}",command=RevealAnswerPret,fg=self.universalForeground,bg=self.universalBackground)
                ButtonPretRevAns.pack(side=LEFT)
                
                if self.ChosenLanguage!="EN":
                    PerfLabel=Label(subFrameTOP,text=f"{self.ColumnsLang[self.ChosenLanguage][3]}",bg=self.universalBackground,fg=self.universalForeground,font=self.defaultFont)
                    PerfLabel.pack(side=LEFT,padx=3)
                    PerfEntry=Entry(subFrameMID, width=30)#,text=ContentVar)
                    PerfEntry.pack(side=LEFT,padx=10,pady=10)
                    ButtonPerfRevAns=Button(subFrameBOTTOM,text=f"Reveal {self.ColumnsLang[self.ChosenLanguage][3]}",command=RevealAnswerPerf,fg=self.universalForeground,bg=self.universalBackground)
                    ButtonPerfRevAns.pack(side=LEFT)
            else:
                # ContentVar = StringVar()
                # ContentVar.set("oo")
                entree = Entry(Frame1, width=30)#,text=ContentVar)
                entree.pack(side=TOP,padx=10,pady=10)
            ButtonSubmit=Button(Frame1, text="Submit", command=submit)
            ButtonSubmit.pack(side=RIGHT,padx=10,pady=10)
            ButtonContinue=Button(Frame1,text="Continue",command=proceed)
            ButtonHintFR=Button(Frame1,text="French Hint",command=HintFR)
            ButtonHintENG=Button(Frame1,text="English Hint",command=HintENG)
            ButtonHintDE=Button(Frame1,text="German Hint",command=HintDE)
            ButtonHintES=Button(Frame1,text="Spanish Hint",command=HintES)
            ButtonRevealAnswer=Button(Frame1,text="Reveal Answer",command=RevealAnswer)
            ButtonRevealAnswer.pack(side=LEFT)
            ShowHintFR=Label(TTT,text="",bg=self.universalBackground)
            ShowHintENG=Label(TTT,text="",bg=self.universalBackground)
            ShowHintDE=Label(TTT,text="",bg=self.universalBackground)
            ShowHintES=Label(TTT,text="",bg=self.universalBackground)
            StopButton=Button(TTT,text="Stop exercise!",command=stopAll)
            StopButton.pack(side=TOP, fill=X,padx=5)
            PackHints(hintFR,hintENG,hintDE,hintES)
            TTT.mainloop()
    def Home(self):
        """The main screen"""
        main=[self.EN,self.DE,self.ES,self.FR]
        sub_main=["EN","DE","ES","FR"]
        for i in range(len(main)):
            if len(main[i])>0:
                self.enableOrDisable[sub_main[i]]="normal"
        def Language():
            """ Language """
            Windows.Language(self)
        def goodbye():
            """ Quit """
            TT.destroy()
            Windows.goodbye(self)
        def WD():
            """ Words then the definition """
            TT.destroy()
            exercise="Words then the definition"
            Windows.SubOperations.DoubleTermCall(self,exercise,TDOrDT=0)
            Windows.Home(self)
        def DW():
            """ Definition then the words """
            TT.destroy()
            exercise="Definition then the words"
            Windows.SubOperations.DoubleTermCall(self,exercise,TDOrDT=1)
            Windows.Home(self)
        def WT():
            """ Words then their tenses """
            TT.destroy()
            exercise="Words then their tenses"
            Windows.SubOperations.TrippleTermCall(self,exercise,WTOrTW=0)
            Windows.Home(self)
        def TW():
            """ Tenses then the words """
            TT.destroy()
            exercise="Tenses then the words"
            Windows.SubOperations.DoubleTermCall(self,exercise,TDOrDT=1)
            Windows.Home(self)
        def WTD():
            """ Words, tenses then definition """
            Windows.WTD(self)
        def WDT():
            """ Words, definition then tenses """
            Windows.WDT(self)
        def TWD():
            """ Tenses, words then defintion """
            Windows.TWD(self)
        def TDW():
            """ Tenses, definition then words """
            Windows.TDW(self)
        def DTW():
            """ Definition, tenses then words """
            # Windows.DTW(self)
        def DWT():
            """ Definition, words then tenses """
            # Windows.DWT(self)
        def V():
            """ Verbs """
            # Windows.V(self)
        def OST():
            """ Of a specific tense """
            # Windows.OST(self)
        def OAT():
            """ Of all the tenses """
            # Windows.OAT(self)
        def ET():
            """ English translation """
            # Windows.ET(self)
        def FT():
            """ French translation """
            # Windows.FT(self)
        def WCLT():
            """ The words and the chosen language for the translation """
            # Windows.WCLT(self)
        def EVE():
            """ Everything """
            # Windows.EVE(self)
        def Author():
            """ The author """
            Windows.Author(self)
        def Watermarks():
            """ My Watermarks """
            Windows.Watermarks(self)
        def Score():
            """ You're score"""
            Windows.Score(self)
        def TS():
            """ Time spent """
            Windows.TS(self)
        def COS():
            """ Current OS """
            Windows.COS(self)
        def HELPERS():
            """ Helpers """
            Windows.HELPERS(self)
        def HT():
            """ How to """
            Windows.HT(self)
        def HID():
            """ Hidden """
            Windows.HID(self)
        def AS():
            """ All the sounds """
            Windows.AS(self)
        def Ss():
            """ Specific sound """
            Windows.Ss(self)
        def FS():
            """ Where to find the sounds """
            Windows.FS(self)
        def AV():
            """ All the videos """
            Windows.AV(self)
        def SV():
            """ Specific video """
            Windows.SV(self)
        def FV():
            """ Where to find the videos """
            Windows.FV(self)
        def updateRadio(*args):
            e=int(value.get())
            print(f"e={e},type(e)={type(e)}")
            if e==1:
                self.ChosenLanguage="EN"
                self.ContentLanguage=self.EN
                self.ListLength=len(self.ChosenLanguage)-1
            elif e==2:
                self.ChosenLanguage="DE"
                self.ContentLanguage=self.DE
                self.ListLength=len(self.ChosenLanguage)-1
            elif e==3:
                self.ChosenLanguage="ES"
                self.ContentLanguage=self.ES
                self.ListLength=len(self.ChosenLanguage)-1
            else:
                self.ChosenLanguage="FR"
                self.ContentLanguage=self.FR
                self.ListLength=len(self.ChosenLanguage)-1
            print(f"Chosen Langauge={self.ChosenLanguage}")
        def updateGameMethod(*args):
            method=MethValue.get()
            if method==1:
                self.PMethod="written"
            else:
                self.PMethod="radio"
        def setRadioLanguage():
            if self.ChosenLanguage=="EN":
                return 1
            elif self.ChosenLanguage=="DE":
                return 2
            elif self.ChosenLanguage=="ES":
                return 3
            else:
                return 4
        def setRadioWrittenOrRadio():
            if self.PMethod=="written":
                return 1
            else:
                return 2
    
        TT = Tk()
        TT["bg"]=self.universalBackground
        TT.title("Main Menu - Language")
        TT.geometry(self.geometry)
        TT.minsize(self.size_x,self.size_y)
        if self.hasIcon==True:TT.iconbitmap=self.icon
        TT.config(background="#00b8bb")
        menubar = Menu(TT)

        menu0 = Menu(menubar, tearoff=0)
        menu0.add_command(label="Language", command=Language)
        menu0.add_separator()
        menu0.add_command(label="Quit", command=goodbye)
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
        menu3.add_command(label="Tenses, words then definition", command=TWD)
        menu3.add_command(label="Tenses, definition then words", command=TDW)
        menu3.add_command(label="Definition, tenses then words", command=DTW)
        menu3.add_command(label="Definition, words then tenses", command=DWT)
        menubar.add_cascade(label="Words, Tenses & definition", menu=menu3)


        menu4 = Menu(menubar, tearoff=0)
        menu4.add_command(label="Verbs", command=V)
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

        TT.config(menu=menubar)
        # Test=Label(TT,text="test0",bg=self.universalBackground)#,anchor="center")
        # Test.pack(side=TOP,padx=10,pady=10)
        FrameContentMenu=Frame(TT,bg=self.universalBackground,padx=0,pady=10)
        FrameContentMenu.pack(fill=BOTH)
        Title=Label(FrameContentMenu,text="Welcome to the program Learn irregular verbs",bg=self.universalForeground,fg=self.universalBackground,font=(self.Font,self.Size+10,"bold"))#,anchor="center")
        Title.pack(side=TOP,fill=X,padx=10,pady=10)
        Hint=Label(FrameContentMenu,text="HowTo",bg=self.universalBackground,font=(self.Font,self.Size,"bold"))#,anchor="center")
        Hint.pack(side=TOP,fill=X,padx=10,pady=10)
        WriteOrRadioLanguage=Frame(FrameContentMenu,bg=self.universalBackground,padx=0,pady=10)
        WriteOrRadioLanguage.pack(fill=X,side=RIGHT,padx=self.innerPadding,pady=0)
        MethValue = StringVar()
        MethValue.set(setRadioWrittenOrRadio())
        buttonWrite = Radiobutton(WriteOrRadioLanguage, text="Written", variable=MethValue, value=1,bg=self.universalBackground,font=self.defaultFont,command=updateGameMethod,state=self.enableOrDisable["written"])
        buttonRadio = Radiobutton(WriteOrRadioLanguage, text="Radio choice", variable=MethValue, value=2,bg=self.universalBackground,font=self.defaultFont,command=updateGameMethod,state=self.enableOrDisable["radio"])
        buttonRadio.pack(fill=X,side=RIGHT)
        buttonWrite.pack(fill=X,side=RIGHT)
        Hint1=Label(FrameContentMenu,text="1. Chose the language you wish to study.",bg=self.universalBackground,font=self.defaultFont,anchor="w")
        Hint1.pack(side=TOP,fill=X,padx=self.innerPadding,pady=5)
        FrameLanguage=Frame(FrameContentMenu,bg=self.universalBackground,padx=0,pady=10)
        FrameLanguage.pack(fill=X,side=TOP,padx=self.innerPadding,pady=0)
        value = StringVar()
        value.set(setRadioLanguage())
        buttonEnglish = Radiobutton(FrameLanguage, text="English", variable=value, value=1,bg=self.universalBackground,font=self.defaultFont,command=updateRadio,state=self.enableOrDisable["EN"])
        buttonGerman = Radiobutton(FrameLanguage, text="German", variable=value, value=2,bg=self.universalBackground,font=self.defaultFont,command=updateRadio,state=self.enableOrDisable["DE"])
        buttonSpanish = Radiobutton(FrameLanguage, text="Spanish", variable=value, value=3,bg=self.universalBackground,font=self.defaultFont,command=updateRadio,state=self.enableOrDisable["ES"])
        buttonFrench = Radiobutton(FrameLanguage, text="French", variable=value, value=4,bg=self.universalBackground,font=self.defaultFont,command=updateRadio,state=self.enableOrDisable["FR"])
        buttonEnglish.pack(fill=X,side=LEFT)
        buttonGerman.pack(fill=X,side=LEFT)
        buttonSpanish.pack(fill=X,side=LEFT)
        buttonFrench.pack(fill=X,side=LEFT)
        Hint2=Label(FrameContentMenu,text="2. Chose the method you wish to use to study",bg=self.universalBackground,font=self.defaultFont,anchor="w")
        Hint2.pack(side=TOP,fill=X,padx=self.innerPadding,pady=5)
        FrameMethod=Frame(FrameContentMenu,bg=self.universalBackground,padx=10,pady=10)
        FrameMethod.pack(fill=X,padx=self.innerPadding,pady=0)
        ButtonWD=Button(FrameMethod,text="Words then the definition",bg=self.universalBackground,command=WD)
        ButtonWD.pack(side=LEFT,padx=0,pady=0)
        ButtonWT=Button(FrameMethod,text="Words then their tenses",bg=self.universalBackground,command=WT)
        ButtonWT.pack(side=LEFT,padx=0,pady=0)
        ButtonWTD=Button(FrameMethod,text="Words, tenses then definition",bg=self.universalBackground,command=WTD)
        ButtonWTD.pack(side=LEFT,padx=0,pady=0)
        Hint3=Label(FrameContentMenu,text="3. Check the menu for more training options.",bg=self.universalBackground,font=self.defaultFont,anchor="w")
        Hint3.pack(side=TOP,fill=X,padx=self.innerPadding,pady=5)
        FrameQuit=Frame(TT,bg="#00b8bb",padx=10,pady=0)
        FrameQuit.pack(fill=X)
        ButtonQuit=Button(FrameQuit,text="Quit",anchor="w",font=self.defaultFont,command=goodbye)
        ButtonQuit.pack(side=RIGHT,padx=5,pady=5)
        Watermark=Label(FrameQuit,text=self.watermark,bg=self.universalBackground,font=self.defaultFont)
        Watermark.pack(side=LEFT,padx=5,pady=0)

        TT.mainloop()
    def Language(self):
        """Choose the language and adjust other settings."""
        def setRadioLanguage():
            if self.ChosenLanguage=="EN":
                return 1
            elif self.ChosenLanguage=="DE":
                return 2
            elif self.ChosenLanguage=="ES":
                return 3
            else:
                return 4
        def setRadioWrittenOrRadio():
            if self.PMethod=="written":
                return 1
            else:
                return 2
        def setVoicePreference():
            if self.VoiceType=="Female":
                return 1
            else:
                return 2
        def getRadioLanguage(*args):
            e=int(value.get())
            print(f"e={e},type(e)={type(e)}")
            if e==1:
                self.ChosenLanguage="EN"
                self.ContentLanguage=self.EN
                self.ListLength=len(self.ChosenLanguage)-1
            elif e==2:
                self.ChosenLanguage="DE"
                self.ContentLanguage=self.DE
                self.ListLength=len(self.ChosenLanguage)-1
            elif e==3:
                self.ChosenLanguage="ES"
                self.ContentLanguage=self.ES
                self.ListLength=len(self.ChosenLanguage)-1
            else:
                self.ChosenLanguage="FR"
                self.ContentLanguage=self.FR
                self.ListLength=len(self.ChosenLanguage)-1
            print(f"Chosen Langauge={self.ChosenLanguage}")
        def updateGameMethod(*args):
            method=MethValue.get()
            if method==1:
                self.PMethod="written"
            else:
                self.PMethod="radio"
        def updateVoicePreference(*args):
            preference=VoiceValue.get()
            if preference==1:
                self.VoiceType="Female"
            else:
                self.VoiceType="Male"
        TTT=Tk()
        geometry_questions=f"{self.size_questions_x}x{self.size_questions_y+15}"
        TTT.geometry(geometry_questions)
        TTT.minsize(self.size_questions_x,self.size_questions_y+15)
        TTT.title("Select the language")
        TTT['bg']=self.universalBackground
        if self.hasIcon==True:TTT.iconbitmap=self.icon
        TitleLabel=Label(TTT,text="Settings for the language & Co.",fg=self.universalBackground,bg=self.universalForeground,font=(self.Font,self.Size+10,"bold"),anchor="center")
        TitleLabel.pack(side=TOP,fill=X)
        FrameMain=Frame(TTT,bg=self.universalBackground,relief=FLAT,borderwidth=0)
        FrameMain.pack(side=TOP,fill=X)
        # LanguageLabel=Label(FrameMain,text="Choose the language you wish to study.",fg=self.universalForeground,bg=self.universalBackground,font=self.defaultFont,anchor="nw")
        # LanguageLabel.pack(side=TOP,fill=X)
        FrameLanguage=LabelFrame(FrameMain,text="Choose the language you wish to study.",fg=self.universalForeground,font=self.defaultFont,bg=self.universalBackground,padx=0,pady=5)
        FrameLanguage.pack(fill=X,side=TOP,padx=self.innerPadding,pady=0)
        value = StringVar()
        value.set(setRadioLanguage())
        buttonEnglish = Radiobutton(FrameLanguage, text="English", variable=value, value=1,bg=self.universalBackground,font=self.defaultFont,command=getRadioLanguage,state=self.enableOrDisable["EN"])
        buttonGerman = Radiobutton(FrameLanguage, text="German", variable=value, value=2,bg=self.universalBackground,font=self.defaultFont,command=getRadioLanguage,state=self.enableOrDisable["DE"])
        buttonSpanish = Radiobutton(FrameLanguage, text="Spanish", variable=value, value=3,bg=self.universalBackground,font=self.defaultFont,command=getRadioLanguage,state=self.enableOrDisable["ES"])
        buttonFrench = Radiobutton(FrameLanguage, text="French", variable=value, value=4,bg=self.universalBackground,font=self.defaultFont,command=getRadioLanguage,state=self.enableOrDisable["FR"])
        buttonEnglish.pack(fill=X,side=LEFT)
        buttonGerman.pack(fill=X,side=LEFT)
        buttonSpanish.pack(fill=X,side=LEFT)
        buttonFrench.pack(fill=X,side=LEFT)
        WriteOrRadioLanguage=LabelFrame(FrameMain,text="Do you wish to write the words or choose from a list.",fg=self.universalForeground,font=self.defaultFont,bg=self.universalBackground,padx=0,pady=0)
        WriteOrRadioLanguage.pack(fill=None,side=RIGHT,padx=self.innerPadding,pady=0)
        MethValue = StringVar()
        MethValue.set(setRadioWrittenOrRadio())
        buttonWrite = Radiobutton(WriteOrRadioLanguage, text="Written", variable=MethValue, value=1,bg=self.universalBackground,font=self.defaultFont,command=updateGameMethod,state=self.enableOrDisable["written"])
        buttonRadio = Radiobutton(WriteOrRadioLanguage, text="Radio choice", variable=MethValue, value=2,bg=self.universalBackground,font=self.defaultFont,command=updateGameMethod,state=self.enableOrDisable["radio"])
        buttonRadio.pack(fill=X,side=RIGHT)
        buttonWrite.pack(fill=X,side=RIGHT)
        # TitleVoicePreferenceLabel=Label(FrameMain,text="Choose your the voice of the person reading.",bg=self.universalBackground,fg=self.universalForeground,font=self.defaultFont,anchor="nw")
        # TitleVoicePreferenceLabel.pack(side=TOP,fill=X)
        VoicePreference=LabelFrame(FrameMain,text="Choose your narrators voice:",fg=self.universalForeground,bg=self.universalBackground,padx=0,pady=5)
        VoicePreference.pack(fill=None,side=LEFT,padx=self.innerPadding,pady=0)
        VoiceValue = StringVar()
        VoiceValue.set(setVoicePreference())
        buttonFemale = Radiobutton(VoicePreference, text="Female", variable=VoiceValue, value=1,bg=self.universalBackground,font=self.defaultFont,command=updateVoicePreference,state=self.enableOrDisable["female"])
        buttonMale = Radiobutton(VoicePreference, text="Male", variable=VoiceValue, value=2,bg=self.universalBackground,font=self.defaultFont,command=updateVoicePreference,state=self.enableOrDisable["male"])
        buttonFemale.pack(fill=X,side=LEFT)
        buttonMale.pack(fill=X,side=LEFT)
        ButtonClose=Button(TTT,text="Close",fg=self.universalForeground,bg=self.universalBackground,font=self.defaultFont,command=TTT.destroy)
        ButtonClose.pack(side=RIGHT,padx=5)
        WatermarkLabel=Label(TTT,text=self.watermark,fg=self.universalForeground,bg=self.universalBackground,font=self.defaultFont)
        WatermarkLabel.pack(side=LEFT,padx=5)
        TTT.mainloop()
    def DW(self):
        print("ee")
    def WT(self):
        print("ee")
    def TW(self):
        print("ee")
    def WTD(self):
        print("ee")
    def WDT(self):
        print("ee")
    def TWD(self):
        print("ee")
    def TDW(self):
        print("ee")
    def Author(self):
        print("hi")
    def Watermarks(self):
        print("hi")
    def Score(self):
        print("hi")
    def TS(self):
        print("hi")
    def COS(self):
        print("hi")
    def HELPERS(self):
        print("hi")
    def HT(self):
        print("hi")
    def HID(self):
        print("hi")
    def AS(self):
        print("hi")
    def Ss(self):
        print("hi")
    def FS(self):
        print("hi")
    def AV(self):
        print("hi")
    def SV(self):
        print("hi")
    def FV(self):
        print("hi")
    def TS(self):
        print("hi")                #index   ToAdd
    def SaveProgress(self,language,progress,score,exercise,time_start,time_end,total_time=0):
        """This will save the users progress for a given exercise"""
        def SaveTheProgress():
            if os.path.exists(self.ProgressFolder)==False:
                os.mkdir(self.ProgressFolder)
            f=open(f"{self.ProgressFolder}/{self.username}_{language}_{exercise}.save","w")
            f.write(f"{language}\n{exercise}\n{progress}\n{score}\n{d}\n{mo}\n{y}\n{h}\n{minute}\n{s}\n{ms}\n{time_start}\n{time_end}\n")
            if total_time==0:
                f.write(f"{time_start}\n")
                self.first_time_started=time_start
            else:
                f.write(f"{total_time['first_time_started']}\n")
            f.close()
            def CloseBoth():
                Saved.destroy()
                Progress.destroy()
            Saved=Tk()
            Saved.geometry(self.geometry_small_window)
            Saved.minsize(self.size_small_window_x,self.size_small_window_y)
            if self.hasIcon==True:Saved.iconbitmap=self.icon
            Saved.title("Saved")
            SavedLabel=Label(Saved,text="Progress Saved",bg=self.universalBackground,fg=self.universalForeground,font=self.defaultFont,anchor="center")
            SavedLabel.pack(side=TOP, fill=X)
            SavedButton=Button(Saved,text="OK!",bg=self.universalBackground,fg=self.universalForeground,font=self.defaultFont,anchor="center",command=CloseBoth)
            SavedButton.pack(side=TOP,fill=X)
            Saved.mainloop()
        def DiscardTheProgress():
            Progress.destroy()
        timeInfo=Windows.SubOperations.splitTime(self,Start_time=time_start,Stop_time=time_end,total_time=total_time)
        d=timeInfo["d"]
        mo=timeInfo["mo"]
        y=timeInfo["y"]
        h=timeInfo["h"]
        minute=timeInfo["minute"]
        s=timeInfo["s"]
        ms=timeInfo["ms"]
        p=timeInfo["p"] #dictionnary
        print(f"d={d},mo={mo},y={y},h={h},minute={minute},s={s},ms={ms},p={p},type({d})={type(d)},type({mo})={type(mo)},type({y})={type(y)},type({h})={type(h)},type({minute})={type(minute)},type({s})={type(s)},type({ms})={type(ms)},type({p})={type(p)}")

        

        Progress=Tk()
        Progress.geometry(self.geometry_stat_windows)
        Progress.minsize(self.size_stat_windows_x,self.size_stat_windows_y)
        if self.hasIcon==True:Progress.iconbitmap=self.icon
        Progress.title("Save Progress?")
        Progress['bg']=self.universalBackground
        TitleLabel=Label(Progress,text="Do you wish to save your progress?",bg=self.universalForeground,fg=self.universalBackground,font=self.defaultFont,anchor="center")
        TitleLabel.pack(side=TOP,fill=X)
        FrameOptions=Frame(Progress,bg=self.universalBackground,relief=FLAT,borderwidth=0)
        FrameOptions.pack(side=TOP,fill=BOTH)
        ButtonYes=Button(FrameOptions,text="Yes",bg=self.universalBackground,fg=self.universalForeground,command=SaveTheProgress,anchor="center",font=self.defaultFont)
        ButtonYes.pack(side=TOP,fill=BOTH,pady=5)
        ButtonNo=Button(FrameOptions,text="No",bg=self.universalBackground,fg=self.universalForeground,command=DiscardTheProgress,anchor="center",font=self.defaultFont)
        ButtonNo.pack(side=BOTTOM,fill=BOTH,pady=5)
        InfoLabel=Label(Progress,text=f"For the language '{language}'.\nYour score is {score}/{self.ListLength*2} points.\nAnd your progress is {progress}/{self.ListLength} questions in a total of\n {y} year{p['yp']}, {mo} month{p['mop']}, {d} day{p['dp']}, {h} hour{p['hp']}, {minute} minute{p['minutep']} {s} second{p['sp']}, {ms} millisecond{p['msp']}",bg=self.universalForeground,fg=self.universalBackground,font=self.defaultFont,anchor="center")
        InfoLabel.pack(side=TOP,fill=X)
        Progress.mainloop()

    def RestoreProgress(self,language,exercise):
        """If save file found for a specific user and exercise, it will give the choice to the user if he wishes to restore the saved file or not."""
        def RestoreTheProgress():
            def CloseBoth():
                Saved.destroy()
                Progress.destroy()
                self.first_time_started=timeInfoRestore["first_time_started"]
            Saved=Tk()
            Saved.geometry(self.geometry_small_window)
            Saved.minsize(self.size_small_window_x,self.size_small_window_y)
            if self.hasIcon==True:Saved.iconbitmap=self.icon
            Saved.title("Restored")
            SavedLabel=Label(Saved,text="Progress Restored",bg=self.universalBackground,fg=self.universalForeground,font=self.defaultFont,anchor="center")
            SavedLabel.pack(side=TOP, fill=X)
            SavedButton=Button(Saved,text="OK!",bg=self.universalBackground,fg=self.universalForeground,font=self.defaultFont,anchor="center",command=CloseBoth)
            SavedButton.pack(side=TOP,fill=X)
            Saved.mainloop()
            self.timeInfoRestore=timeInfoRestore
        def DiscardTheProgress():
            Progress.destroy()
            os.remove(f"{self.ProgressFolder}/{self.username}_{language}_{exercise}.save")
            self.timeInfoRestore=0
            update.date()
            self.first_time_started=self.Alls
            return 0
        try:
            if os.path.exists(self.ProgressFolder)==False:
                self.timeInfoRestore=0
                return 0
            f=open(f"{self.ProgressFolder}/{self.username}_{language}_{exercise}.save","r")
            Content=f.read()#{language}\n{exercise}\n{progress}\n{score}\n{d}\n{mo}\n{y}\n{h}\n{minute}\n{s}\n{ms}\n{time_start}\n{time_end}\n
            f.close()
            Content=Content.split("\n")
            ToPlace=["language","exercise","progress","score","d","mo","y","h","minute","s","ms","time_start","time_end","first_time_started"]
            timeInfoRestore={}
            for i in range(len(ToPlace)):
                try: 
                    Content[i]=int(Content[i])
                except:
                    pass
                timeInfoRestore[ToPlace[i]]=Content[i]
            timeInfoRestore["index"]=timeInfoRestore["progress"]
        except:
            self.timeInfoRestore=0
            return 0
        print(f"timeInfo={timeInfoRestore}\n")
        timeInfo=Windows.SubOperations.splitTime(self,Start_time=timeInfoRestore["time_start"],Stop_time=timeInfoRestore["time_end"])
        p=timeInfo["p"]
        Progress=Tk()
        Progress.geometry(self.geometry_stat_windows)
        Progress.minsize(self.size_stat_windows_x,self.size_stat_windows_y)
        if self.hasIcon==True:Progress.iconbitmap=self.icon
        Progress.title("Restore Progress?")
        Progress['bg']=self.universalBackground
        TitleLabel=Label(Progress,text="Do you wish to restore your progress for this exercise?",bg=self.universalForeground,fg=self.universalBackground,font=self.defaultFont,anchor="center")
        TitleLabel.pack(side=TOP,fill=X)
        FrameOptions=Frame(Progress,bg=self.universalBackground,relief=FLAT,borderwidth=0)
        FrameOptions.pack(side=TOP,fill=BOTH)
        ButtonYes=Button(FrameOptions,text="Yes",bg=self.universalBackground,fg=self.universalForeground,command=RestoreTheProgress,anchor="center",font=self.defaultFont)
        ButtonYes.pack(side=TOP,fill=BOTH,pady=5)
        ButtonNo=Button(FrameOptions,text="No",bg=self.universalBackground,fg=self.universalForeground,command=DiscardTheProgress,anchor="center",font=self.defaultFont)
        ButtonNo.pack(side=BOTTOM,fill=BOTH,pady=5)
        InfoLabel=Label(Progress,text=f"For the language '{timeInfoRestore['language']}'.\nYour score is {timeInfoRestore['score']}/{self.ListLength*2} points.\nAnd your progress is {timeInfoRestore['progress']}/{self.ListLength} questions in a total of\n {timeInfoRestore['y']} year{p['yp']}, {timeInfoRestore['mo']} month{p['mop']}, {timeInfoRestore['d']} day{p['dp']}, {timeInfoRestore['h']} hour{p['hp']}, {timeInfoRestore['minute']} minute{p['minutep']} {timeInfoRestore['s']} second{p['sp']}, {timeInfoRestore['ms']} millisecond{p['msp']}.",bg=self.universalForeground,fg=self.universalBackground,font=self.defaultFont,anchor="center")
        InfoLabel.pack(side=TOP,fill=X)
        Progress.mainloop()

    def goodbye(self):
        TT=Tk()
        TT.geometry(self.geometry_small_window)
        TT.minsize(self.size_small_window_x,self.size_small_window_y)
        if self.hasIcon==True:TT.iconbitmap=self.icon
        TT["bg"]=self.universalBackground
        Go=Label(TT,text="Goodbye",anchor="center",bg=self.universalBackground)
        Go.pack(fill=X)
        bu=Button(TT,text="Close",command=TT.destroy,anchor="center")
        bu.pack(fill=X)
        TT.mainloop()
    def ScoreBoard(self,score,answ_questions,tot_questions,exercise,time_start,time_stop,total_time=0):
        """Displays a few stats about the user for a given module."""
        print("################################################################################################################################################################################")
        print(f"score={score},answ_questions={answ_questions},tot_questions={tot_questions},exercise={exercise},time_start={time_start},time_stop={time_stop}")
        print("################################################################################################################################################################################")
        timeInfo=Windows.SubOperations.splitTime(self,Start_time=time_start,Stop_time=time_stop,total_time=total_time)
        if total_time!=0:
            time_start=total_time["time_start"]
        d=timeInfo["d"]
        mo=timeInfo["mo"]
        y=timeInfo["y"]
        h=timeInfo["h"]
        minute=timeInfo["minute"]
        s=timeInfo["s"]
        ms=timeInfo["ms"]
        p=timeInfo["p"]
            
        TS=Tk()
        TS.geometry(self.geometry_stat_windows)
        TS.minsize(self.size_stat_windows_x,self.size_stat_windows_y)
        if self.hasIcon==True:TS.iconbitmap=self.icon
        TS['bg']=self.universalBackground
        TS.title("Results")
        LabelTitle=Label(TS,text="The Results",bg=self.universalForeground,fg=self.universalBackground)
        LabelTitle.pack(side=TOP,fill=X)
        LabelScore=Label(TS,text=f"Your score is {score}/{(answ_questions*2)} for the exercise {exercise}.",bg=self.universalBackground)
        LabelScore.pack(side=TOP,fill=X)
        aqp=""
        if answ_questions>1:
            aqp="s"
        tqp=""
        if tot_questions>1:
            tqp="s"
        LabelQuestions=Label(TS,text=f"You have answered {answ_questions} question{aqp} out of {tot_questions} question{tqp} for the exercise {exercise}.",bg=self.universalBackground)
        LabelQuestions.pack(side=TOP,fill=X)
        LabelToTimeUsed=Label(TS,text=f"You took {y} year{p['yp']}, {mo} month{p['mop']}, {d} day{p['dp']}, {h} hour{p['hp']}, {minute} minute{p['minutep']} {s} second{p['sp']}, {ms} millisecond{p['msp']} for the exercise: '{exercise}'.",bg=self.universalBackground)
        LabelToTimeUsed.pack(side=TOP,fill=X)
        LabelFirstTimeStart=Label(TS,text=f"Exercise ({exercise}) first time started on {self.first_time_started}",bg=self.universalBackground)
        LabelFirstTimeStart.pack(side=TOP,fill=X)
        LabelTimeStart=Label(TS,text=f"Exercise ({exercise}) started at {time_start}.",bg=self.universalBackground)
        LabelTimeStart.pack(side=TOP,fill=X)
        LabelTimeStop=Label(TS,text=f"Exercise ({exercise}) finished at {time_stop}.",bg=self.universalBackground)
        LabelTimeStop.pack(side=TOP,fill=X)
        ButtonContinue=Button(TS,text="Okay!",bg=self.universalBackground,command=TS.destroy)
        ButtonContinue.pack(side=TOP,fill=X)
        TS.mainloop()
    def start(self):
        log.ProgStarted(self,__name__)
        log.CompInfo(self,self.OSInfo)
        Windows.Home(self)
        log.ProgStopped(self,__name__)

class log(Windows):
    def AppendLog(self,Content):
        if os.path.exists(f"{self.logDir}")==False:
            os.mkdir(f"{self.logDir}")
        f=open(f"{self.logDir}/Log_{self.username}.log","a")
        f.write(f"{Content}")
        f.close()
    def score(self,score,exercise):
        update.date(self)
        log.AppendLog(self,f"[{self.Alls}]: Your score is '{score}' for the exercise: '{exercise}'.\n")
    def questions(self,answ_questions,tot_questions,exercise):
        update.date(self)
        if answ_questions>1:
            plurala="s"
        else:
            plurala=""
        if tot_questions>1:
            pluralt="s"
        else:
            pluralt=""
        log.AppendLog(self,f"[{self.Alls}]: You have answered {answ_questions} question{plurala} of {tot_questions} question{pluralt} for the exercise '{exercise}'.\n")
    def Time(self,Start_time,Stop_time,exercise,total_time=0):
        timeInfo=Windows.SubOperations.splitTime(self,Start_time,Stop_time,total_time=total_time)
        p=timeInfo["p"]
        if total_time!=0:
            Start_time=total_time["time_start"]
        log.AppendLog(self,f"[{self.Alls}]: You took {timeInfo['y']} year{p['yp']}, {timeInfo['mo']} month{p['mop']}, {timeInfo['d']} day{p['dp']}, {timeInfo['h']} hour{p['hp']}, {timeInfo['minute']} minute{p['minutep']} {timeInfo['s']} second{p['sp']}, {timeInfo['ms']} millisecond{p['msp']} for the exercise: '{exercise}', exercise started at {Start_time} and finished at {Stop_time}.\n")
    def ExerciseStarted(self,exercise):
        update.date(self)
        log.AppendLog(self,f"[{self.Alls}]: Exercise {exercise} started.\n")
    def ExerciseStopped(self,exercise):
        update.date(self)
        log.AppendLog(self,f"[{self.Alls}]: Exercise {exercise} stopped.\n")
    def ProgStarted(self,prog):
        update.date(self)
        log.AppendLog(self,f"[{self.Alls}]:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        log.AppendLog(self,f"[{self.Alls}]:+--------------------------+\n")
        log.AppendLog(self,f"[{self.Alls}]:|  Program {prog} started. |\n")
        log.AppendLog(self,f"[{self.Alls}]:+--------------------------+\n")
    def ProgStopped(self,prog):
        update.date(self)
        log.AppendLog(self,f"[{self.Alls}]: Program {prog} stopped.\n")
    def CompInfo(self,OSInfo):
        update.date(self)
        log.AppendLog(self,f"[{self.Alls}]:##################################################################################################################################\n")
        log.AppendLog(self,f"[{self.Alls}]:Begining of usseless but usable data.\n")
        for i in OSInfo:
            update.date(self)
            log.AppendLog(self,f"[{self.Alls}]:{i}={OSInfo[i]}\n")
        update.date(self)
        log.AppendLog(self,f"[{self.Alls}]:Ending of usseless but usable data.\n")
        log.AppendLog(self,f"[{self.Alls}]:##################################################################################################################################\n")
    def view(self):
        # if self.OSInfo["name"]=="nt":
        #     os.startfile(r"{self.logDir}/Log_{self.username}.log")
        f=open(f"{self.logDir}/Log_{self.username}.log","r")
        content=f.read()
        f.close()
        content=content.split("\n")
        Display=Tk()
        Display.geometry(self.geometry)
        Display.minsize(self.size_x,self.size_y)
        if self.hasIcon==True:Display.iconbitmap=self.icon
        Display.title(f"Log of {self.unsername}")
        Display["bg"]=self.universalBackground
        WindowTitle=Label(Display,text=f"Log of {self.username}",fg=self.universalForeground,bg=self.universalBackground,anchor="center")
        WindowTitle.pack(side=TOP,fill=X)
        TextLog=Text(Display,bg=self.universalBackground,fg=self.universalForeground,cursor="cross",wrap="word",width=100,height=200,exportselection=0)
        TextLog.pack(side=TOP,fill=X)
        for i in range(len(content)):
            TextLog.insert(f"{i}.0",f"{content[i]}\n")
        Close=Button(Display,text="Close",bg=self.universalBackground,fg=self.universalForeground,anchor="center",command=Display.destroy)
        Close.pack(side=TOP,fill=X)
        Display.mainloop()

class update(Windows):
    def date(self):
        DATE=datetime.now()
        self.microsecond=DATE.microsecond
        self.second=DATE.second
        self.minute=DATE.minute
        self.hour=DATE.hour
        self.day=DATE.day
        self.month=DATE.month
        self.year=DATE.year
        self.Date=f"{self.day}/{self.month}/{self.year}"
        self.Time=f"{self.hour}h{self.minute}min{self.second}s"
        self.Timep=f"{self.hour}h{self.minute}min{self.second}s{self.microsecond}ms"
        self.All=f"{self.day}/{self.month}/{self.year}:{self.hour}h{self.minute}min{self.second}s"
        self.Alls=f"{self.day}/{self.month}/{self.year}:{self.hour}h{self.minute}min{self.second}s{self.microsecond}ms"