import tkinter as tk
from tkinter import filedialog as fd
from files import *
from tkinter.font import Font


def changed(*args):
    global cfn
    if var.get() == "new":
        t.delete("1.0", tk.END)
    if var.get() == "save as":
        fn = fd.asksaveasfilename()
        savefile(t.get("1.0", "end-1c"), fn)
        cfn = fn
    if var.get() == "open":
        fn = fd.askopenfilename()
        t.delete("1.0", tk.END)
        txt = filecont(fn)
        t.insert(tk.END, txt)
        cfn = fn
        labtext.set(getfilename(cfn))
    if var.get() == "save":
        savefile(t.get("1.0", "end-1c"), cfn)
    if var.get() == "quit":
        root.destroy()

#create a window
root = tk.Tk()
width = 600
height = 400
root.geometry(f"{width}x{height}")
root.title("text editor")
#root.resizable(False, False)

#set font
myfont = Font(family="Helvetica", size=12)
#create the option menu
var = tk.StringVar(root)
var.set("file")
opts = tk.OptionMenu(root, var, "new", "open", "save", "save as", "quit")
opts.pack(anchor="w")

#filename label
labtext = tk.StringVar()
lab = tk.Label(root, textvariable=labtext)
lab.pack(anchor="se")

#create a text space
t = tk.Text(root, width = width, height = height)
t.configure(font=myfont)
t.pack()

#option menu changing
var.trace('w', changed)






root.mainloop()
