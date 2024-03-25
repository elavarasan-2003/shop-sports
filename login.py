#-------------------------------------------------------------login page----------------------------------------------------
import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call
from select_1 import *
#-----------------------------------------------------login function---------------------------------------------------------
def ok():
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="praba2910",database="sports")
    mycursor=mysqldb.cursor()
    uid=r1.get()
    passwd=r2.get()
    sql="select * from login where uid=%s and passwd=%s"
    mycursor.execute(sql,[(uid),(passwd)])
    result=mycursor.fetchall()
    if result:
        menu()
        #lroot.destroy()
        call(["python","main.py"])
        return True
    else:
        messagebox.showinfo("","incorrect")
        return False
#--------------------------------------------------------------register function---------------------------------------------
def reg():
    uid = r1.get()
    passwd = r2.get()

    mysqldb=mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
    mycursor=mysqldb.cursor()

    try:
        sql = "INSERT INTO login (uid,passwd)VALUES (%s,%s)"
        val = (uid, passwd)
        if val[0] and val[1]:
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "record inserted successfully....")
            r1.delete(0, END)
            r2.delete(0, END)
            r1.focus_set()
        else:
            messagebox.showinfo("alert","Please check")
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()
#--------------------------------------------------login window development---------------------------------
lroot=Tk()
lroot.title("login")
lroot.geometry("800x500")
lroot.state('zoomed')
lroot.configure(background="dark grey")
global r1
global r2

Label(lroot,text="LOGIN FORM",font="ariel 35 bold",bg="dark grey").place(x=570,y=80)

Label(lroot,text="username",font="ariel 20 bold",bg="dark grey").place(x=530,y=220)
Label(lroot,text="password",font="ariel 20 bold",bg="dark grey").place(x=530,y=290)

r1=Entry(lroot)
r1.place(x=750,y=225,width=160,height=30)

r2=Entry(lroot)
r2.place(x=750,y=295,width=160,height=30)
r2.config(show="*")
Button(lroot,text="login",command=ok,height=2,width=13).place(x=450,y=400)

Button(lroot,text="register",command=reg,height=2,width=13).place(x=650,y=400)
Button(lroot,text="EXIT",command=lroot.destroy,height=2,width=13).place(x=850,y=400)
#Button(lroot,text="enter",command=menu,height=2,width=13).place(x=700,y=250)
lroot.mainloop()
