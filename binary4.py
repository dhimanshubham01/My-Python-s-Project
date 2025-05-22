import pickle
s="this program is used with statement"
with open("binary program.txt","ab")as a:
    pickle.dump(s,a)
print("installed")
