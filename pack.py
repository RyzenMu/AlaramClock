import tkinter


from tkinter import *

from tkinter import ttk

# initializing tkinter instance 
root = Tk()

# creating frame widget
frame_no_2 = ttk.Frame(root, padding=100)
frame_no_2.pack(side="right")

# creating label widget within frame widget
labl = ttk.Label(frame_no_2, text="hello Worls no 2")
labl.pack(side="right")

labl = ttk.Label(frame_no_2, text="hello World - left")
labl.pack(side="left")

labl = ttk.Label(frame_no_2, text="hello World - bottom")
labl.pack(side="top")

root.mainloop()


