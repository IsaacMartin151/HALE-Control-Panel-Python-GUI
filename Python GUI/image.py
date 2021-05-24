import tkinter as tk
from tkinter import font as tkFont
import element
import enums
import PIL.Image, PIL.ImageTk


class Image(element.Element):
    def __init__(self, *, file="./hale.png", resize_x=None, resize_y=None, **kwargs):
        self.file = file
        self.resize_x = resize_x
        self.resize_y = resize_y
        super().__init__(**kwargs)

    def display_content(self):
        image = PIL.Image.open(self.file)

        # resize_x and resize_y are optional absolute pixel dimensions
        if (self.resize_x and self.resize_y):
            image = image.resize((self.resize_x, self.resize_y))

        self.image = PIL.ImageTk.PhotoImage(image)

        self.c = tk.Label(self.containing_frame, image=self.image, bd=0)
        self.c.pack(expand=True, fill="both")


    def update(self):
        pass