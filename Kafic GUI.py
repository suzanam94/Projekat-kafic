from Klase import *
from tkinter import *

root = Tk()
root.title("Suza kafe")
root.geometry("300x700")

def sto(button):
    t = Toplevel(root)
    t.geometry("150x150")
    title = button.cget("text")
    t.title(title)

    l1_t = Label(t, text = "Unesi ID proizvoda")
    l1_t.pack()

    e1_t = Entry(t)
    e1_t.pack()

    b1_t = Button(t, text = "Dodaj", command = lambda: [l2_t.configure(text = K.dodavanje(button.cget("text"),e1_t.get())),e1_t.delete(0,END)])
    b1_t.pack()

    l2_t = Label(t, text = "")
    l2_t.pack()
                  
def racun():
    t1 = Toplevel(root)
    t1.geometry("150x150")
    title = "Racun"
    t1.title(title)

    l1_t1 = Label(t1, text = "Unesi ID stola")
    l1_t1.pack()

    e1_t1 = Entry(t1)
    e1_t1.pack()

    b1_t1 = Button(t1, text = "Plati", command = lambda: [l2_t1.configure(text = K.racun(e1_t1.get())), e1_t1.delete(0,END)])
    b1_t1.pack()

    l2_t1 = Label(t1, text = "")
    l2_t1.pack()

b1 = Button(root, text = "1", width = "15" ,height = "15", command = lambda: sto(b1))
b1.grid(row=0, column=0)

b2 = Button(root, text = "2", width = "15", height = "15", command = lambda: sto(b2))
b2.grid(row=0, column=1)

b3 = Button(root, text = "3", width = "15", height = "15", command = lambda: sto(b3))
b3.grid(row=1, column=0)

b4 = Button(root, text = "4", width = "15", height = "15",command = lambda: sto(b4))
b4.grid(row=1, column=1)

b5 = Button(root, text = "Racun", width = "25", height = "10", command = lambda: racun())
b5.grid(row=2, column=0, columnspan = 2)


mainloop()
