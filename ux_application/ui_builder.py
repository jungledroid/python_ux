#!/usr/local/bin/env python3
#-*- coding utf-8 -*-
from tkinter import *

def buildCommandMenu(bar):
    cmdBtn = Menubutton(bar,text="File",underline=2)
    cmdBtn.pack(side=LEFT,padx="2m")
    cmdBtn.menu = Menu(cmdBtn)
    cmdBtn.menu.add_command(label="New Project...")
    cmdBtn.menu.entryconfig(0)
    cmdBtn.menu.add_command(label="New...",background='white',activebackground='green')
    cmdBtn.menu.entryconfig(1, state=DISABLED)


    cmdBtn['menu']=cmdBtn.menu
    return cmdBtn

def buildCascadingMenu():
    pass

def buildCheckbuttonMenu():
    pass

def buildRadiobuttonMenu():
    pass

def buildDisableMenu():
    pass