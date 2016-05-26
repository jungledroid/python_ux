#!/usr/local/bin/env python3
#-*- coding utf-8 -*-
from tkinter import *
import tkinter.messagebox as msgbox
import logging

class BtnApp:
    def __init__(self,master=None):
        frame = Frame(master)
        frame.pack(side=TOP,fill=BOTH)
        Button(frame,background='red',text='quite',command=frame.quit).pack(fill=BOTH)

# class FrameApp:
#      def __init__(self,master=None):
#          Label(text="one").pack()
#          frame =Frame(height=2,bd=1,relief=SUNKEN)
#          frame.pack(fill=X,padx=5,pady=5)
#          Label(text="two",font=("Helvetica",13)).pack()
class ListApp:
    def __init__(self,master=None):
        frame = Frame(master)
        frame.pack(fill=X,side=TOP)
        scrollbar = Scrollbar(frame,orient=VERTICAL)
        self.listFrame= Listbox(frame,exportselection=0,foreground='red',selectmode=EXTENDED,yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listFrame.yview)
        scrollbar.pack(side=RIGHT,fill=Y)
        self.listFrame.pack(side=LEFT,fill=BOTH,expand=1)
        self.listFrame.insert(END,"a list box")
        for item in ["one","two","three","four"]:
            self.listFrame.insert(END,item)
        bframe=Frame(master)
        bframe.pack(side=BOTTOM,fill=X)
        Button(bframe,foreground='green',text="delete Top",command=self.deleteSelectItems).pack(side=BOTTOM)
        Button(bframe,foreground="blue",text="add item",command=self.addItem).pack(side=BOTTOM)
    def deleteSelectItems(self):
        data = list(map(int,self.listFrame.curselection()))
        if len(data) == 0:
            return
        logging.error("item %s"%data)
        self.listFrame.delete(data[0],data[-1])

    def addItem(self):
        self.listFrame.insert(END,"add item")

root = Tk()
root.geometry("400x300+5+5")
frame=ListApp(root)
root.mainloop()



