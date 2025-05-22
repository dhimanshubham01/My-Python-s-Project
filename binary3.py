import pickle
s={}
a=open("binary program.txt","ab")
q="y"
while q=="y":
    rno=int(input("enter roll no "))
    name=input("enter name ")
    marks=int(input("enter marks "))
    s["roll no"]=rno
    s["name"]=name
    s["marks"]=marks
    pickle.dump(s,a)
    print("inserted")
    q=input("do you want to continue or n \n press 'n' for no and 'y' to continue:::")
a.close()
