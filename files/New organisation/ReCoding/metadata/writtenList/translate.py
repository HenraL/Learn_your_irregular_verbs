from tkinter import *
t=1
if t==1:
    def GetContent(*args):
        global e
        e=Test.get("0.0","end-1c")
        print(f"type(e)={type(e)}")
        #e=str(e)
        TT.destroy()
        print(e)
    TT=Tk()
    Test=Text(TT)
    Test.pack()
    r=Button(TT,text="Continue",command=GetContent,anchor="center")
    r.pack()
    TT.mainloop()

    print("content received")
else:
    f=open("English.py","r")
    e=f.read()
    f.close()
b=input("Enter the name (+extention) of the file that will receive the translated content:")
print("name received")
f=open(b,"w")
f.write(f"{e}")
f.close()
print("done")
