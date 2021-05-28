import tkinter as tk
from tkinter import scrolledtext
from tkinter import font as tkFont
from time import gmtime, strftime
import element
import time

# This file defines the logging box used in the main panel

# All values listed in __init__ below are default values that can be modified by passing in different arguments from wherever the Chart is created.
# This file is not intended to be modified

# In order to add a message to the logging box, use the add_message method seen below

class LoggingBox(element.Element):
    # Constructor for the logging box. You can change the font size and type or colors of stuff by passing in different arguments when creating it.
    # These are just the default values
    def __init__(self, *, font=("Arial", 12), text_color="black", bgcolor="white", **kwargs):
        self.font = font
        self.text_color = text_color
        self.bgcolor = bgcolor
        super().__init__(**kwargs)

    # Makes the logging box visible on the panel
    def display_content(self):
        self.lb = scrolledtext.ScrolledText(self.containing_frame)
        self.lb.pack(expand=True, fill="both")
        
    # Used to add messages to the logging box. Right now there's limited room for the messages so don't overuse
    def add_message(self, text="Message"):
        self.lb.insert(tk.END, strftime("%H:%M:%S: ", gmtime()) + text + '\n')

    # The Logging box doesn't need to update
    def update(self): 
        pass