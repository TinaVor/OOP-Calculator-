from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk() 
window.title("Calculator") 
window.geometry('500x500')

calculator = Label(window, text='Calculator', font=("Arial 32", 24, "bold"), fg="pink")
calculator.place(x=160, y=60)

count_1 = StringVar()
count_1_entry = Entry(textvariable = count_1 , width = 10, bg="pink")
count_1_entry.place(x=100, y=170)
count_1_var = count_1_entry.get()
 
count_2 = StringVar()
count_2_entry = Entry(textvariable = count_2 , width = 10, bg = "pink")
count_2_entry.place(x=300, y=170)
count_2_var = count_2_entry.get()

box=ttk.Combobox(window, width=5, font=("Arial 32", 12, ), justify = CENTER, values=("+", "-", "*", "/")) 
box.place(x = 195, y=220)
box.set("знак")
 
count = Button(window, text = "=", height=1, width=3,  font=("Arial 32", 12), bg="pink", fg="white")
count.place(x = 205, y = 270)

f = "Arial 32", 14, "bold"
bin_ = Label(window, text="bin  = ", font=(f), fg="pink")
bin_.place(x = 100, y = 340)
dec_ = Label(window, text="dec = ", font=(f), fg="pink")
dec_.place(x = 100, y = 365)
oct_ = Label(window, text="oct  = ", font=(f), fg="pink")
oct_.place(x = 100, y = 390)
hex_ = Label(window, text="hex = ", font=(f), fg="pink")
hex_.place(x = 100, y = 415)

def Count (count_1, count_2): 
    operator = box.get() 
    count_1 = int(count_1) 
    count_2 = int(count_2)
    match operator:
        case "+": return count_1 + count_2
        case "-": return count_1 - count_2
        case "*": return count_1 * count_2
        case "/":
            if (count_2 == 0):
                messagebox.showerror(title=None, message = "Деление на ноль")
            else:
                return count_1 // count_2
 
def Result(event):
        resultbin["text"] = bin(Count(count_1_entry.get(), count_2_entry.get()))
        resultdec["text"] = Count(count_1_entry.get(), count_2_entry.get())
        resultoct["text"] = oct(Count(count_1_entry.get(), count_2_entry.get()))
        resulthex["text"] = hex(Count(count_1_entry.get(), count_2_entry.get()))

resultbin = Label(window, text = " ", font=(f), fg="pink")
resultbin.place(x = 160, y = 340)
resultdec = Label(window, text = " ", font=(f), fg="pink")
resultdec.place(x = 160, y = 365)
resultoct = Label(window, text = " ", font=(f), fg="pink")
resultoct.place(x = 160, y = 390)
resulthex = Label(window, text = " ", font=(f), fg="pink")
resulthex.place(x = 160, y = 415)

count.bind('<Button-1>', Result)

window.mainloop()
