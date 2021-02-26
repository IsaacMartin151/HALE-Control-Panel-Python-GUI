import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as anim
from IPython.display import clear_output

#Setting variables for the GUI's main display
root= tk.Tk()
width = 1600
height = 500
plotDPI = 80

canvas1 = tk.Canvas(root, width = width, height = height)
background_image = tk.PhotoImage(file = "C:\\Users\\Isaac\\Desktop\\background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
canvas1.pack()

#Code for the 3 box entries to manually input data
#entry1 = tk.Entry (root)
#canvas1.create_window(width/2, 100, window=entry1)

#entry2 = tk.Entry (root)
#canvas1.create_window(width/2, 120, window=entry2)

#entry3 = tk.Entry (root)
#canvas1.create_window(width/2, 140, window=entry3)

#Dummy data
x1 = 10
x2 = 13
x3 = 23

#Left side charts
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

i = 1
k = 0
#Functions that are associated with the buttons
def create_charts():
    #These are data values at the top of this function
    global i
    global k
    #x1 = float(entry1.get())
    #x2 = float(entry2.get())
    #x3 = float(entry3.get())

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
    #subplot4.xlabel("x")
    #subplot4.ylabel("sinx")
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

def command_nogo():
    bar1.get_tk_widget().pack_forget()
    pie2.get_tk_widget().pack_forget()

def fuel_nogo():
    bar1.get_tk_widget().pack_forget()
    pie2.get_tk_widget().pack_forget()

def oxidizer_nogo():
    bar1.get_tk_widget().pack_forget()
    pie2.get_tk_widget().pack_forget()

def create_primary_display():
    #root = tk.Tk()
    #Code to create the main GUI

    #Adding the header
    label1 = tk.Label(root, text='Control Panel')
    label1.config(font=('Arial', 20))
    canvas1.create_window(width/2, 50, window=label1)

    create_charts()
    #Buttons for cancelling oxidizer, fuel, and command
    fuelbutton = tk.Button (root, text=' FUEL NOGO ',command=fuel_nogo, bg='red', font=('Arial', 11, 'bold'), width=30, height = 5)
    canvas1.create_window(width/2+width/4, 180, window=fuelbutton)

    oxidizerbutton = tk.Button (root, text=' OXIDIZER NOGO ',command=oxidizer_nogo, bg='red', font=('Arial', 11, 'bold'), width=30, height = 5)
    canvas1.create_window(width/2-width/4, 180, window=oxidizerbutton)

    commandbutton = tk.Button (root, text=' COMMAND NOGO ',command=command_nogo, bg='red', font=('Arial', 11, 'bold'), width=30, height = 5)
    canvas1.create_window(width/2, 180, window=commandbutton)

    standardizedButtonHeight = 2
    standardizedButtonWidth = 25
    startingHeight = 350
    heightSpacing = 40



    #Left column of center buttons
    commandbutton = tk.Button (root, text=' ABV-PR-120 (FUEL PRESS) ',command=command_nogo, bg='green', font=('Arial', 10, 'bold'))
    commandbutton.config(height = standardizedButtonHeight, width = standardizedButtonWidth)
    canvas1.create_window(width/2 - 120, startingHeight + heightSpacing*0, window=commandbutton)
    commandbutton = tk.Button (root, text=' ABV-FU-310 (FUEL VENT) ',command=command_nogo, bg='orange', font=('Arial', 10, 'bold'))
    commandbutton.config(height = standardizedButtonHeight, width = standardizedButtonWidth)
    canvas1.create_window(width/2 - 120, startingHeight + heightSpacing*1, window=commandbutton)
    commandbutton = tk.Button (root, text=' ABV-FU-320 (FUEL ISOLATION) ',command=command_nogo, bg='orange', font=('Arial', 10, 'bold'))
    commandbutton.config(height = standardizedButtonHeight, width = standardizedButtonWidth)
    canvas1.create_window(width/2 - 120, startingHeight + heightSpacing*2, window=commandbutton)
    commandbutton = tk.Button (root, text=' ABV-FU-330 (FUEL PURGE) ',command=command_nogo, bg='orange', font=('Arial', 10, 'bold'))
    commandbutton.config(height = standardizedButtonHeight, width = standardizedButtonWidth)
    canvas1.create_window(width/2 - 120, startingHeight + heightSpacing*3, window=commandbutton)
    commandbutton = tk.Button (root, text=' ABV-FU-340 (FUEL MAIN) ',command=command_nogo, bg='orange', font=('Arial', 10, 'bold'))
    commandbutton.config(height = standardizedButtonHeight, width = standardizedButtonWidth)
    canvas1.create_window(width/2 - 120, startingHeight + heightSpacing*4, window=commandbutton)

    #Right column of center buttons
    commandbutton = tk.Button (root, text=' ABV-PR-110 (LOx PRESS) ',command=command_nogo, bg='green', font=('Arial', 10, 'bold'))
    commandbutton.config(height = standardizedButtonHeight, width = standardizedButtonWidth)
    canvas1.create_window(width/2 + 120, startingHeight + heightSpacing*0, window=commandbutton)
    commandbutton = tk.Button (root, text=' ABV-FU-310 (LOx VENT) ',command=command_nogo, bg='blue', font=('Arial', 10, 'bold'))
    commandbutton.config(height = standardizedButtonHeight, width = standardizedButtonWidth)
    canvas1.create_window(width/2 + 120, startingHeight + heightSpacing*1, window=commandbutton)
    commandbutton = tk.Button (root, text=' ABV-FU-320 (LOx ISOLATION) ',command=command_nogo, bg='blue', font=('Arial', 10, 'bold'))
    commandbutton.config(height = standardizedButtonHeight, width = standardizedButtonWidth)
    canvas1.create_window(width/2 + 120, startingHeight + heightSpacing*2, window=commandbutton)
    commandbutton = tk.Button (root, text=' ABV-FU-330 (LOx CHILL) ',command=command_nogo, bg='blue', font=('Arial', 10, 'bold'))
    commandbutton.config(height = standardizedButtonHeight, width = standardizedButtonWidth)
    canvas1.create_window(width/2 + 120, startingHeight + heightSpacing*3, window=commandbutton)
    commandbutton = tk.Button (root, text=' ABV-FU-340 (LOx MAIN) ',command=command_nogo, bg='blue', font=('Arial', 10, 'bold'))
    commandbutton.config(height = standardizedButtonHeight, width = standardizedButtonWidth)
    canvas1.create_window(width/2 + 120, startingHeight + heightSpacing*4, window=commandbutton)

create_primary_display()

while(True):
    #clear_output(wait=True)
    create_charts()
    root.update()
    #clear_charts()

root.mainloop()