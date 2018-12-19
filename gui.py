import tkinter as tk
def changed(*args):
    print(var.get())

#create a window
root = tk.Tk()
root.geometry("600x400")
root.title("text editor")
root.resizable(False, False)

#create the oprion menu
var = tk.StringVar(root)
var.set("file")
opts = tk.OptionMenu(root, var, "save", "new")
opts.pack(anchor="w")


#create a text space
t = tk.Text(root)
t.pack()

var.trace('a', changed)




root.mainloop()
