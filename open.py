from subprocess import call
from tkinter import *

root = Tk(className=" HOTEL MANAGEMENT ")
root.geometry('1920x1080')


# calling functions
def click_admin():
    call(["python", "admin_login.py"])

def click_vacancy():
    call(["python", "vacancy.py"])

def click_developers():
    call(["python", "developers.py"])

def click_branches():
    call(["python", "branches.py"])

def click_contact_us():
    call(["python", "contact_us.py"])

def click_staff():
    call(["python", "staff.py"])


def click_connect():
    call(['python', 'offer.py'])


# Menu Bar
menu_bar = Menu(root)
root.config(menu=menu_bar)
home_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Home", menu=home_menu)
home_menu.add_command(label="Vacancy", command=click_vacancy)
home_menu.add_separator()
home_menu.add_command(label="Exit", command=root.quit)

about_menu = Menu(menu_bar)
menu_bar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="Branches", command=click_branches)
about_menu.add_separator()
about_menu.add_command(label="Staff", command=click_staff)
about_menu.add_separator()
about_menu.add_command(label="Developers", command=click_developers)

help_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Connect", command=click_connect)
about_menu.add_separator()
help_menu.add_command(label="Contact Us", command=click_contact_us)

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

# Buttons
adm_button = Button(root, text="Admin", bg='#000000', fg='white', font=('Orbitron', 20, 'bold'), width=30,
                    command=click_admin)
adm_button.pack(pady=10)

vac_button = Button(root, text="Customer", bg='#404040', fg='white', font=('Orbitron', 20, 'bold'), width=30, command=click_vacancy)
vac_button.pack(pady=10)

exit_button = Button(root, text="Exit", bg="#ff0000", fg="white", width=30, command=root.quit,
                     font=('Orbitron', 20, 'bold'))
exit_button.pack(pady=10)

root.mainloop()
