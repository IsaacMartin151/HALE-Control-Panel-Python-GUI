import tkinter as tk
from tkinter import font as tkFont
import element
import enums
import helpers

class IndicatorLight(element.Element):
    def __init__(self, *, text="Indicator Label", starting_color="green", text_color = "white", get_data = None, **kwargs):
        self.get_data = get_data
        self.color = starting_color
        self.text_color = text_color
        self.text = text
        super().__init__(**kwargs)

    def display_content(self):
        title = tk.Label(self.containing_frame, text=self.text, fg=self.text_color, bg=self.panel_bgcolor, font=("Arial", 12))

        canvas_padding = 24

        self.c = tk.Canvas(self.containing_frame, width=self.abs_size_x, height=self.abs_size_y-canvas_padding, bg=self.panel_bgcolor, bd=0, highlightthickness=0, relief='ridge')
        title.pack(side = tk.TOP)
        self.c.pack(side=tk.BOTTOM)
        min_dimension = min(self.abs_size_x, self.abs_size_y-canvas_padding)
        self.circle = self.c.create_oval((self.abs_size_x -min_dimension)/2, (self.abs_size_y -canvas_padding -min_dimension)/2, (self.abs_size_x -min_dimension)/2 + min_dimension, (self.abs_size_y - canvas_padding -min_dimension)/2 + min_dimension, fill=self.color)


    def update(self):
        if (self.get_data):
            self.color = self.get_data()
            self.c.itemconfig(self.circle, fill=self.color)