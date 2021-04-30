import tkinter as tk
from tkinter import font as tkFont
import element
import time
class PushButton(element.Element):
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
        if(self.onclick):
            self.b = tk.Button(self.containing_frame, command = self.onclick, text =self.text, fg =self.text_color, bg=self.bgcolor, font=text_font)
        else:
            self.b = tk.Button(self.containing_frame, text =self.text, fg =self.text_color, bg=self.bgcolor, font=text_font)
        self.b.pack(expand=True, fill="both")

    def update(self): 
        pass
