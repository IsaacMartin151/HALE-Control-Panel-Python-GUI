import tkinter as tk
from tkinter import font as tkFont
import element
import enums
import helpers

class Rectangle(element.Element):
    def __init__(self, *, color="green", **kwargs):
        self.color = color
        super().__init__(**kwargs)

    def display_content(self):


        self.c = tk.Canvas(self.containing_frame, width=self.abs_size_x, height=self.abs_size_y, bg=self.color, bd=0, highlightthickness=0, relief='ridge')
        self.c.pack(expand=True, fill="both")


    def update(self):
        pass