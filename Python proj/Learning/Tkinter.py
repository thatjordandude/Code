from tkinter import *
root = Tk()

#Entry widget
entry = Entry(root, width = 50, borderwidth=14)
entry.pack()
entry.insert(0, 'Enter your name')

def click():
    hello = 'Hello ' + entry.get()
    mylabel = Label(root, text = hello)
    mylabel.pack()

mybutton = Button(root, text='Submit', command=click, width=10, height=10)
# mybutton2 = Button(root, text='clickme', state=DISABLED)
mybutton.pack()
# mybutton2.pack()

# Packing it in the first avaliable spot
# myLabel1.grid(row=0, column=8)
# myLabel2.grid(row=1, column=5)

# Col and rows are subjective

root.mainloop()
