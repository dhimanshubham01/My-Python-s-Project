import pickle
emp1={'empno':1,'name':"ankush","age":22,"salery":25000}
emp2={"empno":2,"name":"shiv","age":21,"salery":15000}
emp3={"enpno":3,"name":"pinky","age":25,"salery":20000}
a=open("binary program.txt",'wb')
pickle.dump(emp1,a)
pickle.dump(emp2,a)
pickle.dump(emp3,a)
print("successfully written in binary")
a.close()
