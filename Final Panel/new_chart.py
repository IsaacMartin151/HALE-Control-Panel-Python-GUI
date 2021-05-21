from random import randint
import tkinter as tk
import datetime as dt
import element
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.pyplot as plt

class Chart(element.Element):
    def __init__(self, *, title = "Chart title", font="Arial Bold", xlabel="Time", max_points = 10,  lines = [("Series 1", "#FF0000")], ylabel="Pressure", text_color="black", get_data = None, font_size = 24,  **kwargs):
        #self.figure1 = None
        self.lines = lines
        self.get_data = get_data
        self.title = title
        self.text_color = text_color
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.font_size = font_size
        self.max_points = max_points
        self.font = font
        self.x_data = []
        self.y_data = [[] for line in range(len(lines))]
        super().__init__(**kwargs)

        

    def display_content(self):
        self.figure = Figure(figsize=(4,3), dpi=80, facecolor="#777777")

        self.subplot = self.figure.add_subplot(1, 1, 1, facecolor='#CACACA')
        self.subplot.set_xlabel(self.xlabel, color=self.text_color)
        self.subplot.set_ylabel(self.ylabel, color=self.text_color)
        self.scatter = FigureCanvasTkAgg(self.figure, self.containing_frame)
        #print("placing plot")
        self.scatter.get_tk_widget().pack(expand=True, fill="both")
        ani = animation.FuncAnimation(self.figure, self.update, interval=self.refresh_interval)

    def update(self):
        if(self.get_data):
            new_data = self.get_data()
            time = dt.datetime.now().strftime('%H:%M:%S.%f')
            time = time[:-4]
            self.x_data.append(time)
            if (len(self.x_data) > self.max_points):
                self.x_data = self.x_data[-self.max_points:]
            for line_idx, value in enumerate(new_data):
                self.y_data[line_idx].append(value)
                if (len(self.y_data[line_idx]) > self.max_points):
                    self.y_data[line_idx] = self.y_data[line_idx][-self.max_points:]
        self.subplot.clear()
        self.subplot.set_title(self.title)
        self.subplot.set_xlabel(self.xlabel, color=self.text_color)
        self.subplot.set_ylabel(self.ylabel, color=self.text_color)
        for line_idx, line in enumerate(self.lines):
            self.subplot.plot(self.x_data, self.y_data[line_idx], label = line[0], color=line[1])
        self.subplot.legend(loc='upper left')
        self.scatter = FigureCanvasTkAgg(self.figure, self.containing_frame)
        if(self.containing_frame.winfo_children()[-1]):
            self.containing_frame.winfo_children()[-1].place(x=0,y=0)
        if(self.containing_frame.winfo_children()[-2]):
            self.containing_frame.winfo_children()[-2].destroy()
        self.scatter.get_tk_widget().pack(expand=True, fill="both")
        #self.display_content()
        #pass