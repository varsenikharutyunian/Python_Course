f=open("6.txt","r")
text=f.read()
print(len(text))

g=open("test.log","r")
txt=g.read(6)
print(txt)


f=open("may30.py","r")
with open("may30.py") as f:
    text=f.readline()
print(sum(map(int,text.split(",")))