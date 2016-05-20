#!/usr/local/bin/env python3
# -*- coding utf-8 -*-

from tkinter import *
import tkinter.messagebox as msgbox
class App:
    def __init__(self,master):
        frame = Frame(master,name='frame',height = 200,width = 400)
        frame.pack(fill=BOTH)
        print(str(frame))
        self.quiteBtn = Button(frame,padx=50,justify=LEFT,text="Quite",background='red',command=frame.quit)
        self.quiteBtn.config(relief=SUNKEN)
        self.quiteBtn.pack(side=LEFT)
        print(str(self.quiteBtn))
        self.helloBtn = Button(frame,text="hello",command=self.sayHello)
        self.helloBtn.pack(side=BOTTOM)

        Button(frame,text='help',state=DISABLED,command=self.callHelp).pack(side=RIGHT)

    def callHelp(self):
        msgbox.showinfo('Help','no help info here!')


    def sayHello(self):
        msgbox.showinfo("info","hello,guy!")

root = Tk()
root.geometry("400x300+5+5")
app = App(root)
root.mainloop()
# root.destroy()