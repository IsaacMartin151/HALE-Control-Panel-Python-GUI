import tkinter as tk
from tkinter import font as tkFont
import element
import enums
import helpers

class Image(element.Element):
    def __init__(self, *, image="./hale.png", **kwargs):
        self.image = image
        super().__init__(**kwargs)

    def display_content(self):
        self.c = tk.Label(self.containing_frame, width=self.abs_size_x, height=self.abs_size_y, image=self.image, bd=0)
        self.c.pack(expand=True, fill="both")


    def update(self):
        pass