import tkinter as tk
import element
import pushbutton
import togglebutton
import indicatorlight
import rectangle
import random
import enums

# This file defines what a Panel is

# This file is not intended to be modified

# Each panel has an array of elements that can be added to. It will iterate through the elements to update them
# Wherever you see "tk", that's a tkinter function used to create either a new application or a new display source.
# You can find documentation about tkinter at https://docs.python.org/3/library/tkinter.html, but the more readable 
# and more practical examples of tkinter can be found at https://www.geeksforgeeks.org/python-gui-tkinter/. 

class Panel:
    # Add a new element to the current list of elements
    def add_element(self, e):
        self.elements.append(e)
        self.display()
        return self.elements[-1]

    # Creates a new source for the panel display, see the tkinter documentation links above
    def init_window(self):
        if(self.root):
            for widget in self.root.winfo_children():
                widget.destroy()
        else:
            self.root = tk.Toplevel()
            self.root.geometry(str(self.size_x) + "x" + str(self.size_y) + "+" + str(self.pos_x) + "+" + str(self.pos_y))
            self.root.configure(bg = self.bgcolor)

    # Shows the elements of the panel and uses this panel's information to adjust sizes
    def display(self):
        self.init_window()
        self.elements.sort(key= lambda x : x.z)
        for element in self.elements:
            element.set_panel_info(self.root, self.bgcolor, self.size_x, self.size_y)
            element.display()
       
        # Open window having dimension 100x100

    # Constructor for the panel, can override these default values when creating a new panel
    def __init__(self, *, size_x=1600, size_y=900, pos_x=0, pos_y=0, bgcolor = "#000000"):
        self.size_x = size_x
        self.size_y = size_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.elements = []
        self.root = None
        self.bgcolor = bgcolor
        self.init_window()
        self.display()
        

        
