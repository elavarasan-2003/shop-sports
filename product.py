#-----------------------------------------employee page-------------------------------------------



import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
from display import *
from select_1 import *
#---------------------------------------------------------function to add product------------------------
def add():
    pid = e1.get()
    pname = e2.get()
    price = e3.get()
    quantity = e4.get()

    mysqldb=mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
    mycursor=mysqldb.cursor()

    try:
        sql = "INSERT INTO product (pid,pname,price,quantity)VALUES (%s,%s,%s,%s)"
        val = (pid, pname, price, quantity)
        mycursor.execute(sql, val)
        mysqldb.commit()
            #lastid = mycursor.lastrowid
        messagebox.showinfo("information", "record inserted successfully....")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

#---------------------------------------update product-------------------------------------------------
def update():
        pid = e1.get()
        pname = e2.get()
        price = e3.get()
        quantity = e4.get()
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
        mycursor=mysqldb.cursor()

        try:
            sql = "update product set pname=%s,price=%s,quantity=%s where pid=%s"
            val = (pname,price,quantity,pid)
            mycursor.execute(sql,val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information","product Updated Successfully...")

            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e1.focus_set()

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

#----------------------------------------------------delete product-------------------------
def delete():
        pid = e1.get()

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
        mycursor=mysqldb.cursor()

        try:
            sql = "delete from product where pid=%s"
            val = (pid,)
            mycursor.execute(sql,val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information","Product Delete Successfully...")

            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e1.focus_set()

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
#---------------------------------------function to manipulate product-------------------------------
def product():
    proot = Tk()
    proot.geometry("800x500")
    proot.configure(background="black")
    global e1
    global e2
    global e3
    global e4
    proot.state('zoomed')
    Label(proot, text="MEPCO SPORTS SHOP ", fg="white",bg="black", font="ariel 30 bold").place(x=425, y=50)
    Label(proot, text="PRODUCT  DETAILS", fg="red",bg="black", font="ariel 15 bold").place(x=550, y=100)
    Label(proot, text="PRODUCT ID",fg="white",bg="black", font="ariel 15 ").place(x=375,y=200)
    Label(proot, text="PRODUCT NAME",fg="white",bg="black", font="ariel 15").place(x=375,y=250)
    Label(proot, text="PRICE",fg="white",bg="black", font="ariel 15").place(x=375,y=300)
    Label(proot, text="QUANTITY",fg="white",bg="black", font="ariel 15 ").place(x=375,y=350)

    e1 = Entry(proot)
    e1.place(x=750, y=200,width=160,height=30)

    e2 = Entry(proot)
    e2.place(x=750, y=250,width=160,height=30)

    e3 = Entry(proot)
    e3.place(x=750, y=300,width=160,height=30)

    e4 = Entry(proot)
    e4.place(x=750, y=350,width=160,height=30)

    Button(proot, text="ADD", command=add ,fg="red", height=2, width=13).place(x=230,y=500)

    Button(proot, text="UPDATE", command= update,fg="red", height=2, width=13).place(x=430,y=500)

    Button(proot, text="DELETE", command= delete,fg="red", height=2, width=13).place(x=630,y=500)

    Button(proot, text="DISPLAY", command= display, fg="red",height=2, width=13).place(x=830,y=500)

    Button(proot, text="BACK", command= proot.destroy,fg="black", height=2, width=13).place(x=1030,y=500)

    proot.mainloop()
