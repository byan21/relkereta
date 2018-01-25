#!/usr/bin/python

import Tkinter
import tkMessageBox
import os
import sys
from time import *
import time


def helloCallBack():
    tkMessageBox.showinfo( "Hello Python", "Hello World")
def client_exit():
    #B["text"]="holla"
    #
    B["command"]=tes
    while(1):
        C = Tkinter.Button(top, text ="Holla", command = tes)
        C.pack()
        print 'ok'
        time.sleep(1)
        

    
        
    #exit()



#def main():
def tes():
    B["text"]="tes"
    


if __name__ == '__main__':
    top = Tkinter.Tk()
    top.title('coba')
    top.resizable(width=True, height=True)
    top.geometry("400x300")
    B = Tkinter.Button(top, text ="Hello", command = client_exit)
    #B.place()
    B.pack()
    top.mainloop()