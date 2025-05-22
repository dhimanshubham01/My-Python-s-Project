#pro lcm and hcf
def hcf(a,b):
    if a>b:
        larger=a
        smaller=b
    else:
        larger=b
        smaller=a
    for i in range(1,smaller+1):
        if larger%i==0:
            if smaller%i==0:
                n=i
        else:
            o=0
    return(n);
def lcm(c,d):
    if c>d:
        larger=c
        smaller=d
    else:
        larger=d
        smaller=c
    while(True):
        if larger%c==0 and smaller%d==0:
            k=larger
            break
        else:
            larger=larger+1
    return(k);
o=int(input(""))
p=int(input(""))
z=lcm(o,p)
x=hcf(o,p)
print("lcm ",z)
print("HCF ",x)
        
        
