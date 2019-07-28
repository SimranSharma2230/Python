from tkinter import *
from tkinter import messagebox
from Studentsidb import *

def goto():
    t1=int(e1.get());
    t2=e2.get();
    t3=int(e3.get());
    t4=int(e4.get());
    t5=int(e5.get());
    #avg=(t3+t4+t5)/3;
    s1=studentsi(t1,t2,t3,t4,t5)
    avg=s1.avg()
    s1.insert(avg)
    messagebox.showinfo("Data stored in database")

    
root=Tk()
l1=Label(root,text="ID")
e1=Entry(root)
l2=Label(root,text="Name")
e2=Entry(root)
l3=Label(root,text="Maths")
e3=Entry(root)
l4=Label(root,text="Hindi")
e4=Entry(root)
l5=Label(root,text="English")
e5=Entry(root)
b1=Button(root,text="SUBMIT",command=goto)

l1.grid(row=0,column=0)
e1.grid(row=0,column=2)
l2.grid(row=1,column=0)
e2.grid(row=1,column=2)
l3.grid(row=2,column=0)
e3.grid(row=2,column=2)
l4.grid(row=3,column=0)
e4.grid(row=3,column=2)
l5.grid(row=4,column=0)
e5.grid(row=4,column=2)
b1.grid(row=5,column=1)

root.mainloop()
