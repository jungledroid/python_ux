#!/usr/local/bin/env python3
#-*- coding utf-8 -*-
from tkinter import *
import tkinter.messagebox as toast
class DefaultEntry:
    def __init__(self,master=None):
        e = Entry(master)
        e.pack()
        e.delete(0,END)
        e.insert(0,"a default text")
# bind a StringVar instance
class StringEntry:
    def __init__(self,master=None):
        v = StringVar()
        e = Entry(master,textvariable=v)
        e.pack()
        v.set("a string var set text")
        print(v.get())

class PrintButtonEntry:
    def __init__(self,master=None):
        self.e = Entry(master)
        self.e.pack()
        # self.e.insert(0,"hello entry")
        self.e.focus_set()
        self.b = Button(master,text="get",command=self.callback)
        self.b.pack()
    def callback(self):
        print(self.e.get())
        if self.e.get():
            toast.showinfo("input",self.e.get())
root = Tk()
# DefaultEntry(root)
# StringEntry(root)
# PrintButtonEntry(root)
root.mainloop()
