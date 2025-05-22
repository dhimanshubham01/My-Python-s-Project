f=open("q.txt","w")
i=1
while i<=5:
    b=input("enter names ")
    f.write(b)
    print(b)
    i=i+1
f.close()
