from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")

check = True
count = 0

def button(btns):
    global check, count
    if btns["text"] == "" and check == True :
        btns["text"] = "X"
        check = False
        count += 1
        winner()

    elif btns["text"] == "" and check == False :
        btns["text"] = "O"
        check = True
        count += 1
        winner()

    else:
        messagebox.showerror("Tic Tac Toe.","Already clicked.")

def winner():
    if (btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
            btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X' or
            btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X' or
            btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X' or
            btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X' or
            btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X' or
            btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X' or
            btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X'):
        messagebox.showinfo("Tic Tac Toe", "Player X wins.")
        restart(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    elif (btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
          btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or
          btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O' or
          btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or
          btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O' or
          btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or
          btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O' or
          btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O'):
        messagebox.showinfo("Tic Tac Toe", "Player O wins.")
        restart(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    elif (count == 9):
        messagebox.showinfo("Tic Tac Toe.", "It's a tie.")
        restart(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)

def restart(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9):
    global count, check
    btn1["text"] = ""
    btn2["text"] = ""
    btn3["text"] = ""
    btn4["text"] = ""
    btn5["text"] = ""
    btn6["text"] = ""
    btn7["text"] = ""
    btn8["text"] = ""
    btn9["text"] = ""
    count = 0
    check = True

p1 = Label(root, text="Player X : ", height=1, width=8)
p1.grid(row=1, column=0)
p1e = Entry(root)
p1e.grid(row=1, column=1, columnspan=8)
p2 = Label(root, text="Player O : ", height=1, width=8)
p2.grid(row=2, column=0, pady=5)
p2e = Entry(root)
p2e.grid(row=2, column=1, columnspan=8, pady=5)


btn1 = Button(root, text="", command=lambda:button(btn1), height=5, width=10)
btn1.grid(row=3, column=0)
btn2 = Button(root, text="", command=lambda:button(btn2), height=5, width=10)
btn2.grid(row=3, column=1)
btn3 = Button(root, text="", command=lambda:button(btn3), height=5, width=10)
btn3.grid(row=3, column=2)
btn4 = Button(root, text="", command=lambda:button(btn4), height=5, width=10)
btn4.grid(row=4, column=0)
btn5 = Button(root, text="", command=lambda:button(btn5), height=5, width=10)
btn5.grid(row=4, column=1)
btn6 = Button(root, text="", command=lambda:button(btn6), height=5, width=10)
btn6.grid(row=4, column=2)
btn7 = Button(root, text="", command=lambda:button(btn7), height=5, width=10)
btn7.grid(row=5, column=0)
btn8 = Button(root, text="", command=lambda:button(btn8), height=5, width=10)
btn8.grid(row=5, column=1)
btn9 = Button(root, text="", command=lambda:button(btn9), height=5, width=10)
btn9.grid(row=5, column=2)
re = Button(root, text="Restart", command=lambda:restart(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9), height=2, width=4, padx=10)
re.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()