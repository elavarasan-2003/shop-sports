#-------------------------------------------------employee page--------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
from display import *
#---------------------------------------------------add employee----------------------------------------------
def empadd():
    eid = p1.get()
    ename = p2.get()
    salary = p3.get()
    pno = p4.get()

    mysqldb=mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
    mycursor=mysqldb.cursor()

    try:
        sql = "INSERT INTO employee (eid,ename,salary,pno)VALUES (%s,%s,%s,%s)"
        val = (eid, ename,salary, pno)
        mycursor.execute(sql, val)
        mysqldb.commit()
            #lastid = mycursor.lastrowid
        messagebox.showinfo("information", "record inserted successfully....")
        p1.delete(0, END)
        p2.delete(0, END)
        p3.delete(0, END)
        p4.delete(0, END)
        p1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()



#----------------------------------------------------update employee-----------------------------------------------
def empupdate():
        eid = p1.get()
        ename = p2.get()
        salary = p3.get()
        pno = p4.get()
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
        mycursor=mysqldb.cursor()

        try:
            sql = "update employee set ename=%s,salary=%s,pno=%s where eid=%s"
            val = (ename,salary,pno,eid)
            mycursor.execute(sql,val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information","product Updated Successfully...")

            p1.delete(0, END)
            p2.delete(0, END)
            p3.delete(0, END)
            p4.delete(0, END)
            p1.focus_set()

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
#-------------------------------------------------delete employee---------------------------------------------------
def empdelete():
        eid = p1.get()

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
        mycursor=mysqldb.cursor()

        try:
            sql = "delete from employee where eid=%s"
            val = (eid,)
            mycursor.execute(sql,val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information","Product Delete Successfully...")

            p1.delete(0, END)
            p2.delete(0, END)
            p3.delete(0, END)
            p4.delete(0, END)
            p1.focus_set()

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
#----------------------------------------------manipulate employee-------------------------------------------------
def employee():
    eroot = Tk()
    eroot.geometry("800x500")
    eroot.configure(background="black")
    global p1
    global p2
    global p3
    global p4
    eroot.state('zoomed')
    Label(eroot, text="MEPCO SPORTS SHOP ", fg="white",bg="black", font="ariel 30 bold").place(x=425, y=50)
    Label(eroot, text="EMPLOYEE  DETAILS", fg="red",bg="black", font="ariel 15 bold").place(x=550, y=100)
    Label(eroot, text="EMPLOYEE ID",fg="white",bg="black", font="ariel 15 ").place(x=375,y=200)
    Label(eroot, text="EMPLOYEE NAME",fg="white",bg="black", font="ariel 15").place(x=375,y=250)
    Label(eroot, text="SALARY",fg="white",bg="black", font="ariel 15").place(x=375,y=300)
    Label(eroot, text="PHONE NUMBER",fg="white",bg="black", font="ariel 15 ").place(x=375,y=350)

    p1 = Entry(eroot)
    p1.place(x=750, y=200,width=160,height=30)

    p2 = Entry(eroot)
    p2.place(x=750, y=250,width=160,height=30)

    p3 = Entry(eroot)
    p3.place(x=750, y=300,width=160,height=30)

    p4 = Entry(eroot)
    p4.place(x=750, y=350,width=160,height=30)

    Button(eroot, text="ADD", command=empadd ,fg="red", height=2, width=13).place(x=230,y=500)

    Button(eroot, text="UPDATE", command= empupdate,fg="red", height=2, width=13).place(x=430,y=500)

    Button(eroot, text="DELETE", command= empdelete,fg="red", height=2, width=13).place(x=630,y=500)

    Button(eroot, text="DISPLAY", command= empdisplay, fg="red",height=2, width=13).place(x=830,y=500)

    Button(eroot, text="BACK", command= eroot.destroy,fg="black", height=2, width=13).place(x=1030,y=500)

    eroot.mainloop()
