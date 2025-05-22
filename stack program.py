#top=-1
#li=list[]
def push(val):
    li.append(val)
    top=len(li)-1
    print("value installed")
def pop():
    if(len(li)==0):
        print("under flow")
    else:
        v=li.pop(len(li)-1)
        if len(li)==0:
            top=None
        else:
            top=len(li)-1
        print("delete",v)
def disp():
    if(len(li)==0):
        print("under flow")
        return
    top=len(li)-1
    for i in range(top,-1,-1):
        print(li[i])
def peek():
    if(len(li)==0):
        print("under flow")
        return
    else:
        top=len(li)-1
        return li[top]
top=None
li=[]
while True:
    print("enter 1 for insert \n 2 for deletion \n 3 for display \n 4 for peek and any other key foe exit")
    ch=int(input("enter choice "))
    if ch == 1:
        val=int(input('enter value to insert'))
        push(val)
    elif ch == 2:
        pop()
    elif ch == 3:
        disp()
    elif ch == 4:
        va=peek()
        print("value on top is ",va)
    else:
        break
    
    
