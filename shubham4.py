#prog find largest no.
def l(a):
    m=0
    while (a>0):
        b=a%10
        if b>m:
            m=b
        a=a//10
    return(m)
q=int(input(""))
z=l(q)
print(z)
