from tkinter import *
import tkinter.messagebox as tmsg
import os
import time
from math import *
import tkinter.ttk as ttk


def getvals(event):
    value = event.widget.cget("text")
    if value == "Clr":
        screen_var.set("")
    elif value == "=":
        try:
            screen_var.set(eval(screen.get()))
            screen.update()
        except:
            screen_var.set("Syntax error")
            screen.update()
            # status_var.set("Preparing...")
            # screen.update()
            time.sleep(1)
            screen_var.set("")
            screen.update()

    else:
        screen_var.set(f"{screen_var.get()}{value}")


root = Tk()
theme = ttk.Style()
theme.theme_use("alt")
# root.geometry(f"{canvas_width}x{canvas_height}")
# root.maxsize(canvas_width, canvas_height)
# root.minsize(canvas_width, canvas_height)
root.title("Scientific Calculator ")
root.call("wm", "iconphoto", root._w, PhotoImage(file="calculator.png"))

"""
my_menu = Menu(root)
m1 = Menu(my_menu, tearoff=0, fg="red")
m1.add_command(label="Terms of Use", command=term_of_use)
m1.add_command(label="Send Feedback", command=send_feedback)
root.config(menu=my_menu)
my_menu.add_cascade(label=" About ", menu=m1)
"""
# my_menu.add_command(label='Exit',command=quit)


screen_var = StringVar()
screen = Entry(
    root,
    textvariable=screen_var,
    font="Helvetica 35 italic",
    fg="green",
    bg="black",
    borderwidth=10,
)
screen.pack(pady=20)


f = Frame(root)
f.pack()
b1 = Button(
    f,
    text="7",
    font="Algerian 15 italic",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b2 = Button(
    f,
    text="8",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b3 = Button(
    f,
    text="9",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b4 = Button(
    f,
    text="*",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b5 = Button(
    f,
    text="sin",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b6 = Button(
    f,
    text="(",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b1.bind("<Button-1>", getvals)
b2.bind("<Button-1>", getvals)
b3.bind("<Button-1>", getvals)
b4.bind("<Button-1>", getvals)
b5.bind("<Button-1>", getvals)
b6.bind("<Button-1>", getvals)
buttons = [b1, b2, b3, b4, b5, b6]
count = 0
for i in range(6):
    buttons[count].grid(row=1, column=i)
    count += 1


f = Frame(root)
f.pack()
b1 = Button(
    f,
    text="4",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b2 = Button(
    f,
    text="5",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b3 = Button(
    f,
    text="6",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b4 = Button(
    f,
    text="-",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b5 = Button(
    f,
    text="cos",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b6 = Button(
    f,
    text=")",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)


b1.bind("<Button-1>", getvals)
b2.bind("<Button-1>", getvals)
b3.bind("<Button-1>", getvals)
b4.bind("<Button-1>", getvals)
b5.bind("<Button-1>", getvals)
b6.bind("<Button-1>", getvals)
buttons = [b1, b2, b3, b4, b5, b6]
count = 0
for i in range(6):
    buttons[count].grid(row=2, column=i)
    count += 1
f = Frame(root)
f.pack()
b1 = Button(
    f,
    text="1",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b2 = Button(
    f,
    text="2",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b3 = Button(
    f,
    text="3",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b4 = Button(
    f,
    text="+",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b5 = Button(
    f,
    text="tan",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b6 = Button(
    f,
    text="%",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)


b1.bind("<Button-1>", getvals)
b2.bind("<Button-1>", getvals)
b3.bind("<Button-1>", getvals)
b4.bind("<Button-1>", getvals)
b5.bind("<Button-1>", getvals)
b6.bind("<Button-1>", getvals)
buttons = [b1, b2, b3, b4, b5, b6]
count = 0
for i in range(6):
    buttons[count].grid(row=3, column=i)
    count += 1
f = Frame(root)
f.pack()
b1 = Button(
    f,
    text=".",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b2 = Button(
    f,
    text="0",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b3 = Button(
    f,
    text="sinh",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b4 = Button(
    f,
    text="cosh",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b5 = Button(
    f,
    text="tanh",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b6 = Button(
    f,
    text="pi",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b1.bind("<Button-1>", getvals)
b2.bind("<Button-1>", getvals)
b3.bind("<Button-1>", getvals)
b4.bind("<Button-1>", getvals)
b5.bind("<Button-1>", getvals)
b6.bind("<Button-1>", getvals)
buttons = [b1, b2, b3, b4, b5, b6]
count = 0
for i in range(6):
    buttons[count].grid(row=4, column=i)
    count += 1
f = Frame(root)
f.pack()

b1 = Button(
    f,
    text="log10",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b2 = Button(
    f,
    text="exp",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b3 = Button(
    f,
    text="/",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b4 = Button(
    f,
    text="Clear",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b5 = Button(
    f,
    text="log",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)

b6 = Button(
    f,
    text="=",
    font="Helvetica 15 bold",
    padx=20,
    pady=20,
    borderwidth=3,
    fg="green",
    bg="black",
    width=3,
)


b1.bind("<Button-1>", getvals)
b2.bind("<Button-1>", getvals)
b3.bind("<Button-1>", getvals)
b4.bind("<Button-1>", getvals)
b5.bind("<Button-1>", getvals)
b6.bind("<Button-1>", getvals)
buttons = [b1, b2, b3, b4, b5, b6]
count = 0
for i in range(6):
    buttons[count].grid(row=5, column=i)
    count += 1
root.mainloop()
