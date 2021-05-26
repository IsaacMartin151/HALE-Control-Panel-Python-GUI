import tkinter as tk
from tkinter import font as tkFont
import element
import time
import enums

# This file defines the ToggleButtons used on the main panel

# All values listed in __init__ below are default values that can be modified by passing in different arguments from wherever the ToggleButton is created.
# This file is not intended to be modified

# ToggleButtons are pretty much more complicated PushButtons, because they have two functions you can specify, one for off and one for on. They also
# have an off color and an on color

class ToggleButton(element.Element):
    # Constructor for the toggle button, default values can be overridden from wherever they're created by passing in different arguments
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

    # Defines what happens when the button is clicked, which results in either the toggle_on function happening or the toggle_off happening
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

    # Simple function to get whether it's on or off
    def get_state(self):
        return self.state

    # Makes the ToggleButton visible on the panel
    def display_content(self):
        text_font = tkFont.Font(family = self.font, size=self.font_size)
        if (self.state == enums.ToggleStates.OFF):
            self.b = tk.Button(self.containing_frame, command = self.toggle, text =self.off_text, fg =self.off_text_color, bg=self.off_bgcolor, font=text_font)
        elif(self.state == enums.ToggleStates.ON):
            self.b = tk.Button(self.containing_frame, command = self.toggle, text =self.on_text, fg =self.on_text_color, bg=self.on_bgcolor, font=text_font)
        else:
            throw (ValueError("Invalid Button State"))
        self.b.pack(expand=True, fill="both")

    # ToggleButton doesn't need to passively update
    def update(self): 
            pass
