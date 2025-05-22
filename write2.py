a=open("C:\\Users\\Shubham\\Desktop\\aa.txt","r")
l=a.read()
b=len(l)
s=str(l)
j=0
for i in range(b):
    if s[i].isspace() :
        j=j+1
print(b-j)
#display sze of file after removing EOL charactor
