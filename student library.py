import mysql.connector as a
con=a.connect(host="localhost",user="root",passwd="123456",database="l1")

def issueb():
    n=input("Enter Scholar number : ")
    r=input("Enter Name : ")
    q=input("Enter Class : ")
    w=input("Enter Section : ")
    d=input("Enter Issueing Book Data : ")
    co=input("Enter Book Code : ")
    a="insert into s_issue values(%s,%s,%s,%s,%s,%s)"
    data=(n,r,q,w,d,co)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print(">------------------------------------------------------------------<")
    print("Book issued to : ",r,"--",n)
    bookup(co,-1)

def submitb():
    n=input("Enter Scholar number : ")
    r=input("Enter Name : ")
    q=input("Enter Class : ")
    w=input("Enter Section : ")
    d=input("Enter Submiting Book Data : ")
    co=input("Enter Book Code : ")
    a="insert into s_submit values(%s,%s,%s,%s,%s,%s)"
    data=(n,r,q,w,d,co)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print(">------------------------------------------------------------------<")
    print("Book Submitted from : ",r,"--",n)
    bookup(co,1)

def bookup(co,u):
    a="select TOTAL from books where BCODE=%s"
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0]+u
    sql="update books set TOTAL = %s where BCODE = %s"
    d=(t,co)
    c.execute(sql,d)
    con.commit()
    main()

def dispbook():
    a="select *from books"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Book Name : ",i[0])
        print("Book Code : ",i[1])
        print("Total : ",i[2])
        print(">------------------------<")
    main()

def main():
    print('''
                                Welcome!!!!!!
                        To Nosegay Public School Library
    1. ISSUE BOOK
    2. SUBMIT BOOK
    3. DISPLAY BOOKS
    ''')
    cho=input("Enter Task No. : ")
    print(">--------------------------------------------------------------------<")           
    if cho=='1' :
        issueb()
    elif cho=='2' :
        submitb()
    elif cho=='3' :
        dispbook()
    else:
        print("wrong choice entered!!!!!!!!")
        main()
    
main()
