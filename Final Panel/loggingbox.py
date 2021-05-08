import tkinter as tk
from tkinter import font as tkFont
import element
import time

class LoggingBox(element.Element):
    def __init__(self, *, onclick = None, text = "Button", font="Arial Bold", text_color="black", bgcolor="white", font_size = 24,  **kwargs):
        self.text = text
        self.text_color = text_color
        self.bgcolor = bgcolor
        self.font_size = font_size
        self.onclick = onclick
        self.font = font
        super().__init__(**kwargs)

    def display_content(self):
        text_font = tkFont.Font(family = self.font, size=self.font_size)
        self.lb = tk.Listbox(self.containing_frame, width=self.abs_size_x)
        self.lb.pack(expand=True, fill="both")
        

    def add_message(self, text="No content", color="white"):
        self.lb.insert(0, text)
        self.lb.itemconfig(0, bg=color)
        #print("adding to logging box: "+text)

    def update(self): 
        pass