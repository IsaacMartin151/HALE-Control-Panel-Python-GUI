import tkinter as tk
from tkinter import font as tkFont
import element
import enums
import helpers

class Image(element.Element):
    def __init__(self, *, file="./hale.png", **kwargs):
        self.file = file
        super().__init__(**kwargs)

    def display_content(self):
        self.image = tk.PhotoImage(file=self.file, width=self.abs_size_x, height=self.abs_size_y)
        self.c = tk.Label(self.containing_frame, image=self.image, bd=0)
        self.c.pack(expand=True, fill="both")


    def update(self):
        pass