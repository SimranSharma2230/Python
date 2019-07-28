from tkinter import *
from tkinter import messagebox
import pymysql

def get():
    stri=""
    db=pymysql.connect("localhost","root","mysql","school")
    cobj=db.cursor()
    if(div.get()==1):
        sql="select name from studentsi where avg>=60"
    elif(div.get()==2):
        sql="select name from studentsi where avg<60 and avg>=45"
    elif(div.get()==3):
        sql="select name from studentsi where avg<45 and avg>=33"
    elif(div.get()==4):
        sql="select name from studentsi where avg<33"
    cobj.execute(sql)
    res=cobj.fetchall()
    for row in res:
        name=row[0]
        stri=stri+name+","    
    db.commit()
    stri=stri[0:len(stri)-1]
    messagebox.showinfo("Students",stri)
    
root=Tk()
div=IntVar()
l1=Label(root,text="Display students on basis of following criteria")
r1=Radiobutton(root,text="First Division",variable=div,value=1)
r2=Radiobutton(root,text="Second Division",variable=div,value=2)
r3=Radiobutton(root,text="Third Division",variable=div,value=3)
r4=Radiobutton(root,text="Fail",variable=div,value=4)
b1=Button(root,text="FIND",command=get)

l1.grid(row=0,column=0,columnspan=5)
r1.grid(row=1,column=2)
r2.grid(row=2,column=2)
r3.grid(row=3,column=2)
r4.grid(row=4,column=2)
b1.grid(row=5,column=3)

root.mainloop()
