import tkinter as tk
import time
import enums

# This file defines the parent class for anything that goes 'into' the panel. Examples are charts, lights, buttons, etc. 

# Whenever sizes are specified in Element's child classes, they will be clipped based on the element's panel's size as seen in clip_abs_x and clip_abs_y

# All values listed in __init__ below are default values that can be modified by passing in different arguments from wherever the Element or child class is created.
# This file is not intended to be modified


class Element:
        # Clips the size according to a standardized panel size of 1000
        def clip_abs_x (self, x):
            return int(((x/1000)*self.panel_size_x))

        def clip_abs_y (self, y):
            return int(((y/1000)*self.panel_size_y))

        # Figures out where the element should go based on the inputs
        def calculate_positions(self, size_x, size_y, pos_x, pos_y, anchor):
            if (anchor == enums.AnchorPoints.TOPLEFT):
                x = pos_x
                y = pos_y
            elif(anchor == enums.AnchorPoints.TOPRIGHT):
                x = pos_x - size_x
                y = pos_y
            elif(anchor == enums.AnchorPoints.BOTTOMLEFT):
                x = pos_x
                y = pos_y - size_y
            elif(anchor == enums.AnchorPoints.BOTTOMRIGHT):
                x = pos_x - size_x
                y = pos_y - size_y
            elif(anchor == enums.AnchorPoints.CENTER):
                x = pos_x - (size_x/2)
                y = pos_y - (size_y/2)
            else:
                raise(ValueError("Invalid Anchor Point Specified"))
            self.abs_pos_x = self.clip_abs_x(x)
            self.abs_pos_y = self.clip_abs_y(y)
            self.abs_size_x = self.clip_abs_x(size_x)
            self.abs_size_y = self.clip_abs_y(size_y)

        # These functions are left for the child classes to implement

        #Called periodically every refresh_interval. Child classes should implement data acquisition and display here
        def update(self):
            pass
        
        #This is called at initialization when the panel is to be drawn for the first time
        def display_content(self):
            pass
        
        #Handles the periodic calling of update()
        def update_loop(self):
            self.update()
            if (self.refresh_interval):
                self.containing_frame.after(self.refresh_interval, self.update_loop)

        # Shows the element after positioning and clipping
        def display(self):
            self.calculate_positions(self.size_x, self.size_y, self.pos_x, self.pos_y, self.anchor)

            self.containing_frame = tk.Frame(self.panel_root, bg=self.panel_bgcolor, width=self.abs_size_x, height=self.abs_size_y)
            self.containing_frame.place(x=self.abs_pos_x, y=self.abs_pos_y)
            self.containing_frame.pack_propagate(0)

            self.display_content()

            self.update_loop()

        # Tells the element information about the panel it's on
        def set_panel_info(self, panel_root, panel_bgcolor, panel_size_x, panel_size_y):
            self.panel_size_x = panel_size_x
            self.panel_size_y = panel_size_y
            self.panel_root = panel_root
            self.panel_bgcolor = panel_bgcolor

        # Constructor for an element, has a set size and position and various default values that can be passed in
        def __init__ (self, *, z = enums.Depths.MIDDLEGROUND, size_x=100, size_y=100, pos_x = 0, pos_y=0, anchor=enums.AnchorPoints.TOPLEFT, refresh_interval=None):
            self.anchor = anchor
            self.size_x = size_x
            self.size_y = size_y
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.z = z
            self.refresh_interval = refresh_interval


