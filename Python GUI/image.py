import tkinter as tk
from tkinter import font as tkFont
import element
import enums
import PIL.Image, PIL.ImageTk

# This file defines an image. The image size should be set to whatever its corresponding pixels are, while its resize values should be the
# size it should appear on the panel. 

# This file isn't intended to be modified

class Image(element.Element):
    # Constructor for the image, specifies the resize values and the string leading to the image
    # Make sure the image is in the same directory as the panel_init.py, then add "./" in front of the filename
    # otherwise the image will just be the default value, which is the hale.png logo
    def __init__(self, *, file="./hale.png", resize_x=None, resize_y=None, **kwargs):
        self.file = file
        self.resize_x = resize_x
        self.resize_y = resize_y
        super().__init__(**kwargs)

    # function to make the Image visible
    def display_content(self):
        image = PIL.Image.open(self.file)

        # resize_x and resize_y are optional absolute pixel dimensions
        if (self.resize_x and self.resize_y):
            image = image.resize((self.resize_x, self.resize_y))

        self.image = PIL.ImageTk.PhotoImage(image)

        self.c = tk.Label(self.containing_frame, image=self.image, bd=0)
        self.c.pack(expand=True, fill="both")

    # The image does not need to update so we skip this
    def update(self):
        pass