a=input("enter a string:::")
b=a.split()
n=0
for i in range(len(b)):
    if len(b[n])<len(b[i]):
        n=i
print("longerst sub string::::",b[n])

