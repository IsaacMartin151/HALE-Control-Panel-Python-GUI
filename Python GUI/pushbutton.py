import tkinter as tk
from tkinter import font as tkFont
import element
import time

# This file defines the PushButtons used on the main panel

# All values listed in __init__ below are default values that can be modified by passing in different arguments from wherever the PushButton is created.
# This file is not intended to be modified

# Each PushButton has an onclick function that should be specified to declare what should happen when the button is clicked

class PushButton(element.Element):
    # Constructor for the PushButton, can override these values to customize the PushButton and ignore default values
    def __init__(self, *, onclick = None, text = "Button", font="Arial Bold", text_color="black", bgcolor="white", font_size = 24,  **kwargs):
        self.text = text
        self.text_color = text_color
        self.bgcolor = bgcolor
        self.font_size = font_size
        self.onclick = onclick
        self.font = font
        super().__init__(**kwargs)

    # Make the PushButton visible on the panel
    def display_content(self):
        text_font = tkFont.Font(family = self.font, size=self.font_size)
        if(self.onclick):
            self.b = tk.Button(self.containing_frame, command = self.onclick, text =self.text, fg =self.text_color, bg=self.bgcolor, font=text_font)
        else:
            self.b = tk.Button(self.containing_frame, text =self.text, fg =self.text_color, bg=self.bgcolor, font=text_font)
        self.b.pack(expand=True, fill="both")

    # The pushbutton doesn't need to update
    def update(self): 
        pass
