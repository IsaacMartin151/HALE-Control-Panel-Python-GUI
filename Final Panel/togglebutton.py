import tkinter as tk
from tkinter import font as tkFont
import element
import time
import enums

class ToggleButton(element.Element):

    def __init__(self, *, on_toggleon=None, on_toggleoff=None, off_text="OFF", on_text="ON", font="Arial Bold", font_size=24, off_text_color="white", off_bgcolor="#ff0000", on_text_color="white", on_bgcolor="#339933", starting_state=enums.ToggleStates.OFF,  **kwargs):
        self.state = starting_state

        self.on_text = on_text
        self.on_text_color = on_text_color
        self.on_bgcolor = on_bgcolor

        self.off_text = off_text
        self.off_text_color = off_text_color
        self.off_bgcolor = off_bgcolor

        self.font_size = font_size
        self.on_toggleon = on_toggleon
        self.on_toggleoff = on_toggleoff
        self.font = font
        super().__init__(**kwargs)

    def toggle(self):
        if (self.state == enums.ToggleStates.OFF):
            self.state = enums.ToggleStates.ON
            self.b.configure(fg =self.on_text_color, bg=self.on_bgcolor, text=self.on_text)
            if(self.on_toggleon):
                self.on_toggleon()
        else:
            self.state = enums.ToggleStates.OFF
            self.b.configure(fg =self.off_text_color, bg=self.off_bgcolor, text=self.off_text)
            if(self.on_toggleoff):
                self.on_toggleoff()

    def get_state(self):
        return self.state

    def display_content(self):
        text_font = tkFont.Font(family = self.font, size=self.font_size)
        if (self.state == enums.ToggleStates.OFF):
            self.b = tk.Button(self.containing_frame, command = self.toggle, text =self.off_text, fg =self.off_text_color, bg=self.off_bgcolor, font=text_font)
        elif(self.state == enums.ToggleStates.ON):
            self.b = tk.Button(self.containing_frame, command = self.toggle, text =self.on_text, fg =self.on_text_color, bg=self.on_bgcolor, font=text_font)
        else:
            throw (ValueError("Invalid Button State"))
        self.b.pack(expand=True, fill="both")

    def update(self): 
            pass
