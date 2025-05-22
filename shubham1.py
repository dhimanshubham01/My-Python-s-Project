#pro prime and co-prime
def cop(a,b):
    if a>b:
        l=a
        ss=b
    else:
        l=b
        ss=a
    c=0
    for i in range(1,ss+1):
        if l%i==0 and ss%i==0:
            c=c+1;
    p=c
    return p
f=int(input('first no.'))
s=int(input("second no."))
q=cop(f,s)
if q==1:
    print("co-prime")
else:
    print("not co-prime")
    
