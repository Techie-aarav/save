from tkinter import *
from tkinter.filedialog import asksaveasfile
#root.Tk()
from tkinter import *
window = Tk()
window.title ("Demo window")
window.geometry("400x300")
#root.geometry("400x800")
def save():
    files = ["All files" , "*.*" , "python files" , "*.py" , "text files" ,"*.txt"]
    file = asksaveasfile(filetypes = files , deafaultextension = files)
btn = Button(window , text = "save" , command = lambda:save())
btn.pack(side = TOP)
mainloop()