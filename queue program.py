li=[]
f,e=0,0
def inqueue(val):
    if len(li)==0:
        li.append(val)
        f=e=len(li)-1
    else:
        li.append(val)
        e=len(li)-1
    print("value inserted")
    return
def dequeue():
    if len(li)==0:
        print("under flow")
        return
    elif len(li)==1:
        li.pop(0)
        f=e=None
    else:
        li.pop(0)
    print("value deleted")
    return
def disp():
    if len(li)==0:
        print("empty empty empty empty empty")
    else:
        for i in range(0,len(li)):
            print(li[i])
        return
def peek():
    if len(li)==0:
        print("under flow")
    else:
        e=len(li)-1
        print(li[e])
        return
while True:
    print("enter 1 for push \n 2 for pop \n 3 for display \n 4 for peek \n any other key for exit")
    ch=int(input("enter choice  "))
    if (ch == 1):
        val=int(input("enter value to insert "))
        inqueue(val)
    elif (ch == 2):
        dequeue()
    elif (ch == 3):
        disp()
    elif (ch == 4):
        peek()
    else:
        break
    
            
        
