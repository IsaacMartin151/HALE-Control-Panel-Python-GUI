import tkinter as tk
from tkinter import font as tkFont
import element
import enums

# This file defines the number displays used on the indicator panel

# All values listed in __init__ below are default values that can be modified by passing in different arguments from wherever the NumericDisplay is created.
# This file is not intended to be modified

# This is just a small text box that shows a number

class NumericDisplay(element.Element):
    # Constructor for the numeric display, the default values can be overridden wherever it's created by passing in different arguments
    def __init__(self, *, text="Indicator Label", starting_value=0, text_color = "white", font=("Arial", 12), bgcolor = None, get_data = None, **kwargs):
        self.get_data = get_data
        self.value = starting_value
        self.text_color = text_color
        self.text = text
        self.bgcolor = bgcolor
        self.font = font
        super().__init__(**kwargs)

    # Makes the numeric display visible on the panel
    def display_content(self):
        if (self.bgcolor == None):
            self.bgcolor = self.panel_bgcolor

        if (self.text):

            title = tk.Label(self.containing_frame, text=self.text, fg=self.text_color, bg=self.bgcolor, font=self.font)
            title.pack(side = tk.TOP)

        self.t = tk.Text(self.containing_frame, height=self.abs_size_x, width=self.abs_size_y)
        self.t.insert(tk.END, float(self.value))
        self.t.pack(expand=True, fill="both")

        

    # If the numeric display was passed a get_data function, it should show whatever that the function's value is
    def update(self):
            if (self.get_data):
                self.value = self.get_data()
                self.t.delete("1.0", "end")
                self.t.insert(tk.END, float(self.value))