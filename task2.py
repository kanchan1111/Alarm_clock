from tkinter import *
import random
import smtplib
from PIL import Image, ImageTk

root=Tk()
root.title("Email OTP Verification")
root.config(bg="#583759")

rw=550
rh=430
sw=root.winfo_screenwidth()
sh=root.winfo_screenheight()
wpos=(sw/2)-(rw/2)
hpos=(sh/2)-(rh/2)
root.geometry("%dx%d+%d+%d"%(rw,rh,wpos,hpos))
root.maxsize(2560,1600)
root.minsize(650,450)

def generate_otp():
    return str(random.randint(100000, 999999))

def send_email(email, otp):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("Email ID", "password")
    message = otp+" is your One Time Password (OTP) for OTP Verifier application. "
    server.sendmail('Mail for You', email, message)
    server.quit()

def verify_otp():
    user_otp = e2.get()
    if user_otp == otp:
        L2.config(text='OTP Verified', fg='green')
    else:
        L2.config(text='OTP Incorrect', fg='red')

def send_otp():
    global otp
    otp = generate_otp()
    email = e1.get()
    send_email(email, otp)
    L1.config(text='OTP sent successfully!')

ac=ImageTk.PhotoImage(file="OTPVeri.png")
add=Label(image=ac)
add.place(x=270,y=75)

l1=Label(root,text="Enter Your Email ID:",width=0,height=0,font=("times new roman",15))
l1.configure(bg="#DCD0FF",fg="black")
l1.place(x=40,y=220)
e1=Entry(root,font=(5))
e1.configure(bg="white",fg="Black")
e1.place(x=250,y=225)
b1=Button(root,text="Send OTP",width=10,height=0,font=(30),command=send_otp)
b1.config(bg="white",fg="Blue")
b1.place(x=500,y=220)
L1=Label(root,text=" ",width=0,height=0,font=("times new roman",8))
L1.configure(bg="#DCD0FF",fg="black")
L1.place(x=300,y=260)

l3=Label(root,text="Enter 6-digit OTP:",width=0,height=0,font=("times new roman",15))
l3.configure(bg="#DCD0FF",fg="black")
l3.place(x=40,y=300)
e2=Entry(root,font=(5))
e2.configure(bg="white",fg="Black")
e2.place(x=250,y=305)
b1=Button(root,text="Verify OTP",width=10,height=0,font=(30),command=verify_otp)
b1.config(bg="white",fg="Blue")
b1.place(x=500,y=300)
L2=Label(root,text=" ",width=0,height=0,font=("times new roman",8))
L2.configure(bg="#DCD0FF",fg="black")
L2.place(x=300,y=340)

head = Label(root, text="Email OTP Verification",bg="#DCD0FF", font=('times new roman', 20, "bold","italic","underline"))
head.pack(fill=X)
head.place(x=190,y=20)

root.mainloop()