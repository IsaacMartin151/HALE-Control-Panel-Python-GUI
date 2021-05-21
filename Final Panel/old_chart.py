import tkinter as tk
import element
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Chart(element.Element):
    def __init__(self, *, title = "Chart title", font="Arial Bold", xlabel="Time", max_points = 5, ylabel="Pressure", text_color="black", get_data = None, font_size = 24,  **kwargs):
        #self.figure1 = None
        self.lines = []
        self.get_data = get_data
        self.title = title
        self.text_color = text_color
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.font_size = font_size
        self.max_points = max_points
        self.font = font
        super().__init__(**kwargs)

    def add_info(self, x, y, colorI, labelI):
        self.lines.append([x, y, colorI, labelI])
        self.subplot.plot(x, y, color=colorI, label=labelI)
        self.subplot.legend()
        

    def display_content(self):
        self.figure = Figure(figsize=(4,3), dpi=80, facecolor="#777777")
        self.subplot = self.figure.add_subplot(1, 1, 1, facecolor='#CACACA')
        self.subplot.set_xlabel("Time", color=self.text_color)
        self.subplot.set_ylabel("Pressure", color=self.text_color)
        self.scatter = FigureCanvasTkAgg(self.figure, self.containing_frame)
        #print("placing plot")
        self.scatter.get_tk_widget().pack(expand=True, fill="both")
    

    def update(self):
            
        self.subplot.clear()
        self.subplot.set_title(self.title)
        self.subplot.set_xlabel("Time", color=self.text_color)
        self.subplot.set_ylabel("Pressure", color=self.text_color)
        for line in range(len(self.lines)):
            info = self.lines[line]
            self.add_info(info[0], info[1], info[2], info[3])
        #self.display_content()
        #pass