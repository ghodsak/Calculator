from tkinter import*
import tkinter as tk


def center():

    h = a.winfo_reqheight()
    w = a.winfo_reqwidth()
    ws = a.winfo_screenwidth()
    hs = a.winfo_screenheight()

    x = (ws/2)-(w/2)
    y = (hs/2)-(h/2)
    a.geometry('%dx%d+%d+%d'%(w,h,x,y))


a = tk.Tk()
center()
a.mainloop()