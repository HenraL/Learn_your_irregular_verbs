import sys
import requests
import os
def pause():
    pause=input("Press enter to continue...")
class Get:
    def __init__(self):
        self.home="https://henral.github.io/Learn_your_irregular_verbs/"
        self.data="files/website/additionnal_files/metadata/writtenList"
        self.dataFiles=['English(AInsi).txt', 'English(safe).txt', 'English.csv', 'English.xlsx', 'formats.txt', 'French.csv', 'German.csv', 'read.py', 'Spanish.csv', 'start.cmd', 'test(default format).csv', 'test.csv', 'translate.py']
        self.folders=["metadat","writtenList"]
    def prepareTheTerrain(self):
        self.temp="./"
        for i in range(len(self.folders)):
            if os.path.exists(f"{self.temp}{self.folders[i]}")==False:
                os.mkdir(f"{self.temp}{self.folders[i]}")
            self.temp+=f"{self.folders[i]}/"
    def folders(self):
        for i in range(len(self.dataFiles)):
            if os.path.exists(f"{self.temp}{self.dataFiles[i]}")==False:
                fileContent=Get.link(f"{self.home}/{self.data}/{self.temp}{self.dataFiles[i]}")
                if type(fileContent)==type(b"ee"):
                    f=open(f"{self.temp}{self.dataFiles[i]}","wb")
                    f.write(fileContent)
                    f.close()
                elif type(fileContent)==type(""):
                    f=open(f"{self.temp}{self.dataFiles[i]}","w")
                    f.write(fileContent)
                    f.close()
                else:
                    print(f"Error:\nFile {self.dataFiles[i]} could not be found in the database.")
    def link(url):
        try:
            e=requests.get(url)
            return e.content
        except:
            return ["",""]
    def start(self):
        Get.prepareTheTerrain(self)
        Get.folders(self)
class languages:
    def __init__(self):
        self.a="DATAbases"
        self.path="metadata/writtenList"
        self.sortList=["inf","pras","prat","perf","trad_fr","hint_fr","trad_eng","hint_eng"]
    def GetVerbs(self,file,path):
        """Treats a csv file and retruns the table as a list containing dictionaries for the lines"""
        print(f"path={path}, file={file}.csv,path/file={path}/{file}.csv")
        # pause()
        try:
            f=open(f"{path}/{file}.csv","r")
            e=f.read()
            f.close()
        except:
            print("r failed")
            try:
                f=open(f"{path}/{file}.csv","rb")
                e=f.read()
                f.close()
                try:
                    print("decoding")
                    e=e.decode()
                    print("decoded")
                except:
                    print("rb success but decode failed.")
                    sys.exit(0)
            except:
                print("r and rb failed")
                sys.exit(0)
        if len(e)>0:
            e=e.split("\n")
            # print(f"type(e)={type(e)}")
            # print(f"e=\n{e}")
            self.sortList=e.pop(0)
            # print(f"self.sortList={self.sortList}")
            self.sortList=self.sortList.split(";")
            temp=self.sortList[len(self.sortList)-1].split("\r")
            self.sortList[len(self.sortList)-1]=temp[0]
            # print(f"e={e}")
            if e[len(e)-1]=="":
                print(f"e.pop(len(e)-1)='{e.pop(len(e)-1)}'")
            # pause()
            for i in range(len(e)):
                # print(f"e[i]={e[i]}")
                e[i]=e[i].split(";")
            temp=[]
            print(f"self.sortList={self.sortList}")
            # pause()
            for i in range(len(e)):
                # print(f"i={i},len(e)={len(e)}")
                sub_temp={}
                for b in range(len(self.sortList)):
                    # print(f"i={i},len(e[i])={len(e[i])} len(self.sortList)={len(self.sortList)},self.sortList[b]={self.sortList[b]}")
                    sub_temp[self.sortList[b]]=e[i][b]
                temp.append(sub_temp)
            return temp
        else:
            return ''
    def start(self):
        Get.start(Get())
        print(f"self.a={self.a}")
        print("English")
        self.sortList=["inf","pret","pastSimp.","trad_fr","hint_fr","trad_de","hint_de","hint_eng","trad_es","hint_es"]
        EN=languages.GetVerbs(self,"English",self.path)
        ColumnsEN=self.sortList
        print("French")
        self.sortList=["inf","pres","pret","perf","trad_fr","hint_fr","trad_eng","hint_eng"]
        FR=languages.GetVerbs(self,"French",self.path)
        ColumnsFR=self.sortList
        print("German")
        self.sortList=["inf","pras","prat","perf","trad_fr","hint_fr","trad_eng","hint_eng"]
        DE=languages.GetVerbs(self,"German",self.path)
        ColumnsDE=self.sortList
        print("Spanish")
        self.sortList=["inf","pras","prat","perf","trad_fr","hint_fr","trad_eng","hint_eng"]
        ES=languages.GetVerbs(self,"Spanish",self.path)
        ColumnsES=self.sortList
        return {"EN":EN,"FR":FR,"DE":DE,"ES":ES},{"EN":ColumnsEN,"FR":ColumnsFR,"DE":ColumnsDE,"ES":ColumnsES}
