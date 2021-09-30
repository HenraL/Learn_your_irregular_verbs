try:
    print("opening as rb")
    f=open("English.csv","rb")
    e=f.read()
    f.close()
    print("decoding")
    e=e.decode()
    print("decoded")
except:
    print("failed")

try:
    print("opening as r")
    f=open("English.csv","rb")
    e=f.read()
    f.close()
    print("read")
except:
    pass
