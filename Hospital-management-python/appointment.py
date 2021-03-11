import tkinter
from tkinter import *
import pymysql
mycon=pymysql.connect(host="localhost",user="root",password="986064",database="HMS")
conn=mycon.cursor()
rootAA=None

def set():
    global e3,e1,e2,e4,e5,e6,conn
    p1= e1.get()
    p2=e2.get()
    p4=e4.get()
    p5=e5.get()
    p6=e6.get(1.0,tkinter.END)
    mycon = pymysql.connect(host="localhost", user="root", password="986064", database="HMS")
    conn = mycon.cursor()
    conn.execute("Insert into appointment(PATIENT_ID,EMP_ID,AP_TIME,AP_DATE,description) values(%a,%a,%a,%a,%a)"%(p1,p2,p4,p5,p6))
    mycon.commit()
    tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "APPOINTMENT SET SUCCESSFULLY")


def appo():
    global rootAA,L,e1,e2,e4,e5,e6
    rootAA=tkinter.Tk()
    rootAA.geometry("500x550")
    rootAA.title("APPOINTMENTS")
    H=tkinter.Label(rootAA,text="APOINTMENTS",fg="blue",font="Arial 10 bold")
    H.place(x=55,y=5)
    l1=tkinter.Label(rootAA,text="PATIENT ID")
    l1.place(x=20,y=30)
    e1=tkinter.Entry(rootAA)
    e1.place(x=100,y=30)
    l2 = tkinter.Label(rootAA,text="DOCTOR ID")
    l2.place(x=20,y=60)
    e2 = tkinter.Entry(rootAA)
    e2.place(x=110, y=60)
    l4 = tkinter.Label(rootAA,text="APPOINTMENT TIME(HH:MM:SS)")
    l4.place(x=20,y=120)
    e4=tkinter.Entry(rootAA)
    e4.place(x=20,y=145)
    l5 = tkinter.Label(rootAA,text="APPOINTMENT DATE(YYYY-MM-DD)")
    l5.place(x=20,y=170)
    e5=tkinter.Entry(rootAA)
    e5.place(x=20,y=195)
    l6=tkinter.Label(rootAA,text="DESCRIPTION")
    l6.place(x=20,y=220)
    e6=tkinter.Text(rootAA,width=20,height=3)
    e6.place(x=20,y=240)
    scrollbar = tkinter.Scrollbar(rootAA,orient=tkinter.HORIZONTAL)
    scrollbar.place(x=235, y=90)
    b1=tkinter.Button(rootAA,text="SET APPOINTMENT",command=set)
    b1.place(x=20,y=310)
    b2=tkinter.Button(rootAA,text="Delete Appointment",command=dela)
    b2.place(x=180,y=310)
    b4=tkinter.Button(rootAA,text="TODAYS APPOINTMENTS",command=va)
    b4.place(x=320,y=310)
    rootAA.mainloop()

def remove():
    global e7,edd
    edd=str(e7.get())
    conn.execute("select * from appointment where AP_NO=%a;"%(edd,))
    v=conn.fetchone()
    if (v==None):
        errorD = tkinter.Label(rootAA, text="PATIENT APPOINTMENT NOT FIXED",fg="red")
        errorD.place(x=20,y=420)
    else:
        conn.execute("DELETE FROM appointment where AP_NO=%a"%(edd))
        disd1=tkinter.Label(rootAA,text="PATIENT APPOINTMENT DELETED",fg='green')
        disd1.place(x=20,y=420)
        mycon.commit()



def dela():
    global e1,e7
    l3 = tkinter.Label(rootAA, text="ENTER APPOINTMENT NO TO DELETE")
    l3.place(x=20, y=340)
    e7=tkinter.Entry(rootAA)
    e7.place(x=20,y=360)
    b3=tkinter.Button(rootAA,text="Delete",command=remove)
    b3.place(x=50,y=380)

rootAP=None

def viewappointment():
    global e8
    ap=str(e8.get())
    conn.execute("select * from appointment where AP_DATE=%a;"%ap)
    vv=conn.fetchone()
    if vv == None:
        errorD = tkinter.Label(rootAA, text="NO APPOINTMENT FOR TODAY", fg="red")
        errorD.place(x=20, y=420)
    else:
        s3=[]
        conn.execute("Select PATIENT_ID,NAME,AP_NO,AP_TIME from PATIENT NATURAL  JOIN appointment where AP_DATE=%a;"%ap)
        s1=conn.fetchall()
        conn.execute("select EMP_ID, DESIG,EMP_NAME from employee NATURAL JOIN appointment where AP_DATE=%a;"%ap)
        s2=conn.fetchall()
        s3 = [("PATIENT_ID | ", "NAME | ", "AP_NO | ", "AP_TIME | ", "EMP_ID | ", "EMP_TYPE | ", "NAME | ")]
        s3.append(" ")
        for i in range(len(s1)):
                 s3.append(s1[i]+s2[i])
        # Creating the root window
        root = tkinter.Tk()
        root.geometry("500x200")
        # Creating a Listbox and
        # attaching it to root window
        listbox = tkinter.Listbox(root)
        # Adding Listbox to the left
        # side of root window
        listbox.pack(side=LEFT, fill=BOTH,expand=True)

        # Creating a Scrollbar and
        # attaching it to root window
        scrollbar = tkinter.Scrollbar(root)

        # Adding Scrollbar to the right
        # side of root window
        scrollbar.pack(side=RIGHT, fill=BOTH)

        # Insert elements into the listbox

        for i in s3:
            listbox.insert(END, i)

            # Attaching Listbox to Scrollbar
        # Since we need to have a vertical
        # scroll we use yscrollcommand
        listbox.config(xscrollcommand=scrollbar.set)

        # setting scrollbar command parameter
        # to listbox.yview method its yview because
        # we need to have a vertical view
        scrollbar.config(command=listbox.xview)

        root.mainloop()

def va():
    global rootAP,e8
    rootAP=tkinter.Tk()
    rootAP.geometry("500x550")
    rootAP.title("TODAYS APPOINTMENTS")
    h1=tkinter.Label(rootAP,text="ENTER DATE TO VIEW APPOINTMENTS")
    h1.place(x=20,y=20)
    e8=tkinter.Entry(rootAP)
    e8.place(x=20,y=40)
    b5=tkinter.Button(rootAP,text="SEARCH",command=viewappointment)
    b5.place(x=20,y=65)
    rootAP.mainloop()