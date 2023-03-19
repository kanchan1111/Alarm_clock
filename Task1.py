from tkinter import *
from tkinter import messagebox
import time
import threading
from pygame import mixer

root = Tk()
root.title("Alarm")
root.geometry("550x350")
root.config(bg="#494D5F")

mixer.init()


def th():
    t1 = threading.Thread(target=a, args=())
    t1.start()


def a():
    a = hr.get()
    if a == "":
        msg = messagebox.showerror('Invalid data', 'Please enter valid time')
    else:
        Alarmtime = a
        CurrentTime = time.strftime("%H:%M")

        while Alarmtime != CurrentTime:
            CurrentTime = time.strftime("%H:%M")

        if Alarmtime == CurrentTime:
            mixer.music.load('Alarm_Clock.mp3')
            mixer.music.play()
            msg = messagebox.showinfo('It is time', f'{amsg.get()}')
            if msg == 'ok':
                mixer.music.stop()


header = Frame(root)
header.place(x=5, y=5)

head = Label(root, text="ALARM CLOCK",bg="#A0D2EB", font=('times new roman', 20, "bold"))
head.pack(fill=X)

console = Frame(root)
console.place(x=25, y=75)

acc = PhotoImage(file='Alarm_Clock.png')

ac = Label(console, image=acc)
ac.grid(rowspan=4, column=0)

atime = Label(console, text="Alarm Time \n(Hr:Min)", font=('times new roman', 18))
atime.grid(row=0, column=1, padx=10, pady=5)

hr = Entry(console, font=('times new roman', 20), width=5)
hr.grid(row=0, column=2, padx=10, pady=5)

amessage = Label(console, text="Message", font=('times new roman', 20))
amessage.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

amsg = Entry(console, font=('times new roman', 15), width=25)
amsg.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

start = Button(console, text="Set Alarm", font=('times new roman', 20), command=th)
start.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

root.mainloop()