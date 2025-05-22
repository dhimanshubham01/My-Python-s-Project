def u(l1):
    q=len(l1)
    l2=[]
    for i in range(q):
        l1.sort()
        if i==0:
            l2.append(l1[0])
        elif l1[i-1] is not l1[i]:
            l2.append(l1[i])
    return(l2)
a=int(input("no. of digit::::"))
l1=[]
for i in range(0,a):
    b=int(input("enter a no.:::"))
    l1.insert(i,b)
print("input list:::",l1)
print("sorted list:::",u(l1))

