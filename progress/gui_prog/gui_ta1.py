from Tkinter import *
import Tkinter
import ttk
import tkFont
import tkMessageBox
import ttk
import os
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
        ##os.system("gnome-terminal -x python cmd_gps.py")
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
        os.system("sudo systemctl stop serial-getty@ttyS0.service")
        os.system("sudo systemctl disable serial-getty@ttyS0.service")
        os.system("sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock")
        tkMessageBox.showinfo("Run GPS","Run GPS berhasil")
    def run_sys():
        #execfile("progress2.py")
        os.system("gnome-terminal -x python progress_akhir.py")
    def send_data():
        os.system("gnome-terminal -x python send_new.py")
    def kill_gps():
        os.system("gnome-terminal -x python kill_gps.py")
    def cek_gps():
        os.system("gnome-terminal -x python cek_gps.py")
    def cek_aksel():
        #os.system("gnome-terminal -x python cek_accelero.py")
        os.system("sudo i2cdetect -y 1")
        
    def tambah_id():
        file = open("add_id.txt","w")
        file.write(HE.get()+','+IE.get())
        tkMessageBox.showinfo("Input Data","Input data berhasil")
        
        
   
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)

    editmenu.add_separator()

    #editmenu.add_command(label="Cut", command=donothing)
    #editmenu.add_command(label="Copy", command=donothing)
    #editmenu.add_command(label="Paste", command=donothing)
    #editmenu.add_command(label="Delete", command=donothing)
    #editmenu.add_command(label="Select All", command=donothing)

    #menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)

    root.title("Monitoring Indeks Kondisi Rel Kereta Api")
    universal_height = 500
    helv36 = tkFont.Font(family="Helvetica",size=20,weight="bold")
    helv36s = tkFont.Font(family="Helvetica",size=14)
    helv32s = tkFont.Font(family="Helvetica",size=12)

    nb = ttk.Notebook(root)

    # adding Frames as pages for the ttk.Notebook
    # first page, which would get widgets gridded into it
    page1 = ttk.Frame(nb, width= 400,height = universal_height)

    nb.add(page1, text='SETUP')


    nb.grid(column=0)


    day_label = schedGraphics.Label(page1, text="Pengaturan GPS", font=helv36s)
    day_label.pack()
    day_label.place(x=0, y=5)
    
    B = Tkinter.Button(page1, text ="Run GPS", command = test, width=10, height=2)
    B.place(x=20, y=40)
    
    D = Tkinter.Button(page1, text ="Check", command = cek_gps, width=10, height=2)
    D.place(x=150, y=40)
    
    E = Tkinter.Button(page1, text ="Stop GPS", command = kill_gps, width=10, height=2, activebackground="red")
    E.place(x=280, y=40)
    
    
    day_label = schedGraphics.Label(page1, text="Pengaturan Accelerometer", font=helv36s)
    day_label.pack()
    day_label.place(x=0, y=100)
    
    F = Tkinter.Button(page1, text ="Check", command = cek_aksel, width=10, height=2)
    F.place(x=80, y=135)
    
    F = Tkinter.Button(page1, text ="Kalibrasi", command = helloCallBack, width=10, height=2)
    F.place(x=210, y=135)
    
    H = schedGraphics.Label(page1, text="ID Petugas",font=helv32s)
    H.place(x=10,y=200)
    HE = schedGraphics.Entry(page1, bd=1)
    HE.place(x=100, y=200)
    
    I = schedGraphics.Label(page1, text="ID Rute",font=helv32s)
    I.place(x=10,y=235)
    IE = schedGraphics.Entry(page1, bd=1)
    IE.place(x=100, y=235)
    
    J = Tkinter.Button(page1, text ="Tambahkan", command = tambah_id, width=10, height=2)
    J.place(x=280, y=208)
    
    
    K = Tkinter.Button(page1,text="Run Program", width =20, height=4, command = run_sys)
    K.place(x=5, y=300)

    L = Tkinter.Button(page1,text="Send Data", width =20, height=4, command = send_data)
    L.place(x=205, y=300)


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
    canvas.get_tk_widget().grid(column= 12, row=0)



    def animate(i):
        graph_data = open('log.txt', 'r',os.O_NONBLOCK).read()
        lines = graph_data.split('\n')
        batas = len(lines)-10
        ix = []
        xs = []
        ys = []
        zs = []
        vs = []
        for line in lines[batas:]:
            if len(line) > 1:
                i, x, y, z, v, lat, lon, epx, waktu = line.split(',')
                ix.append(int(i))
                xs.append(float(x))
                ys.append(float(y))
                zs.append(float(z))
                vs.append(float(v))
            ax1.clear()
            ax1.plot(ix, ys, label="Horizontal", marker='o')
            ax1.plot(ix, zs, label="Vertikal", marker='o')
            ax1.plot(ix, xs, label="Lateral", marker='o', color="green")
            ax1.set_ylim(-2, 2)
            ax1.set_ylabel('Nilai getar (g)', fontsize=8)
            ax1.legend()
            ax1.set_title("Grafik getaran")
            ax2.clear()
            ax2.plot(ix, vs, label="kecepatan aktual", marker='o', color='yellow')
            ax2.set_ylim(0,100)
            ax2.set_xlabel('Data ke-', fontsize=8)
            ax2.set_ylabel('Nilai keceoatan(km/jam)', fontsize=8)
            ax2.legend()
            ax2.set_title("Grafik kecepatan")



    ani = animation.FuncAnimation(fig, animate, interval=100)
    # plt.show()

    root.mainloop()

if __name__ == "__main__":
    demo()
