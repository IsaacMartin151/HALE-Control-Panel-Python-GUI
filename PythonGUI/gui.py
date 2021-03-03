import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
#import matplotlib.animation as anim
#from IPython.display import clear_output

#Code for the 3 box entries to manually input data

#entry1 = tk.Entry (root)
#canvas1.create_window(width/2, 100, window=entry1)
#entry2 = tk.Entry (root)
#canvas1.create_window(width/2, 120, window=entry2)
#entry3 = tk.Entry (root)
#canvas1.create_window(width/2, 140, window=entry3)

#x1 = float(entry1.get())
#x2 = float(entry2.get())
#x3 = float(entry3.get())

root = tk.Tk()

i = 1
k = 0
plotDPI = 80

# Button states
global fuelbuttonon
global oxidizerbuttonon
global commandbuttonon

global fuelpresson
global fuelventon
global fuelisolationon
global fuelpurgeon
global fuelmainon

global loxpresson
global loxventon
global loxisolationon
global loxchillon
global loxmainon

fuelbuttonon = False
oxidizerbuttonon = False
commandbuttonon = False

fuelpresson = False
fuelventon = False
fuelisolationon = False
fuelpurgeon = False
fuelmainon = False

loxpresson = False
loxventon = False
loxisolationon = False
loxchillon = False
loxmainon = False

def create_charts():
    #These are data values at the top of this function
    global i
    global k
    figure7 = Figure(figsize=(4,3), dpi=plotDPI)
    subplot7 = figure7.add_subplot(111)
    x = np.linspace(0, 100, 200)
    i += 1
    k += .1
    k = k % 200
    #print("i is ", i)
    y = np.sin(2 * np.pi * x + k)
    subplot7.plot(x, y, color = 'lightsteelblue')
    #subplot4.title("Connected Scatterplot points with line")
    subplot7.set_xlabel("x")
    subplot7.set_ylabel("sinx")
    scatter1 = FigureCanvasTkAgg(figure7, root)
    scatter1.get_tk_widget().place(x=700, y=550)

def clear_charts():
    bar1.get_tk_widget().pack_forget()
    bar2.get_tk_widget().pack_forget()
    bar3.get_tk_widget().pack_forget()
    bar4.get_tk_widget().pack_forget()
    pie2.get_tk_widget().pack_forget()
    pie3.get_tk_widget().pack_forget()
    scatter1.get_tk_widget().pack_forget()

def set_gray(button):
    button.configure(bg = 'gray')

class MainScreen:
    #Setting variables for the GUI's main display
    width = 1600
    height = 500

    standardizedButtonHeight = 2
    standardizedButtonWidth = 25
    startingHeight = 350
    heightSpacing = 40

    #Dummy data
    x1 = 10
    x2 = 13
    x3 = 23

    canvas1 = tk.Canvas(root, width = width, height = height)
    background_image = tk.PhotoImage(file = "C:\\Users\\Isaac\\Desktop\\background.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    canvas1.pack()

    label1 = tk.Label(root, text='Control Panel')
    label1.config(font=('Arial', 20))
    canvas1.create_window(width/2, 50, window=label1)

    def command_nogo():
        global commandbuttonon
        commandbuttonon = not commandbuttonon

    def fuel_nogo():
        global fuelbuttonon
        fuelbuttonon = not fuelbuttonon

    def oxidizer_nogo():
        global oxidizerbuttonon
        oxidizerbuttonon = not oxidizerbuttonon


    def fuel_vent():
        global fuelventon
        fuelventon = not fuelventon

    def fuel_press():
        global fuelpresson
        fuelpresson = not fuelpresson

    def fuel_isolation():
        global fuelisolationon
        fuelisolationon = not fuelisolationon

    def fuel_purge():
        global fuelpurgeon
        fuelpurgeon = not fuelpurgeon

    def fuel_main():
        global fuelmainon
        fuelmainon = not fuelmainon

    def lox_vent():
        global loxventon
        loxventon = not loxventon

    def lox_press():
        global loxpresson
        loxpresson = not loxpresson

    def lox_isolation():
        global loxisolationon
        loxisolationon = not loxisolationon

    def lox_chill():
        global loxchillon
        loxchillon = not loxchillon

    def lox_main():
        global loxmainon
        loxmainon = not loxmainon

    # Creating the data for the top three buttons
    fuelbutton = tk.Button (root, text=' FUEL NOGO ',command=fuel_nogo, bg='red', font=('Arial', 11, 'bold'), width=30, height = 5)
    oxidizerbutton = tk.Button (root, text=' OXIDIZER NOGO ',command=oxidizer_nogo, bg='red', font=('Arial', 11, 'bold'), width=30, height = 5)
    commandbutton = tk.Button (root, text=' COMMAND NOGO ',command=command_nogo, bg='red', font=('Arial', 11, 'bold'), width=30, height = 5)

    # Creating the data for the left column of center buttons
    fuelpress = tk.Button (root, text=' ABV-PR-120 (FUEL PRESS) ',command=fuel_press, bg='green', font=('Arial', 10, 'bold'))
    fuelvent = tk.Button (root, text=' ABV-FU-310 (FUEL VENT) ',command=fuel_vent, bg='orange', font=('Arial', 10, 'bold'))
    fuelisolation = tk.Button (root, text=' ABV-FU-320 (FUEL ISOLATION) ',command=fuel_isolation, bg='orange', font=('Arial', 10, 'bold'))
    fuelpurge = tk.Button (root, text=' ABV-FU-330 (FUEL PURGE) ',command=fuel_purge, bg='orange', font=('Arial', 10, 'bold'))
    fuelmain = tk.Button (root, text=' ABV-FU-340 (FUEL MAIN) ',command=fuel_main, bg='orange', font=('Arial', 10, 'bold'))

    # Creating the data for the right column of center buttons
    loxpress = tk.Button (root, text=' ABV-PR-110 (LOx PRESS) ',command=lox_press, bg='green', font=('Arial', 10, 'bold'))
    loxvent = tk.Button (root, text=' ABV-FU-310 (LOx VENT) ',command=lox_vent, bg='blue', font=('Arial', 10, 'bold'))
    loxisolation = tk.Button (root, text=' ABV-FU-320 (LOx ISOLATION) ',command=lox_isolation, bg='blue', font=('Arial', 10, 'bold'))
    loxchill = tk.Button (root, text=' ABV-FU-330 (LOx CHILL) ',command=lox_chill, bg='blue', font=('Arial', 10, 'bold'))
    loxmain = tk.Button (root, text=' ABV-FU-340 (LOx MAIN) ',command=lox_main, bg='blue', font=('Arial', 10, 'bold'))


    def initialize_configurations(self):
        self.fuelpress.config(height = self.standardizedButtonHeight, width = self.standardizedButtonWidth)
        self.fuelvent.config(height = self.standardizedButtonHeight, width = self.standardizedButtonWidth)
        self.fuelisolation.config(height = self.standardizedButtonHeight, width = self.standardizedButtonWidth)
        self.fuelpurge.config(height = self.standardizedButtonHeight, width = self.standardizedButtonWidth)
        self.fuelmain.config(height = self.standardizedButtonHeight, width = self.standardizedButtonWidth)

        self.loxpress.config(height = self.standardizedButtonHeight, width = self.standardizedButtonWidth)
        self.loxvent.config(height = self.standardizedButtonHeight, width = self.standardizedButtonWidth)
        self.loxisolation.config(height = self.standardizedButtonHeight, width = self.standardizedButtonWidth)
        self.loxchill.config(height = self.standardizedButtonHeight, width = self.standardizedButtonWidth)
        self.loxmain.config(height = self.standardizedButtonHeight, width = self.standardizedButtonWidth)

    def draw_buttons(self):
        #Buttons for cancelling oxidizer, fuel, and command
        self.canvas1.create_window(self.width/2+self.width/4, 180, window=self.fuelbutton)
        self.canvas1.create_window(self.width/2-self.width/4, 180, window=self.oxidizerbutton)
        self.canvas1.create_window(self.width/2, 180, window=self.commandbutton)

        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*0, window=self.loxpress)
        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*1, window=self.loxvent)
        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*2, window=self.loxisolation)
        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*3, window=self.loxchill)
        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*4, window=self.loxmain)

        self.canvas1.create_window(self.width/2 - 120, self.startingHeight + self.heightSpacing*0, window=self.fuelpress)
        self.canvas1.create_window(self.width/2 - 120, self.startingHeight + self.heightSpacing*1, window=self.fuelvent)
        self.canvas1.create_window(self.width/2 - 120, self.startingHeight + self.heightSpacing*2, window=self.fuelisolation)
        self.canvas1.create_window(self.width/2 - 120, self.startingHeight + self.heightSpacing*3, window=self.fuelpurge)
        self.canvas1.create_window(self.width/2 - 120, self.startingHeight + self.heightSpacing*4, window=self.fuelmain)

    def configure_buttons(self):
        if fuelbuttonon:
            self.fuelbutton.configure(bg = 'red')
        else:
            self.fuelbutton.configure(bg = 'gray')
        if oxidizerbuttonon:
            self.oxidizerbutton.configure(bg = 'red')
        else:
            self.oxidizerbutton.configure(bg = 'gray')
        if commandbuttonon:
            self.commandbutton.configure(bg = 'red')
        else:
            self.commandbutton.configure(bg = 'gray')
        if fuelpresson:
            self.fuelpress.configure(bg = 'orange')
        else:
            self.fuelpress.configure(bg = 'gray')
        if (fuelventon):
            self.fuelvent.configure(bg = 'orange')
        else:
            self.fuelvent.configure(bg = 'gray')
        if (fuelisolationon):
            self.fuelisolation.configure(bg = 'orange')
        else:
            self.fuelisolation.configure(bg = 'gray')
        if (fuelpurgeon):
            self.fuelpurge.configure(bg = 'orange')
        else:
            self.fuelpurge.configure(bg = 'gray')
        if (fuelmainon):
            self.fuelmain.configure(bg = 'orange')
        else:
            self.fuelmain.configure(bg = 'gray')

        if (loxpresson):
            self.loxpress.configure(bg = 'blue')
        else:
            self.loxpress.configure(bg = 'gray')
        if (loxventon):
            self.loxvent.configure(bg = 'blue')
        else:
            self.loxvent.configure(bg = 'gray')
        if (loxisolationon):
            self.loxisolation.configure(bg = 'blue')
        else:
            self.loxisolation.configure(bg = 'gray')
        if (loxchillon):
            self.loxchill.configure(bg = 'blue')
        else:
            self.loxchill.configure(bg = 'gray')
        if (loxmainon):
            self.loxmain.configure(bg = 'blue')
        else:
            self.loxmain.configure(bg = 'gray')


    def create_charts2(self):
        #Left side charts
        x1 = self.x1
        x2 = self.x2
        x3 = self.x3
        figure1 = Figure(figsize=(4,3), dpi=plotDPI)
        subplot1 = figure1.add_subplot(111)
        xAxis = [float(x1),float(x2),float(x3)]
        yAxis = [float(x1),float(x2),float(x3)]
        subplot1.bar(xAxis,yAxis, color = 'lightsteelblue')
        bar1 = FigureCanvasTkAgg(figure1, root)
        print("placing plot 1")
        bar1.get_tk_widget().place(x=0, y=50)

        figure2 = Figure(figsize=(4,3), dpi=plotDPI)
        subplot2 = figure2.add_subplot(111)
        labels2 = 'Fuel Level', 'Oxidizer\nLevel', 'Regulator\npressure'
        pieSizes = [float(x1),float(x2),float(x3)]
        my_colors2 = ['lightblue','lightsteelblue','silver']
        explode2 = (0, 0, 0)
        subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=False, startangle=90)
        subplot2.axis('equal')
        pie2 = FigureCanvasTkAgg(figure2, root)
        print("placing plot 2")
        pie2.get_tk_widget().place(x=0, y=300)

        figure3 = Figure(figsize=(4,3), dpi=plotDPI)
        subplot3 = figure3.add_subplot(111)
        xAxis2 = [float(x1),float(x2),float(x3)]
        yAxis2 = [float(x1),float(x2),float(x3)]
        subplot3.bar(xAxis2,yAxis2, color = 'lightsteelblue')
        bar2 = FigureCanvasTkAgg(figure3, root)
        print("placing plot 3")
        bar2.get_tk_widget().place(x=0, y=550)


        #Right side charts
        figure4 = Figure(figsize=(4,3), dpi=plotDPI)
        subplot4 = figure4.add_subplot(111)
        xAxis = [float(x1),float(x2),float(x3)]
        yAxis = [float(x1),float(x2),float(x3)]
        subplot4.bar(xAxis,yAxis, color = 'lightsteelblue')
        bar3 = FigureCanvasTkAgg(figure4, root)
        print("placing plot 4")
        bar3.get_tk_widget().place(x=1200, y=50)

        figure5 = Figure(figsize=(4,3), dpi=plotDPI)
        subplot5 = figure5.add_subplot(111)
        labels2 = 'Fuel Level', 'Oxidizer\nLevel', 'Regulator\npressure'
        pieSizes = [float(x1),float(x2),float(x3)]
        my_colors2 = ['lightblue','lightsteelblue','silver']
        explode2 = (0, 0, 0)
        subplot5.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=False, startangle=90)
        subplot5.axis('equal')
        pie3 = FigureCanvasTkAgg(figure5, root)
        print("placing plot 5")
        pie3.get_tk_widget().place(x=1200, y=300)

        figure6 = Figure(figsize=(4,3), dpi=plotDPI)
        subplot6 = figure6.add_subplot(111)
        xAxis2 = [float(x1),float(x2),float(x3)]
        yAxis2 = [float(x1),float(x2),float(x3)]
        subplot6.bar(xAxis2,yAxis2, color = 'lightsteelblue')
        bar4 = FigureCanvasTkAgg(figure6, root)
        print("placing plot 6")
        bar4.get_tk_widget().place(x=1200, y=550)

        create_charts()




bruh = MainScreen()
bruh.initialize_configurations()

bruh.create_charts2()
bruh.draw_buttons()

while(True):
    #clear_output(wait=True)
    #bruh.commandbutton.configure(bg='gray')
    bruh.configure_buttons()
    create_charts()

    root.update()
    #clear_charts()

root.mainloop()