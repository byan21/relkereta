from Tkinter import *
import Tkinter
import ttk
import tkFont
import tkMessageBox
import os
from subprocess import call 


def demo():
    #root = tk.Tk()
    schedGraphics = Tkinter
    root = schedGraphics.Tk()
    
    def donothing():
        filewin = Toplevel(root)
        button = Button(filewin, text="Do nothing button")
        button.pack()
    def helloCallBack():
        tkMessageBox.showinfo( "Hello Python", "Hello World")
    def test():
        os.system("gnome-terminal -x python cmd_gps.py")
##        os.system("python cmd_gps.py")
##        os.system("sudo systemctl stop gpsd.socket")
##        os.system("sudo systemctl disable gpsd.socket")
##        s.system("sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock")
##        os.system("cgps -s")
##        call(["sudo systemctl stop gpsd.socket"])
##        call(["sudo systemctl disable gpsd.socket"])
##        call(["sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock"])
##        call(["cgps -s"])
##        call(["python", "cmd_gps.py"])
        
   
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)

    editmenu.add_separator()

    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)

    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)

    root.title("Testing Bot")
    universal_height = 500
    helv36 = tkFont.Font(family="Helvetica",size=20,weight="bold")
    helv36s = tkFont.Font(family="Helvetica",size=14)

    nb = ttk.Notebook(root)

    # adding Frames as pages for the ttk.Notebook
    # first page, which would get widgets gridded into it
    page1 = ttk.Frame(nb, width= 300,height = universal_height)
    # second page
    page2 = ttk.Frame(nb,width = 300,height = universal_height)

    nb.add(page1, text='SETUP')
    nb.add(page2, text='RUN')

    nb.grid(column=0)

    day_label = schedGraphics.Label(page1, text="SETUP GPS", font=helv36)
    day_label.pack()
    day_label.place(x=0, y=5)
    
    day_label = schedGraphics.Label(page1, text="Pilih Tipe install", font=helv36s)
    day_label.pack()
    day_label.place(x=0, y=35)
    
    B = Tkinter.Button(page1, text ="USB", command = test, width=10, height=2)
    B.place(x=20, y=65)
    
    C = Tkinter.Button(page1, text ="UART", command = helloCallBack, width=10, height=2)
    C.place(x=140, y=65)
    
    day_label = schedGraphics.Label(page1, text="Check GPS", font=helv36s)
    day_label.pack()
    day_label.place(x=0, y=115)
    
    D = Tkinter.Button(page1, text ="Check", command = helloCallBack, width=10, height=2)
    D.place(x=80, y=145)
    
    day_label = schedGraphics.Label(page1, text="Kill GPS", font=helv36s)
    day_label.pack()
    day_label.place(x=0, y=195)
    
    E = Tkinter.Button(page1, text ="Kill", command = helloCallBack, width=10, height=2, activebackground="red")
    E.place(x=80, y=225)
    
    day_label = schedGraphics.Label(page1, text="SETUP ACCELERO", font=helv36)
    day_label.pack()
    day_label.place(x=0, y=285)
    
    day_label = schedGraphics.Label(page1, text="Check Accelero", font=helv36s)
    day_label.pack()
    day_label.place(x=0, y=315)
    
    F = Tkinter.Button(page1, text ="Check", command = helloCallBack, width=10, height=2)
    F.place(x=80, y=345)
    
    day_label = schedGraphics.Label(page1, text="Kalibrasi Accelero", font=helv36s)
    day_label.pack()
    day_label.place(x=0, y=390)
    
    F = Tkinter.Button(page1, text ="Kalibrasi", command = helloCallBack, width=10, height=2)
    F.place(x=80, y=420)
    


    day_label = schedGraphics.Label(page2, text="Program Utama", font=helv36)
    day_label.pack()
    day_label.place(x=0, y=30)
    
    day_label = schedGraphics.Label(page2, text="Start/stop", font=helv36s)
    day_label.pack()
    day_label.place(x=0, y=100)
    
    G = Tkinter.Button(page2, text ="Start", command = helloCallBack, width=16, height=4)
    G.place(x=80, y=140)
    
    day_label = schedGraphics.Label(page2, text="Kirim data", font=helv36s)
    day_label.pack()
    day_label.place(x=0, y=220)
    
    G = Tkinter.Button(page2, text ="Kirim", command = helloCallBack, width=16, height=4)
    G.place(x=80, y=260)
    
    
    canvas = schedGraphics.Canvas(root, width=900, height=universal_height)
    canvas.create_rectangle(50, 500, 300, 600, fill="red")
    canvas.grid(column=1, row=0)

    root.mainloop()

if __name__ == "__main__":
    demo()