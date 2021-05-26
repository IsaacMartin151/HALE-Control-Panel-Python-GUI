import tkinter as tk
from tkinter import font as tkFont
import element
import enums

# This file defines a purely decorative "Rectangle"

# All values listed in __init__ below are default values that can be modified by passing in different arguments from wherever the Rectangle is created.
# This file is not intended to be modified

class Rectangle(element.Element):
    def __init__(self, *, color="green", **kwargs):
        self.color = color
        super().__init__(**kwargs)

    # Function to make the Rectangle visible on the panel
    def display_content(self):
        # relief means that it will have rounded edges. That value can be changed if it's not wanted. 
        self.c = tk.Canvas(self.containing_frame, width=self.abs_size_x, height=self.abs_size_y, bg=self.color, bd=0, highlightthickness=0, relief='ridge')
        self.c.pack(expand=True, fill="both")

    # The rectangle doesn't need to update
    def update(self):
        pass