import pickle
s={}
found=False
f=open("binary program.txt","rb+")
try:
    r=f.tell()
    s=pickle.load(f)
    print(s)
    if s['marks']>80:
        
        s['marks']+=5
        f.seek(r)
        pickle.dump(s,f)
    found=True
except EOFError:
    if found==False:
        print("no record found")
    else:
        print("updated record")
f.close()
