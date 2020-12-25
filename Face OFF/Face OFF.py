from tkinter import *
import tkinter.font as font
import random
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Face OFF")
root.configure(background='grey')

counter = 0

def click(b1, b2, b):
    global counter
    if b["text"] == "🡱":
        b1["text"] = "🡱"
    elif b["text"] == "🡳":
        b1["text"] = "🡳"
    elif b["text"] == "🡰":
        b1["text"] = "🡰"
    elif b["text"] == "🡲":
        b1["text"] = "🡲"
    else :
        b1["text"] = "•"

    n = random.randint(1, 5)
    if n == 1:
        b2["text"] = "🡱"
    elif n == 2:
        b2["text"] = "🡳"
    elif n == 3:
        b2["text"] = "🡰"
    elif n == 4:
        b2["text"] = "🡲"
    else :
        b2["text"] = "•"

    if b1["text"] != b2["text"]:
        counter +=1
    else :
        messagebox.showinfo("Face OFF", "You got " + str(counter) + " points.")
        counter = 0
        b1["text"] = ""
        b2["text"] = ""


mylbl = Label(root, text="Enter your name : ", font=font.Font(family='Times', size='14', weight='bold'), bg='grey')
mylbl.grid(row=0, column=0, columnspan=3)
name = Entry(root)
name.grid(row=0, column=3, columnspan=3)
btn1 = Button(root, text="", image="", height=10, width=20)
btn1.grid(row=1, column=0, padx=2, pady=4, columnspan=3)
btn2 = Button(root, text="", image="", height=10, width=20)
btn2.grid(row=1, column=3, padx=2, pady=4, columnspan=3)
btn_up = Button(root, text="🡱" , command=lambda:click(btn1, btn2, btn_up), height=2, width=4)
btn_up.grid(row=2, column=1)
btn_down = Button(root, text="🡳" , command=lambda:click(btn1, btn2, btn_down), height=2, width=4)
btn_down.grid(row=4, column=1)
btn_left = Button(root, text="🡰" , command=lambda:click(btn1, btn2, btn_left), height=2, width=4)
btn_left.grid(row=3, column=0)
btn_right = Button(root, text="🡲" , command=lambda:click(btn1, btn2, btn_right), height=2, width=4)
btn_right.grid(row=3, column=2)
btn_straight = Button(root, text="•" , command=lambda:click(btn1, btn2, btn_straight), height=2, width=4)
btn_straight.grid(row=3, column=1, pady=4)
photo = PhotoImage(file = r"face.png")
Label(root, image = photo, bg="grey").grid(row=3, column=4)

root.mainloop()