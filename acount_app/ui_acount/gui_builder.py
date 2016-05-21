#/usr/local/bin/env python3
#-*- coding -*-
from tkinter import *
import tkinter.messagebox as toast
import logging
from acount_app.sql_controller.sql_test import *

class AccountContentBuilder:

    def __init__(self,master=None):
        self.sqliteController = SqliteContoller()

        frame = Frame(master,width=500)
        frame.pack(side=TOP,fill=BOTH)
        scrollbar = Scrollbar(frame,orient=VERTICAL)
        self.listview=Listbox(frame,background='green',height=15,yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listview.yview)
        scrollbar.pack(side=RIGHT,fill=Y)
        self.listview.pack(fill=BOTH)

        self.values = self.sqliteController.queryAll()
        self.fillContent(self.values)

        frameBottom = Frame(frame)
        frameL1 = Frame(frameBottom)
        Button(frameL1,background="grey",foreground="black",text="Show Password",command=self.showCurPwd).pack(side=LEFT)
        frameL2 = Frame(frameL1)
        frameL3 = Frame(frameL2)
        Button(frameL3,background="grey",foreground="black",text="delete acount",command=self.alertIsDeleteAccountSelected).pack()

        frameL4 = Frame(frameL2)
        Button(frameL4, background="grey", foreground="black", text="delete all",
               command=self.clearDatabase).pack()
        frameL4.pack(side=RIGHT)
        frameL3.pack(side=LEFT)
        frameL2.pack(side=RIGHT)
        frameL1.pack()
        frameBottom.pack(side=BOTTOM,fill=BOTH)

    def clearDatabase(self):
        self.sqliteController.deleteAllData()
        self.listview.delete(0,END)

    def alertIsDeleteAccountSelected(self):
        confirm = toast.showwarning("Warning", "Do you want to delete acount of %s?" % "umeng")
        logging.error("is try to confirm yes? %s"%confirm)
        if confirm == 'ok':
            self.deleteCurAccount()

    def deleteCurAccount(self):
        # toast.showwarning("Warning","Do you want to delete acount of %s?"%"umeng")
        data = list(map(int, self.listview.curselection()))
        if len(data) == 0:
            return
        logging.error("item %s" % data)
        self.listview.delete(data[0], data[-1])

    def showCurPwd(self):
        data = list(map(int, self.listview.curselection()))
        if len(data) != 1 or len(data) ==0:
            return

        toast.showinfo("Info","password %s"%self.values[data[0]][2])

    def fillContent(self,values = None):
        if not isinstance(values,list):
            toast.showinfo("warning","some error values input")
            return
        if len(values):
            self.listview.delete(0,END)
        for acountname in values:
            self.listview.insert(END,acountname[3])