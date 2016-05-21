#!/usr/local/bin/env python3
#-*- coding utf-8 -*-
from tkinter import *
import tkinter.messagebox as toast
import logging
from acount_app.ui_acount.gui_builder import *
root = Tk()
root.geometry("500x400+5+5")
root.title("Account Management")
content = AccountContentBuilder(root)
root.mainloop()

