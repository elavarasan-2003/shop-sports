#-------------------------------------------customer page----------------------------------------------
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
from display import *
#-------------------------------------------------------------add customer------------------------------------------
def cusadd():
    cid = c1.get()
    cname = c2.get()
    mysqldb=mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
    mycursor=mysqldb.cursor()

    try:
        sql = "INSERT INTO customer (cid,cname)VALUES (%s,%s)"
        val = (cid, cname)	
        mycursor.execute(sql, val)
        mysqldb.commit()
            #lastid = mycursor.lastrowid
        messagebox.showinfo("information", "record inserted successfully....")
        c1.delete(0, END)
        c2.delete(0, END)
        c1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

#--------------------------------------------------------------update customer--------------------------------------
def cusupdate():
        cid = c1.get()
        cname = c2.get()
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
        mycursor=mysqldb.cursor()

        try:
            sql = "update customer set cname=%s where cid=%s"
            val = (cname,cid)
            mycursor.execute(sql,val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information","product Updated Successfully...")

            c1.delete(0, END)
            c2.delete(0, END)
            c1.focus_set()

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
#-------------------------------------------------------------delete customer----------------------------------------
def cusdelete():
        cid = c1.get()

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
        mycursor=mysqldb.cursor()

        try:
            sql = "delete from customer where cid=%s"
            val = (cid,)
            mycursor.execute(sql,val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information","Product Delete Successfully...")

            c1.delete(0, END)
            c2.delete(0, END)
            c1.focus_set()

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
#---------------------------------------------------manipulate customer---------------------------------------------------
def customer():
    croot = Tk()
    croot.geometry("800x500")
    croot.configure(background="black")
    global c1
    global c2
    croot.state('zoomed')
    Label(croot, text="MEPCO SPORTS SHOP ", fg="white",bg="black", font="ariel 30 bold").place(x=425, y=50)
    Label(croot, text="CUSTOMER  DETAILS", fg="red",bg="black", font="ariel 15 bold").place(x=550, y=100)
    Label(croot, text="CUSTOMER ID",fg="white",bg="black", font="ariel 15 ").place(x=375,y=200)
    Label(croot, text="CUSTOMER NAME",fg="white",bg="black", font="ariel 15").place(x=375,y=250)
    #Label(croot, text="SALARY",fg="white",bg="black", font="ariel 15").place(x=375,y=300)
    #Label(croot, text="PHONE NUMBER",fg="white",bg="black", font="ariel 15 ").place(x=375,y=350)

    c1 = Entry(croot)
    c1.place(x=750, y=200,width=160,height=30)
    c2 = Entry(croot)
    c2.place(x=750, y=250,width=160,height=30)
    Button(croot, text="ADD", command=cusadd ,fg="red", height=2, width=13).place(x=230,y=500)

    Button(croot, text="UPDATE", command= cusupdate,fg="red", height=2, width=13).place(x=430,y=500)

    Button(croot, text="DELETE", command= cusdelete,fg="red", height=2, width=13).place(x=630,y=500)

    Button(croot, text="DISPLAY", command= cusdisplay, fg="red",height=2, width=13).place(x=830,y=500)

    Button(croot, text="BACK", command= croot.destroy,fg="black", height=2, width=13).place(x=1030,y=500)

    croot.mainloop()
