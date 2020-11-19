import tkinter as tk
from tkinter import ttk
from itertools import count
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

matplotlib.use("TkAgg")

##LARGE_FONT = ("Verdana", 12)
##
##class gui(tk.Tk):
##    def __init__(self):
##        tk.Tk.__init__(self)
##        container = tk.Frame(self)
##
##        container.pack(side="top", fill="both", expand = True)
##        container.grid_rowconfigure(0, weight =1)
##        container.grid_columnconfigure(0, weight = 1)
##
##        self.frames = {}
##
##        frame = StartPage(container, self)
##        self.frames[StartPage] = frame
##        frame.grid(row=0, column=0, sticky="nsew")
##
##        self.show_frame(StartPage)
##
##    def show_frame(self,cont):
##        frame = self.frames[cont]
##        frame.tkraise()
##
##class StartPage(tk.Frame):
##
##    def __init__(self, parent, controller):
##        tk.Frame.__init__(self,parent)
##        label = tk.Label(self, text="Start Page", font =LARGE_FONT) 
##        label.pack(pady=10,padx=10)
##
##        f = Figure(figsize =(5,5), dpi=100)
##
##
##        
##app = gui()
##app.mainloop()

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

plt.plot([], [], label='Channel 1')
plt.plot([], [], label='Channel 2')


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    ax = plt.gca()
    line1, line2 = ax.lines

    line1.set_data(x, y1)
    line2.set_data(x, y2)

    xlim_low, xlim_high = ax.get_xlim()
    ylim_low, ylim_high = ax.get_ylim()

    ax.set_xlim(xlim_low, (x.max() + 5))

    y1max = y1.max()
    y2max = y2.max()
    current_ymax = y1max if (y1max > y2max) else y2max

    y1min = y1.min()
    y2min = y2.min()
    current_ymin = y1min if (y1min < y2min) else y2min

    ax.set_ylim((current_ymin - 5), (current_ymax + 5))


ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.legend()
plt.tight_layout()
plt.show()
