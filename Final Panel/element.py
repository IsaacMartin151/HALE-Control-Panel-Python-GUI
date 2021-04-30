import tkinter as tk
import time
import enums



class Element:
        
        
        
        def clip_abs_x (self, x):
            return int(((x/1000)*self.panel_size_x))

        def clip_abs_y (self, y):
            return int(((y/1000)*self.panel_size_y))

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

        def update(self):
            pass
        
        def display_content(self):
            pass
        
        def update_loop(self):
            self.update()
            if (self.refresh_interval):
                self.containing_frame.after(self.refresh_interval, self.update_loop);

        def display(self):


            self.calculate_positions(self.size_x, self.size_y, self.pos_x, self.pos_y, self.anchor)



            self.containing_frame = tk.Frame(self.panel_root, bg=self.panel_bgcolor, width=self.abs_size_x, height=self.abs_size_y)
            self.containing_frame.place(x=self.abs_pos_x, y=self.abs_pos_y)
            self.containing_frame.pack_propagate(0)

            self.display_content()

            self.update_loop()

        def set_panel_info(self, panel_root, panel_bgcolor, panel_size_x, panel_size_y):
            self.panel_size_x = panel_size_x
            self.panel_size_y = panel_size_y
            self.panel_root = panel_root
            self.panel_bgcolor = panel_bgcolor

        def __init__ (self, *, z = enums.Depths.MIDDLEGROUND, size_x=100, size_y=100, pos_x = 0, pos_y=0, anchor=enums.AnchorPoints.TOPLEFT, refresh_interval=None):
            self.anchor = anchor
            self.size_x = size_x
            self.size_y = size_y
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.z = z
            self.refresh_interval = refresh_interval


