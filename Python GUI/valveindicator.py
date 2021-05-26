import tkinter as tk
from tkinter import font as tkFont
import element
import enums

# This file defines the ValveIndicators used on the main panel

# All values listed in __init__ below are default values that can be modified by passing in different arguments from wherever the ValveIndicator is created.
# This file is not intended to be modified

# These are the OPEN/CLOSED things in the center of the main panel. They are essentially text-based indicator lights

class ValveIndicator(element.Element):
    def __init__(self, *, state=enums.ToggleStates.OFF, get_data=None, **kwargs):
        self.state = state
        self.get_data = get_data
        self.on_text = "OPEN"
        self.off_text = "CLOSED"
        self.font = "Arial Bold"
        self.font_size = 12
        self.text_color = "white"
        self.on_bgcolor = "#339933"
        self.off_bgcolor="#ff0000"

        super().__init__(**kwargs)

    # Make the ValveIndicator visible on the panel
    def display_content(self):
        text_font = tkFont.Font(family = self.font, size=self.font_size)

        if (self.state == enums.ToggleStates.OFF):
            self.c = tk.Canvas(self.containing_frame, width=self.abs_size_x, height=self.abs_size_y, bg=self.off_bgcolor, bd=0, highlightthickness=0, relief='ridge')
            self.indicator_text = self.c.create_text(self.abs_size_x/2, self.abs_size_y/2, text=self.off_text, font=text_font, fill=self.text_color)
        elif (self.state == enums.ToggleStates.ON):
            self.c = tk.Canvas(self.containing_frame, width=self.abs_size_x, height=self.abs_size_y, bg=self.on_bgcolor,bd=0, highlightthickness=0, relief='ridge')
            self.indicator_text = self.c.create_text(self.abs_size_x/2, self.abs_size_y/2, text=self.on_text, font=text_font, fill=self.text_color)

        else:
            throw (ValueError("Invalid ValveIndicator State"))

        self.c.pack(expand=True, fill="both")

    # Based on whether or not the valve is on or off, update the text and color
    def update(self):
        if (self.get_data):
            self.state = self.get_data()

            if (self.state == enums.ToggleStates.OFF):
                #self.c.itemconfig(self.c, bg=self.off_bgcolor)
                self.c.itemconfig(self.indicator_text, text=self.off_text)
                self.c.configure(bg=self.off_bgcolor)

            elif (self.state == enums.ToggleStates.ON):
                #self.c.itemconfig(self.c, bg=self.on_bgcolor)
                self.c.itemconfig(self.indicator_text, text=self.on_text)
                self.c.configure(bg=self.on_bgcolor)

        else:
            throw (ValueError("Invalid ValveIndicator State"))