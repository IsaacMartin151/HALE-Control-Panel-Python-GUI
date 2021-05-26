import tkinter as tk
import panel

# This is the file that really holds the entire "Application". 
# It has an array of panels that each have elements, and by calling display it starts the entire thing

class Interface:
    
    # Constructor just initializes an array of panels
    def __init__(self):
        self.panels = []

    # This tells the GUI to show all 3 panels and then start running
    def display(self):
        if(len(self.panels) == 0):
            raise ValueError("No Panels Created")
        for panel in self.panels:
            panel.display()
        tk.Toplevel(self.panels[0].root)
        self.panels[0].root.mainloop()

    # Function for adding an additional panel to the array
    def add_panel(self, p):
        self.panels.append(p)
        return self.panels[-1]

