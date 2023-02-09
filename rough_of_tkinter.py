from tkinter import *

import tkinter

# Testing tkinter
# tkinter._test()

from tkinter import ttk



#initializing the tkinter class
carroot = Tk()

#initializing another tkinter class
# carrot = Tk()

#initializing a frame in tkinter
frame_no_1 = ttk.Frame(carroot, padding=500)
frame_no_1.grid()

#creating a label in tkinter
ttk.Label(frame_no_1, text="Hello World!").grid(column=0, row=0)
ttk.Label(frame_no_1, text="Hello World!").grid(column=1, row=0)
ttk.Label(frame_no_1, text="Hello World!").grid(column=1, row=1)
ttk.Label(frame_no_1, text="Hello World!", background='red', relief="groove").grid(column=5, row=1)

#creating a button 
bttnn = ttk.Button(frame_no_1, text="Quit", command=carroot.destroy,)
bttnn.grid(column=10, row=5)

#available configuration options 
btn = ttk.Button(frame_no_1, text=' ')
print(btn.configure().keys())

#available configuration options 
lbl = ttk.Label(frame_no_1, text=' ')
print(lbl.configure().keys())

#available methods for widgets
print(dir(btn))
print(set(dir(btn)) - set(dir(lbl)))

# setting options 
# bttnn["fg"] = "red"



carroot.mainloop()


