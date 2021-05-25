import tkinter as tk
from tkinter import font as tkFont
import element
import time

class LoggingBox(element.Element):
    def __init__(self, *, font=("Arial", 12), text_color="black", bgcolor="white", **kwargs):
        self.font = font
        self.text_color = text_color
        self.bgcolor = bgcolor
        super().__init__(**kwargs)

    def display_content(self):
        self.lb = tk.Listbox(self.containing_frame, width=self.abs_size_x, font=self.font, fg=self.text_color)
        self.lb.pack(expand=True, fill="both")
        
    def add_message(self, text="Message"):
        self.lb.insert(tk.END, text)

    def update(self): 
        pass