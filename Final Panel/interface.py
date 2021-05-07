import tkinter as tk
import panel
class Interface:
    
    def __init__(self):
        self.panels = []

    def display(self):
        if(len(self.panels) == 0):
            raise ValueError("No Panels Created")
        for panel in self.panels:
            panel.display()
        tk.Toplevel(self.panels[0].root)
        self.panels[0].root.mainloop()

    def add_panel(self, p):
        self.panels.append(p)
        return self.panels[-1]

