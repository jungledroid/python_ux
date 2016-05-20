#!/usr/local/bin/env python3
#-*- coding utf-8 -*-
from tkinter import  *
from ux_application.ui_builder import *
root = Tk()
root.title("chat with me")
root.geometry("600x400+300+300")
mBar = Frame(root,relief=RAISED,borderwidth=100)
mBar.pack(fill=X)
cmdButton = buildCommandMenu(mBar)
casBtn = buildCascadingMenu()
chkBtn = buildCheckbuttonMenu()
radioBtn = buildRadiobuttonMenu()
disableBtn = buildDisableMenu()

mBar.tk_menuBar(cmdButton,casBtn,chkBtn,radioBtn,disableBtn)

# Label(root,text="l1",bg="red").pack(fill=BOTH,side=TOP)
# Label(root,text="l2",bg="green").pack(fill=BOTH,side = RIGHT)
# Label(root,text="l3",bg="blue").pack(fill=X)
# Label(root,text="l4",bg="yellow").pack(fill=X,side=BOTTOM)
root.mainloop()