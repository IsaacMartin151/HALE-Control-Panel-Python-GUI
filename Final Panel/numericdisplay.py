import tkinter as tk
from tkinter import font as tkFont
import element
import enums

class NumericDisplay(element.Element):
    def __init__(self, *, text="Indicator Label", starting_value=0, text_color = "white", font=("Arial", 12), bgcolor = None, get_data = None, **kwargs):
        self.get_data = get_data
        self.value = starting_value
        self.text_color = text_color
        self.text = text
        self.bgcolor = bgcolor
        self.font = font
        super().__init__(**kwargs)

    def display_content(self):
        if (self.bgcolor == None):
            self.bgcolor = self.panel_bgcolor

        if (self.text):

            title = tk.Label(self.containing_frame, text=self.text, fg=self.text_color, bg=self.bgcolor, font=self.font)
            title.pack(side = tk.TOP)

        self.t = tk.Text(self.containing_frame, height=self.abs_size_x, width=self.abs_size_y)
        self.t.insert(tk.END, float(self.value))
        self.t.pack(expand=True, fill="both")

        

    def update(self):
            if (self.get_data):
                self.value = self.get_data()
                self.t.delete("1.0", "end")
                self.t.insert(tk.END, float(self.value))