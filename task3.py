import pyshorteners
from tkinter import *
from PIL import ImageTk

root=Tk()
root.title("URL Shortener using Python")
root.config(bg="White")

rw=550
rh=430
sw=root.winfo_screenwidth()
sh=root.winfo_screenheight()
wpos=(sw/2)-(rw/2)
hpos=(sh/2)-(rh/2)
root.geometry("%dx%d+%d+%d"%(rw,rh,wpos,hpos))
root.maxsize(2560,1600)
root.minsize(650,450)

def short():
    global s_url
    url = e1.get()
    short = pyshorteners.Shortener()
    s_url = short.tinyurl.short(url)
    L2.config(text=s_url)

def copy_select():
    global data
    data=s_url.selection_get()

ac=ImageTk.PhotoImage(file="URLshort.png")
add=Label(image=ac)
add.place(x=250,y=55)

l1=Label(root,text="Enter Your URL: ",width=0,height=0,font=("times new roman",20,"bold"))
l1.configure(bg="white",fg="black")
l1.place(x=215,y=150)
e1=Entry(root,font=(6))
e1.configure(bg="white",fg="Black")
e1.place(x=230,y=200)
b1=Button(root,text="Ok",width=10,height=0,font=("times new roman",17,"bold"),command=short)
b1.place(x=250,y=240)

l1=Label(root,text="Short link is:",width=0,height=0,font=("times new roman",20,"bold"))
l1.configure(bg="white",fg="black")
l1.place(x=240,y=300)
L2=Label(root,text="",width=28,height=0,font=("times new roman",15,"bold"))
L2.configure(bg="#BCC6CC",fg="Black")
L2.place(x=155,y=350)
b2=Button(root,text="Copy Link",width=10,height=0,font=("times new roman",12,"bold"))
b2.place(x=270,y=400)

h=Label(root,text="URL Shortener",width=0,height=0,font=("times new roman",25,"bold","italic","underline"))
h.pack(fill=X)
h.config(bg="white")
h.place(x=220,y=10)

root.mainloop()

