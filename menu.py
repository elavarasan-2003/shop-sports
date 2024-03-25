#------------------------------------------------menu page--------------------------------------------------
import tkinter as tk
from tkinter import *
from tkinter import ttk
from prod import *
from emp import *
from bill import *
from customer import*
from display import *
#-------------------------------------menu function------------------------------------------------
def menu():
    second=Tk()
    second.geometry("800x500")
    second.title("home")
    second.state('zoomed')
    second.configure(background="black")
    Label(second,text="MEPCO SPORTS SHOP",fg="white",bg="black",font="arial 30 bold").place(x=470,y=80)

    Label(second,text="MAIN MENU",fg="white",bg="black",font="orbitron 12").place(x=630,y=140)

    #Label(second,text="Please make a option",fg="white",bg="black",font="orbitron 13").place(x=600,y=180)

    Button(second, text="PRODUCT",command=product,fg="red", height=4, width=70).place(x=430,y=210)

    Button(second, text="EMPLOYEE",command=employee, height=4,fg="red", width=70).place(x=430,y=290)

    Button(second, text="CUSTOMER",command=customer, height=4, fg="red",width=70).place(x=430,y=370)

    Button(second, text="TRANSACTION",command=trandisplay, height=4, fg="red",width=70).place(x=430,y=450)

    Button(second, text="BILL", height=4,command=bill,fg="red", width=70).place(x=430,y=530)

    Button(second, text="BACK",command =second.destroy,height=4,fg="black", width=70).place(x=430,y=610)

    second.mainloop()
