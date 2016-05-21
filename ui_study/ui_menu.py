#!/usr/local/bin/env python3
# -*- coding utf-8 -*-
from tkinter import *
import logging
class AppMenu:
    def __init__(self,master=None):
        menubar = Menu(master,tearoff=0)
        fileMenu=Menu(menubar)
        fileMenu.add_command(label="Open",command=self.hello)
        fileMenu.add_separator()
        fileMenu.add_command(label="Save",command=master.quit)

        menubar.add_cascade(label="File",menu=fileMenu)
        editMenu = Menu(master)
        editMenu.add_command(label="Copy")
        editMenu.add_separator()
        editMenu.add_command(label="Paste")
        menubar.add_cascade(label="Edit",menu=editMenu)
        master.config(menu=menubar)

    def hello(self):
        print("hello")

# root = Tk()
# # appMenu = AppMenu(root)
# mMenu=Menu(root,tearoff=0)
# mMenu.add_command(label="undo")
# mMenu.add_command(label="redo")
# frame=Frame(root,width=512,height=512)
# frame.pack()
#
# def popup(event):
#     mMenu.post(event.x_root,event.y_root)
# frame.bind("<Button-3>",popup)
# root.config(menu=mMenu)
# root.mainloop()
counter = 0

def update():
    global counter
    counter = counter + 1
    menu.entryconfig(0, label=str(counter))

root = Tk()

menubar = Menu(root)
menu = Menu(menubar, tearoff=0, postcommand=update)
menu.add_command(label=str(counter))
menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Test", menu=menu)

root.config(menu=menubar)
root.mainloop()