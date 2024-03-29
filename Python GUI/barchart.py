import tkinter as tk
from tkinter import font as tkFont
import element
import enums

# This file defines the bar chart used on the indicator panel

# All values listed in __init__ below are default values that can be modified by passing in different arguments from wherever the BarChart is created.
# This file is not intended to be modified

class BarChart(element.Element):
    def __init__(self, *, starting_value=50, min_value = 0, max_value = 100, barcolor = "#11FF11", bgcolor = None, get_data = None, **kwargs):
        self.get_data = get_data
        self.value = starting_value
        self.min_value = min_value
        self.max_value = max_value
        self.barcolor = barcolor
        self.truncated_value = min(max(self.value, self.min_value), self.max_value)
        self.bgcolor = bgcolor
        super().__init__(**kwargs)

    # function that makes the chart visible
    def display_content(self):
        if (self.bgcolor == None):
            self.bgcolor = self.panel_bgcolor

        self.c = tk.Canvas(self.containing_frame, bg=self.bgcolor, width=self.abs_size_x, height=self.abs_size_y)
        self.bar = self.c.create_rectangle(0, self.abs_size_y - (self.abs_size_y)*((self.truncated_value-self.min_value)/(self.max_value-self.min_value)), self.abs_size_x, self.abs_size_y, fill=self.barcolor)
        self.c.pack(expand=True, fill="both")

    #function that updates the chart's info periodically
    def update(self):
            if (self.get_data):
                self.value = self.get_data()
                self.truncated_value = min(max(self.value, self.min_value), self.max_value)
                self.c.coords(self.bar, 0, self.abs_size_y - (self.abs_size_y)*((self.truncated_value-self.min_value)/(self.max_value-self.min_value)), self.abs_size_x, self.abs_size_y)