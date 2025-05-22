import pickle
emp={}
a=open("binary program.txt","rb")
try:
    while True:
        emp=pickle.load(a)
        print(emp)
except EOFError:
    a.close()
