import tkinter as tk
from tkinter import font as tkFont
import element
import enums
import helpers

class IndicatorLight(element.Element):
    def __init__(self, *, text="Indicator Label", starting_color="green", text_color = "white", font=("Arial", 12), bgcolor = None, get_data = None, **kwargs):
        self.get_data = get_data
        self.color = starting_color
        self.text_color = text_color
        self.text = text
        self.bgcolor = bgcolor
        self.font = font
        super().__init__(**kwargs)

    def display_content(self):
        if (self.bgcolor == None):
            self.bgcolor = self.panel_bgcolor

        canvas_padding = 24

        self.c = tk.Canvas(self.containing_frame, width=self.abs_size_x, height=self.abs_size_y-canvas_padding, bg=self.bgcolor, bd=0, highlightthickness=0, relief='ridge')

        if (self.text):
            self.c.pack(side=tk.BOTTOM)

            title = tk.Label(self.containing_frame, text=self.text, fg=self.text_color, bg=self.bgcolor, font=self.font)
            title.pack(side = tk.TOP)

            min_dimension = min(self.abs_size_x, self.abs_size_y-canvas_padding)
            self.circle = self.c.create_oval((self.abs_size_x -min_dimension)/2, (self.abs_size_y -canvas_padding -min_dimension)/2, (self.abs_size_x -min_dimension)/2 + min_dimension, (self.abs_size_y - canvas_padding -min_dimension)/2 + min_dimension, fill=self.color)

        else:
            self.circle = self.c.create_oval(0, 0, self.abs_size_x, self.abs_size_y, fill=self.color)
            self.c.pack(expand=True, fill="both")
            
        

    def update(self):
        if (self.get_data):
            self.color = self.get_data()
            self.c.itemconfig(self.circle, fill=self.color)