#-----------------------------------------------------display page-----------------------------------------------------------

from tkinter import messagebox
import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import ttk
#-------------------------------------------------display function for product-------------------------------------------
def display():
    secondwindow = Tk()
    secondwindow.state('zoomed')
    secondwindow.title("Dispaly")
    secondwindow.configure(background="black")
    appLabel=tk.Label(secondwindow, text="PRODUCT DETAILS",fg="white",font="ariel 30 bold",bg="black",width = 40)
    appLabel.pack()

    Button(secondwindow, text="BACK", command= secondwindow.destroy,fg="black", height=2, width=13).place(x=600,y=400)

    Listbox = ttk.Treeview(secondwindow)
    Listbox["columns"] = ("one","two","three","four")
    #Listbox.place(x=400,y=700)
    Listbox.heading("one", text="PRODUCT ID")
    Listbox.heading("two", text="PRODUCT NAME")
    Listbox.heading("three", text="PRICE")
    Listbox.heading("four", text="QUANTITY")

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
    mycursor=mysqldb.cursor()
    mycursor.execute("SELECT pid,pname,price,quantity FROM product")
    products = mycursor.fetchall()
    print(products)

    for i, (pid, pname, price, quantity) in enumerate(products, start=1):
            Listbox.insert("","end", values=(pid, pname, price, quantity))
            mysqldb.close()
    treeScroll=ttk.Scrollbar(secondwindow)
    treeScroll.configure(command=Listbox.yview)
    Listbox.configure(yscrollcommand=treeScroll.set)
    treeScroll.pack(side=RIGHT,fill=BOTH)
    Listbox.pack()
    secondwindow.mainloop()
#---------------------------------------------------display function for employee---------------------------------------
def empdisplay():
    secondwindow = Tk()
    secondwindow.state('zoomed')
    secondwindow.title("Dispaly")
    secondwindow.configure(background="black")
    appLabel=tk.Label(secondwindow, text="EMPLOYEE DETAILS",fg="white",font="ariel 30 bold",bg="black",width = 40)
    appLabel.pack()

    Button(secondwindow, text="BACK", command= secondwindow.destroy,fg="black", height=2, width=13).place(x=600,y=400)

    Listbox = ttk.Treeview(secondwindow)
    Listbox["columns"] = ("one","two","three","four")
    #Listbox.place(x=400,y=700)
    Listbox.heading("one", text="EMPLOYEE ID")
    Listbox.heading("two", text="EMPLOYEE NAME")
    Listbox.heading("three", text="SALARY")
    Listbox.heading("four", text="PHONE NO")

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
    mycursor=mysqldb.cursor()
    mycursor.execute("SELECT eid,ename,salary,pno FROM employee")
    employees = mycursor.fetchall()
    print(employees)

    for i, (eid, ename, salary, pno) in enumerate(employees, start=1):
            Listbox.insert("","end", values=(eid, ename, salary, pno))
            mysqldb.close()
    treeScroll=ttk.Scrollbar(secondwindow)
    treeScroll.configure(command=Listbox.yview)
    Listbox.configure(yscrollcommand=treeScroll.set)
    treeScroll.pack(side=RIGHT,fill=BOTH)
    Listbox.pack()
    secondwindow.mainloop()

#-----------------------------------------------display customer-------------------------------------------------------
def cusdisplay():
    secondwindow = Tk()
    secondwindow.state('zoomed')
    secondwindow.title("Display")
    secondwindow.configure(background="black")
    appLabel=tk.Label(secondwindow, text="CUSTOMER DETAILS",fg="white",font="ariel 30 bold",bg="black",width = 40)
    appLabel.pack()

    Button(secondwindow, text="BACK", command= secondwindow.destroy,fg="black", height=2, width=13).place(x=600,y=400)

    Listbox = ttk.Treeview(secondwindow)
    Listbox["columns"] = ("one","two")
    #Listbox.place(x=400,y=700)
    Listbox.heading("one", text="CUSTOMER ID")
    Listbox.heading("two", text="CUSTOMER NAME")

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
    mycursor=mysqldb.cursor()
    mycursor.execute("SELECT cid,cname FROM customer")
    customer = mycursor.fetchall()
    print(customer)

    for i, (cid, cname) in enumerate(customer, start=1):
            Listbox.insert("","end", values=(cid, cname))
            mysqldb.close()
    treeScroll=ttk.Scrollbar(secondwindow)
    treeScroll.configure(command=Listbox.yview)
    Listbox.configure(yscrollcommand=treeScroll.set)
    treeScroll.pack(side=RIGHT,fill=BOTH)
    Listbox.pack()
    secondwindow.mainloop()

#------------------------------------------------display transaction--------------------------------------------------------
def trandisplay():
    def trandel():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
        mycursor=mysqldb.cursor()

        try:
            sql = "delete from transaction"
            mycursor.execute(sql)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo(" Deleted...")

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
    secondwindow = Tk()
    secondwindow.state('zoomed')
    secondwindow.title("Display")
    secondwindow.configure(background="black")
    appLabel=tk.Label(secondwindow, text="TRANSACTION DETAILS",fg="white",font="ariel 30 bold",bg="black",width = 40)
    appLabel.pack()

    Button(secondwindow, text="BACK", command= secondwindow.destroy,fg="black", height=2, width=13).place(x=600,y=400)
    Button(secondwindow, text="DELETE ALL", command=trandel,fg="black", height=2, width=13).place(x=700,y=400)

    Listbox = ttk.Treeview(secondwindow)
    Listbox["columns"] = ("one","two","three","four")
    #Listbox.place(x=400,y=700)
    Listbox.heading("one", text="BILL ID")
    Listbox.heading("two", text="CID NAME")
    Listbox.heading("three", text="TOTAL")
    Listbox.heading("four", text="DATE")

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="praba2910", database="sports")
    mycursor=mysqldb.cursor()
    mycursor.execute("SELECT bill_id,cid,total,date FROM transaction")
    trans = mycursor.fetchall()
    print(trans)

    for i, (bill_id, cid, total, date) in enumerate(trans, start=1):
            Listbox.insert("","end", values=(bill_id,cid,total,date))
            mysqldb.close()
    treeScroll=ttk.Scrollbar(secondwindow)
    treeScroll.configure(command=Listbox.yview)
    Listbox.configure(yscrollcommand=treeScroll.set)
    treeScroll.pack(side=RIGHT,fill=BOTH)
    Listbox.pack()
    secondwindow.mainloop()
