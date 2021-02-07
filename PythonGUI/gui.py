import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#Code to create the main GUI
root= tk.Tk()

width = 1600
height = 500

canvas1 = tk.Canvas(root, width = width, height = height)
canvas1.pack()


#Adding the header
label1 = tk.Label(root, text='Control Panel')
label1.config(font=('Arial', 20))
canvas1.create_window(width/2, 50, window=label1)


#Code for the 3 box entries to manually input data
#entry1 = tk.Entry (root)
#canvas1.create_window(width/2, 100, window=entry1)

#entry2 = tk.Entry (root)
#canvas1.create_window(width/2, 120, window=entry2)

#entry3 = tk.Entry (root)
#canvas1.create_window(width/2, 140, window=entry3)


#Functions that are associated with the buttons
def create_charts():
    #These are data values at the top of this function
    global x1
    global x2
    global x3
    global bar1
    global pie2
    #x1 = float(entry1.get())
    #x2 = float(entry2.get())
    #x3 = float(entry3.get())
    x1 = 10
    x2 = 13
    x3 = 23


    figure1 = Figure(figsize=(4,3), dpi=80)
    subplot1 = figure1.add_subplot(111)
    xAxis = [float(x1),float(x2),float(x3)]
    yAxis = [float(x1),float(x2),float(x3)]
    subplot1.bar(xAxis,yAxis, color = 'lightsteelblue')
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=0)

    figure2 = Figure(figsize=(4,3), dpi=80)
    subplot2 = figure2.add_subplot(111)
    labels2 = 'Fuel Level', 'Oxidizer Level', 'Regulator pressure'
    pieSizes = [float(x1),float(x2),float(x3)]
    my_colors2 = ['lightblue','lightsteelblue','silver']
    explode2 = (0, 0, 0)
    subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=False, startangle=90)
    subplot2.axis('equal')
    pie2 = FigureCanvasTkAgg(figure2, root)
    pie2.get_tk_widget().pack()

    figure3 = Figure(figsize=(4,3), dpi=80)
    subplot3 = figure1.add_subplot(111)
    xAxis2 = [float(x1),float(x2),float(x3)]
    yAxis2 = [float(x1),float(x2),float(x3)]
    subplot3.bar(xAxis2,yAxis2, color = 'lightsteelblue')
    bar2 = FigureCanvasTkAgg(figure3, root)
    bar2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=0)

def clear_charts():
    bar1.get_tk_widget().pack_forget()
    pie2.get_tk_widget().pack_forget()

def command_nogo():
    bar1.get_tk_widget().pack_forget()
    pie2.get_tk_widget().pack_forget()

def fuel_nogo():
    bar1.get_tk_widget().pack_forget()
    pie2.get_tk_widget().pack_forget()

def oxidizer_nogo():
    bar1.get_tk_widget().pack_forget()
    pie2.get_tk_widget().pack_forget()


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


#Buttons to create and clear charts
#button1 = tk.Button (root, text=' Create Charts ',command=create_charts, bg='palegreen2', font=('Arial', 11, 'bold'))
#canvas1.create_window(width/2, startingHeight, window=button1)

#Button to close the panel
#button3 = tk.Button (root, text='Exit Application', command=root.destroy, bg='lightsteelblue2', font=('Arial', 11, 'bold'))
#canvas1.create_window(width/2, startingHeight + 50, window=button3)

create_charts()

root.mainloop()