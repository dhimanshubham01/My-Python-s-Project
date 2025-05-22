#pro simple intrest and compound intrest
def simp(p,r,t):
    q=(p*r*t)/100
    return q
def com(p,r,t):
    t=p+(1+(r/100))**t
    return t
a=int(input("prinpal amount::::"))
b=int(input("rate::::"))
c=int(input("time in year:::"))
w=input("press s for simple intrest or press c for compound intrest:::")
if w=='s':
    m=simp(a,b,c)
    print("simple intrest:::",m)
elif w=="c":
    n=com(a,b,c)
    print("compound intrest::::",n)
   
