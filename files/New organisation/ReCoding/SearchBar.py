from Graphic_User_Interface import Windows as Win
from tkinter import *
try:
    from tkinter import *
except:
    from Tkinter import *
class Searchbar(Win):
    def Query_result(self,Query):
        if Query=="Words":
            print("words")
    def searchView(self):
        def StartSearch(*args):
            Query=SearchQueryField.get()

        Search=Tk()
        Search['bg']=self.universalBackground
        Search.title("Search a function...")
        SearchTitleLabel=Label(Search,text="Enter something to search, then press the magnifying glass",bg=self.universalForeground,bg=self.universalBackground,anchor="center")
        SearchTitleLabel.pack(side=TOP,fill=X)
        SearchFrame=Frame(Search,bg=self.universalBackground,border=FLAT,borderwidth=0)
        SearchFrame.pack(side=TOP, fill=X)
        SearchQueryField=Entry(SearchFrame,bg=self.universalBackground,fg=self.universalForeground,width=500)
        SearchQueryField.pack(side=LEFT,fill=X)
        SearchQueryButton=Button(SearchFrame,bg=self.universalBackground,fg=self.universalForeground,activebackground=self.universalForeground,activeforeground=self.universalBackground,width=50,height=50,text="",anchor="center",command=StartSearch)
        SearchQueryButton.pack(side=LEFT)
        FrameQuerySearchResults=Frame(Search,bg=self.universalBackground,fg=self.universalForeground,anchor="nw")
        FrameQuerySearchResults.pack(side=TOP,fill=BOTH)

        Search.mainloop()
