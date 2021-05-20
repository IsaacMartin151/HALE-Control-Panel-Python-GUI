import tkinter as tk
import element
import pushbutton
import togglebutton
import indicatorlight
import rectangle
import random
import enums

class Panel:
    def add_element(self, e):
        self.elements.append(e)
        self.display()
        return self.elements[-1]

    def init_window(self):
        if(self.root):
            for widget in self.root.winfo_children():
                widget.destroy()
        else:
            self.root = tk.Tk()
            self.root.geometry(str(self.size_x) + "x" + str(self.size_y) + "+" + str(self.pos_x) + "+" + str(self.pos_y))
            self.root.configure(bg = self.bgcolor)

    def display(self):
        self.init_window()
        self.elements.sort(key= lambda x : x.z)
        for element in self.elements:
            element.set_panel_info(self.root, self.bgcolor, self.size_x, self.size_y)
            element.display()
       

 
        # Open window having dimension 100x100

    def __init__(self, *, size_x=1600, size_y=900, pos_x=0, pos_y=0, bgcolor = "#111111"):
        self.size_x = size_x
        self.size_y = size_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.elements = []
        self.root = None
        self.bgcolor = bgcolor
        self.init_window()
        self.display()
        

        
