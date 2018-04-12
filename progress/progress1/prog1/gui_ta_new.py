from Tkinter import *
import Tkinter
import ttk
import tkFont
import tkMessageBox
import ttk
import os
import sys
from subprocess import call
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import matplotlib.gridspec as gridspec





def demo():
    #root = tk.Tk()
    schedGraphics = Tkinter
    root = schedGraphics.Tk()
    root.style=ttk.Style()
    root.style.theme_use("clam")
    
    
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
    def run_sys():
        #execfile("progress2.py")
        os.system("gnome-terminal -x python progress2.py")
   
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

    root.title("Dasboard Indek Rel")
    universal_height = 500
    helv36 = tkFont.Font(family="Helvetica",size=20,weight="bold")
    helv36s = tkFont.Font(family="Helvetica",size=14)

    nb = ttk.Notebook(root)

    # adding Frames as pages for the ttk.Notebook
    # first page, which would get widgets gridded into it
    page1 = ttk.Frame(nb, width=400,height = universal_height)
    # second page
    page2 = ttk.Frame(nb,width = 400,height = universal_height)

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
    
    G = Tkinter.Button(page2, text ="Start", command = run_sys, width=16, height=4)
    G.place(x=80, y=140)
    
    day_label = schedGraphics.Label(page2, text="Kirim data", font=helv36s)
    day_label.pack()
    day_label.place(x=0, y=220)
    
    G = Tkinter.Button(page2, text ="Kirim", command = helloCallBack, width=16, height=4)
    G.place(x=80, y=260)
    style.use('ggplot')
    # plt.ion()
    fig = plt.figure()
    #fig.canvas._master.geometry('900x800+0+0')
    gs1 =gridspec.GridSpec(2,1)
    plt.subplots_adjust(bottom = 0.5, hspace = 1)
    #ax1 = fig.add_subplot(2, 1, 1)
    #ax2 = fig.add_subplot(2, 1, 2)
    ax1 = fig.add_subplot(gs1[0])
    ax2 = fig.add_subplot(gs1[1])
    plt.subplots_adjust(bottom=0.1, left = 0.5, wspace = 0.1)
    gs1.tight_layout(fig, rect=[0,0,1,0.9])
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(column= 4, row=0)
    
    

    # canvas_free.create_rectangle(10, 50 , 300, 600, fill="red")

    # canvas_free.grid(column=10, row=0)


    def animate(i):
        graph_data = open('number.txt', 'r',os.O_NONBLOCK).read()
        lines = graph_data.split('\n')
        batas = len(lines)-5
        ix = []
        xs = []
        ys = []
        zs = []
        vs = []
        for line in lines[batas:]:
            if len(line) > 1:
                i, x, y, z, v, lat, lon = line.split(',')
                ix.append(int(i))
                xs.append(float(x))
                ys.append(float(y))
                zs.append(float(z))
                vs.append(float(v))
            ax1.clear()
            ax1.plot(ix, ys, label="Horizontal", marker='o')
            ax1.plot(ix, zs, label="Vertikal", marker='o')
            ax1.plot(ix, xs, label="Depan", marker='o', color="yellow")
            ax1.set_ylim(-2, 2)
            ax1.set_ylabel('Nilai getar (g)', fontsize=8)
            ax1.legend()
            ax1.set_facecolor('black')
            ax1.set_title("Grafik getaran")
            ax2.clear()
            ax2.plot(ix, vs, label="kecepatan aktual", marker='o', color='yellow')
            ax2.set_ylim(0,100)
            ax2.set_xlabel('Data ke-', fontsize=8)
            ax2.set_ylabel('Nilai keceoatan(km/h)', fontsize=8)
            ax2.legend()
            ax2.set_facecolor('black')
            ax2.set_title("Grafik kecepatan")

    ani = animation.FuncAnimation(fig, animate,  interval=1, repeat=True)
    # plt.show()

    root.mainloop()

if __name__ == "__main__":
    try:
        demo()
    except:
        sys.exit(0) #exit bro 
        root.destroy()
