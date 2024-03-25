#------------------------------------------bill page------------------------------------------------------

import datetime
from tkinter import *
from tkinter import messagebox
import mysql.connector
#------------------------------------------------------------bill function------------------------------------------------
def bill():
    root4=Tk()
    root4.title("Billing Slip")
    root4.geometry('1280x720')
    root4.configure(background="brown")
    global l
    l=[]

    def exit():
        op=messagebox.askyesno('save Exit','Do u want to exit')
        if op>0:
            root4.destroy()
#------------------------------------------function to clear entry--------------------------------
    def clear():
            ientry.delete(0, END)
            rentry.delete(0, END)
            qentry.delete(0, END)
            ientry.focus_set()
#------------------------below function are manipulate the product quantity-----------------------------------
    def updateq(name1,price1,q1,Pid1):

            q=int(q1)
            Pid=str(Pid1)
            name=str(name1)
            price=int(price1)
            print(q)
            print(Pid)
            print(name)
            print(price)

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
            mycursor=mysqldb.cursor()

            try:
                sql = "update product set pname=%s,price=%s,quantity=%s where pid=%s"
                val = (name,price,q,Pid)
                mycursor.execute(sql,val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                #messagebox.showinfo("information","product Updated Successfully...")

            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()
    def updatequan(qm,Pid):

        try:
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
            mycursor=mysqldb.cursor()

            sql="SELECT pname,price,quantity FROM product where pid=%s"
            val=(Pid,)
            mycursor.execute(sql,val)
           # mysqldb.commit()
            lquan = mycursor.fetchone()
            name=lquan[0]
            price=lquan[1]
            qc=lquan[2]
            q=int(qc)
            q-=qm
            updateq(name,price,q,Pid)
        except Exception as e:
            print(e)
            print("error")
            mysqldb.rollback()
            mysqldb.close()
    def billadd():
        stotal=0
        Pid=ientry.get()
        quan = int(qentry.get())
        price =int(rentry.get())
        stotal=price*quan
        l.append(stotal)
        updatequan(quan,Pid)
        print("check last")
        clear()
    def tbill():
        billadd()
        cid=str(centry.get())
        #bill_id=bentry.get()
        print(cid)
        #print(bill_id)
        tb=sum(l)
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
        mycursor=mysqldb.cursor()
        d=datetime.datetime.now().date()

        try:
            sql = "INSERT INTO transaction(cid,total,date)VALUES (%s,%s,%s)"
            val = (cid,tb,d)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("Bill UPDATED successfully....")
            root4.destroy()

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    global centry
    global eentry
    global ientry
    global rentry
    global qentry
    global bentry

    #----TOP SECTON----
    title=Label(root4,text='MEPCO SPORTS SHOP',fg='white',font=('times new romman',25,'bold'),bg='brown',relief=GROOVE,bd=12)
    title.pack(fill=X)

    #_____customer details_____
    f1=LabelFrame(root4,text="CUSTOMER AND EMPLOYEE DETAILS",font=('times new romman',18,'bold'),bg='brown',relief=GROOVE,bd=10,fg='gold')
    f1.place(x=0,y=80,relwidth=1)

    cid=Label(f1,text="CUSTOMER ID",font=('timesnew romman',18,'bold'),fg='black',bg='brown')
    cid.grid(row=0,column=0,padx=10,pady=5)
    centry=Entry(f1,width=15,font='arial 15 bold')
    centry.grid(row=0,column=1,padx=10,pady=5)

    """eid=Label(f1,text="EMPLOYEE ID",font=('timesnew romman',18,'bold'),fg='black',bg='brown')
    eid.grid(row=0,column=2,padx=10,pady=5)
    eentry=Entry(f1,width=15,font='arial 15 bold')
    eentry.grid(row=0,column=3,padx=10,pady=5)"""

    """ b=Label(f1,text="BILL ID",font=('timesnew romman',18,'bold'),fg='black',bg='brown')
    b.grid(row=0,column=4,padx=30,pady=20)
    bentry=Entry(f1,width=15,font='arial 15 bold')
    bentry.grid(row=0,column=5,padx=30,pady=20)"""

    #---------product details--------
    f2=LabelFrame(root4,text="PRODUCT DETAILS",font=('times new romman',18,'bold'),bg='brown',relief=GROOVE,bd=10,fg='gold')
    f2.place(x=300,y=180,width=630,height=500)

    itm=Label(f2,text="PRODUCT ID",font=('timesnew romman',18,'bold'),fg='black',bg='brown')
    itm.grid(row=0,column=0,padx=30,pady=20)
    ientry=Entry(f2,width=15,font='arial 15 bold')
    ientry.grid(row=0,column=1,padx=30,pady=20)

    rate=Label(f2,text="PRICE",font=('timesnew romman',18,'bold'),fg='black',bg='brown')
    rate.grid(row=1,column=0,padx=30,pady=20)
    rentry=Entry(f2,width=15,font='arial 15 bold')
    rentry.grid(row=1,column=1,padx=30,pady=20)

    quan=Label(f2,text="QUANTITY",font=('timesnew romman',18,'bold'),fg='black',bg='brown')
    quan.grid(row=2,column=0,padx=30,pady=20)
    qentry=Entry(f2,width=15,font='arial 15 bold')
    qentry.grid(row=2,column=1,padx=30,pady=20)


    #----button----
    b1=Button(f2,text="add item",command=billadd,font="arial 15 bold")
    b1.grid(row=3,column=0,padx=10,pady=30)
    b2=Button(f2,text="BILL",command=tbill,font="arial 15 bold")
    b2.grid(row=4,column=0,padx=10,pady=30)
    b3=Button(f2,text="Clear",command=clear,font="arial 15 bold")
    b3.grid(row=3,column=1,padx=10,pady=30)
    b4=Button(f2,text="Exit",command=exit,font="arial 15 bold")
    b4.grid(row=4,column=1,padx=10,pady=30)

    #bill area

    """f3=Frame(root4,relief=GROOVE,bd=10)
    f3.place(x=700,y=180,width=500,height=500)
    bill_title=Label(f3,text="BILL AREA",font=('timesnew romman',18,'bold'),bg='brown',relief=GROOVE,bd=7).pack(fill=X)
    Scroll_y=Scrollbar(f3,orient=VERTICAL)
    textarea=Text(f3,yscrollcommand=Scroll_y)
    Scroll_y.pack(side=RIGHT,fill=Y)
    Scroll_y.config(command=textarea.yview)
    textarea.pack()
    #welcome()"""

    root4.mainloop()
