from tkinter import *


window = Tk()

window.title("RP")
window.geometry('500x500')

lbl = Label(window, text="Launch")

lbl.grid(column=0, row=0)

btn = Button(window, text="Launch", bg="RED")

btn.grid(column=1, row=0)

lb2 = Label(window, text="Sensor 1")
lb2.grid(column=0, row=1)
lb3 = Label(window, text="Sensor 2")
lb3.grid(column=0, row=3)
lb4 = Label(window, text="Sensor 3")
lb4.grid(column=0, row=4)


lb5 = Label(window, text="Emergency Shut down")
lb5.grid(column=0, row=5)
btn1 = Button(window, text="Emergy Shut down", bg="BLUE")

btn1.grid(column=1, row=5)


lb5 = Label(window, text="Emergency Shut down")
lb5.grid(column=0, row=5)

window.mainloop()



