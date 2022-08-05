from subprocess import call
from tkinter import *
from tkinter import messagebox

def click_Main_page():
    call(["python", 'Main_page.py'])

def Ok():
    uname = e1.get()
    password = e2.get()

    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")


    elif(uname == "Admin" and password == "123"):
        messagebox.showinfo("","Login Success")
        click_Main_page()
        root.destroy()

    else :
        messagebox.showinfo("","Incorrent Username and Password")


root = Tk()
root.title("Login")
root.geometry('1920x1080')

global e1
global e2

# Title label
title_label = Label(root, text="---------  SS RESIDENCES  ---------", height=2, font=('Orbitron', 10), bg="#ff80bf")
title_label.pack(fill=X)

# Welcome label
welcome_label = Label(root, text="WELCOME", bg="purple", fg="white", font=('Orbitron', 25))
welcome_label.pack(fill=X)

blankspace = Label(root, text="\n")
blankspace.pack()

# image
image1 = PhotoImage(file="top.png")
label_for_image = Label(root, image=image1)
label_for_image.pack()

Label(root, text="UserName",  font=('Orbitron', 20), bg="#ff80bf").place(x=600, y=400)
Label(root, text="Password",  font=('Orbitron', 20), bg="#ff80bf").place(x=600, y=500)

e1 = Entry(root)
e1.place(x=750, y=400, width=200, height=39)

e2 = Entry(root)
e2.place(x=750, y=500, width=200, height=39)
e2.config(show="*")


Button(root, text="Login", command=Ok, height = 3, width = 15).place(x=700, y=600)

root.mainloop()