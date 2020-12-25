from tkinter import *
from tkinter import messagebox
import tkinter.font as font

root = Tk()
root.title('Todo List')
root.geometry('300x350')
root.configure(background='grey')

todo = []

counter = 1

def submit():
    global counter
    text = taskEntry.get() + "\n"
    if text == "\n":
        messagebox.showerror("Text field error.", "You must enter the task to add.")
    else:
        todo.append(text)
        textField.insert('end -1  chars', str(counter) + ") " + text)
        counter += 1
    taskEntry.delete(0, END)

def delete():
    global counter
    num = numField.get(1.0, END)
    if num == "\n" or len(todo) == 0:
        messagebox.showerror("Number field error.", "You must enter a number to delete the existing task.")
    else:
        numField.delete(0.0, END)
        todo.pop(int(num) - 1)
        counter -= 1
        textField.delete(1.0, END)
        for i in range(len(todo)):
            textField.insert('end -1 chars', str(i+1) + ") " + todo[i])


entryLabel = Label(root, text="Enter a task to add in the list !", padx=10, pady=2, bg='grey', font=font.Font(family='Times', size='14', weight='bold'))
entryLabel.pack()
taskEntry = Entry(root, width=40)
taskEntry.pack(padx=10, pady=2)
submitBtn = Button(root, text="Submit", bg='lightgrey', command=submit)
submitBtn.pack( padx=10, pady=2)
deleteLabel = Label(root, text="Delete a task of number :", padx=10, pady=2, bg='grey', font=font.Font(family='Times', size='14', weight='bold'))
deleteLabel.pack()
numField = Text(root, height=1, width=4)
numField.pack( padx=10, pady=2)
deleteBtn = Button(root, text="Delete the task.", bg='lightgrey', command=delete)
deleteBtn.pack( padx=10, pady=2)
textField = Text(root, height=11, width=30)
textField.pack()

root.mainloop()