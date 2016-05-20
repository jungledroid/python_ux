#!/usr/local/bin/env python3
#-*- coding utf-8 -*-
from tkinter import  *
from ux_application.ui_builder import *
root = Tk()
root.title("chat with me")
root.geometry("600x400+300+300")
mBar = Frame(root,relief=RAISED,borderwidth=5)
mBar.pack(fill=X)
cmdButton = buildCommandMenu(mBar)
casBtn = buildCascadingMenu()
chkBtn = buildCheckbuttonMenu()
radioBtn = buildRadiobuttonMenu()
disableBtn = buildDisableMenu()

mBar.tk_menuBar(cmdButton,casBtn,chkBtn,radioBtn,disableBtn)
root.mainloop()