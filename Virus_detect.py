from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("300x200")
def msg():
    messagebox.showwarning("Halt! Virus detected!")
button = Button(window, text = "Scan", command = msg)
button.place(x= 40, y = 40)
window.mainloop()