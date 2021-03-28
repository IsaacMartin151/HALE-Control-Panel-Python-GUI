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

i = 1
k = 0
plotDPI = 60

# Button states
global fuel_button_on
global oxidizer_button_on
global command_button_on

global fuel_press_on
global fuel_vent_on
global fuel_isolation_on
global fuel_purge_on
global fuel_main_on

global lox_press_on
global lox_vent_on
global lox_isolation_on
global lox_chill_on
global lox_main_on

global nanny_on
global sensor_stop_on
global cycle_valves_on
global cycle_vent_on
global data_live_on
global fire_on
global engine_start_up_on
global abort_on

fuel_nogo_on = False
oxidizer_nogo_on = False
command_nogo_on = False

fuel_press_on = True
fuel_vent_on = True
fuel_isolation_on = True
fuel_purge_on = True
fuel_main_on = True

lox_press_on = True
lox_vent_on = True
lox_isolation_on = True
lox_chill_on = True
lox_main_on = True
lox_fill_on = True

nanny_on = False
sensor_stop_on = False
cycle_valves_on = False
cycle_vent_on = False
data_live_on = False
fire_on = False
engine_start_up_on = False
abort_on = False

class MainScreen:
    #Setting variables for the GUI's main display
    width = 1600
    height = 900

    standardizedButtonHeight = 2
    standardizedButtonWidth = 25
    startingHeight = 350
    heightSpacing = 40

    #Dummy data
    x1 = 10
    x2 = 13
    x3 = 23

    root = tk.Tk()
    canvas1 = tk.Canvas(root, width = width, height = height)
    background_image = tk.PhotoImage(file = "./background.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    canvas1.pack()

    label1 = tk.Label(root, text='Control Panel')
    label1.config(font=('Arial', 20))
    canvas1.create_window(width/2, 50, window=label1)

    # toggles state of buttons when clicked
    def command_nogo_toggle():
        global command_button_on
        command_button_on = not command_nogo_on

    def fuel_nogo_toggle():
        global fuel_nogo_on
        fuel_nogo_on = not fuel_nogo_on

    def oxidizer_nogo_toggle():
        global oxidizer_nogo_on
        oxidizer_nogo_on = not oxidizer_nogo_on

    def nanny_toggle():
        global nanny_on
        nanny_on = not nanny_on


    def sensor_stop_toggle():
        global sensor_stop_on
        sensor_stop_on = not sensor_stop_on

    def cycle_valves_toggle():
        global cycle_valves_on
        cycle_valves_on = not cycle_valves_on

    def cycle_vent_toggle():
        global cycle_vent_on
        cycle_vent_on = not cycle_vent_on

    def data_live_toggle():
        global data_live_on
        data_live_on = not data_live_on


    def fuel_vent_toggle():
        global fuel_vent_on
        fuel_vent_on = not fuel_vent_on

    def fuel_press_toggle():
        global fuel_press_on
        fuel_press_on = not fuel_press_on

    def fuel_isolation_toggle():
        global fuel_isolation_on
        fuel_isolation_on = not fuel_isolation_on

    def fuel_purge_toggle():
        global fuel_purge_on
        fuel_purge_on = not fuel_purge_on

    def fuel_main_toggle():
        global fuel_main_on
        fuel_main_on = not fuel_main_on


    def lox_vent_toggle():
        global lox_vent_on
        lox_vent_on = not lox_vent_on

    def lox_press_toggle():
        global lox_press_on
        lox_press_on = not lox_press_on

    def lox_isolation_toggle():
        global lox_isolation_on
        lox_isolation_on = not lox_isolation_on

    def lox_chill_toggle():
        global lox_chill_on
        lox_chill_on = not lox_chill_on

    def lox_main_toggle():
        global lox_main_on
        lox_main_on = not lox_main_on

    def lox_fill_toggle():
        global lox_fill_on
        lox_fill_on = not lox_fill_on


    def fire_toggle():
        global fire_on
        fire_on = not fire_on

    def engine_start_up_toggle():
        global engine_start_up_on
        engine_start_up_on = not engine_start_up_on

    def abort_toggle():
        global abort_on
        abort_on = not abort_on


    # Creating the data for the top three buttons
    fuel_nogo_button     = tk.Button(root, text=' FUEL \'NOGO\' ', command=fuel_nogo_toggle, bg='red', font=('Arial', 11))
    oxidizer_nogo_button = tk.Button(root, text=' OXIDIZER \'NOGO\' ', command=oxidizer_nogo_toggle, bg='red', font=('Arial', 11))
    command_nogo_button  = tk.Button(root, text=' COMMAND \'NOGO\' ', command=command_nogo_toggle, bg='red', font=('Arial', 11))
    nanny_button    = tk.Button(root, text='    Nanny \'OFF\'    ', command=nanny_toggle, bg='pink', font=('Arial', 11))

    # Side buttons
    sensor_stop_button  = tk.Button(root, text=' Sensor Stop ', command=sensor_stop_toggle, fg='red', bg='gray80', font=('Arial', 11))
    cycle_valves_button = tk.Button(root, text=' Valve Sequence OFF ', command=cycle_valves_toggle, bg='gray80', font=('Arial', 11))
    cycle_vent_button   = tk.Button(root, text=' Cycle Vent OFF ', command=cycle_vent_toggle, bg='gray80', font=('Arial', 11))
    data_live_button    = tk.Button(root, text=' DATA PAUSED ', command=data_live_toggle, bg='gray90', font=('Arial', 11))

    # Creating the data for the left column of center buttons
    fuel_press_button     = tk.Button(root, text=' ABV-PR-120 (FUEL PRESS) ', command=fuel_press_toggle, bg='green2', font=('Arial', 10))
    fuel_vent_button      = tk.Button(root, text=' ABV-FU-310 (FUEL VENT) ', command=fuel_vent_toggle, bg='orange', font=('Arial', 10))
    fuel_isolation_button = tk.Button(root, text=' ABV-FU-320 (FUEL ISOLATION) ', command=fuel_isolation_toggle, bg='orange', font=('Arial', 10))
    fuel_purge_button     = tk.Button(root, text=' ABV-FU-330 (FUEL PURGE) ', command=fuel_purge_toggle, bg='orange', font=('Arial', 10))
    fuel_main_button      = tk.Button(root, text=' ABV-FU-340 (FUEL MAIN) ', command=fuel_main_toggle, bg='orange', font=('Arial', 10))

    # Creating the data for the right column of center buttons
    lox_press_button     = tk.Button(root, text=' ABV-PR-110 (LOx PRESS) ', command=lox_press_toggle, bg='green2', font=('Arial', 10))
    lox_vent_button      = tk.Button(root, text=' ABV-OX-210 (LOx VENT) ', command=lox_vent_toggle, bg='cyan', font=('Arial', 10))
    lox_isolation_button = tk.Button(root, text=' ABV-OX-220 (LOx ISOLATION) ', command=lox_isolation_toggle, bg='cyan', font=('Arial', 10))
    lox_chill_button     = tk.Button(root, text=' ABV-OX-230 (LOx CHILL) ', command=lox_chill_toggle, bg='cyan', font=('Arial', 10))
    lox_main_button      = tk.Button(root, text=' ABV-OX-240 (LOx MAIN) ', command=lox_main_toggle, bg='cyan', font=('Arial', 10))
    lox_fill_button      = tk.Button(root, text=' ABV-OX-250 (LOx FILL) ', command=lox_fill_toggle, bg='cyan', font=('Arial', 10))

    fire_button            = tk.Button(root, text=' FIRE ', command=fire_toggle, fg='white', bg='black', font=('Arial', 10))
    engine_start_up_button = tk.Button(root, text=' Engine Start Up ', command=engine_start_up_toggle, bg='gray80', font=('Arial', 10))
    abort_button           = tk.Button(root, text='    ABORT    ', command=abort_toggle, bg='red', font=('Arial', 11))


    #set uniform sizes for buttons that don't have unique sizes
    def initialize_configurations(self):
        self.fuel_nogo_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.oxidizer_nogo_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.command_nogo_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)

        self.sensor_stop_button.config(height=self.standardizedButtonHeight, width= self.standardizedButtonWidth//2)
        self.cycle_valves_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth//2)
        self.cycle_vent_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth//2)

        self.data_live_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth//2)

        self.fuel_press_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.fuel_vent_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.fuel_isolation_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.fuel_purge_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.fuel_main_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)

        self.lox_press_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.lox_vent_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.lox_isolation_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.lox_chill_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.lox_main_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.lox_fill_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)

        self.fire_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth//2 - 1)
        self.engine_start_up_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth//2 - 1)


    def draw_buttons(self):
        #Draw the buttons based on their current state
        self.canvas1.create_window(self.width/2 + self.width/4, 180, window=self.fuel_nogo_button)
        self.canvas1.create_window(self.width/2 - self.width/4, 180, window=self.oxidizer_nogo_button)
        self.canvas1.create_window(self.width/2, 180, window=self.command_nogo_button)

        self.canvas1.create_window(self.width/2, 120, window=self.nanny_button)

        self.canvas1.create_window(self.width/2 - self.width/4, self.startingHeight + self.heightSpacing*0, window=self.sensor_stop_button)
        self.canvas1.create_window(self.width/2 - self.width/4, self.startingHeight + self.heightSpacing*2, window=self.cycle_valves_button)
        self.canvas1.create_window(self.width/2 - self.width/4, self.startingHeight + self.heightSpacing*3, window=self.cycle_vent_button)

        self.canvas1.create_window(self.width/2 + self.width/4 - 100, self.startingHeight + self.heightSpacing*0, window=self.data_live_button)

        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*0, window=self.lox_press_button)
        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*1, window=self.lox_vent_button)
        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*2, window=self.lox_isolation_button)
        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*3, window=self.lox_chill_button)
        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*4, window=self.lox_main_button)
        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*5, window=self.lox_fill_button)

        self.canvas1.create_window(self.width/2 - 120, self.startingHeight + self.heightSpacing*0, window=self.fuel_press_button)
        self.canvas1.create_window(self.width/2 - 120, self.startingHeight + self.heightSpacing*1, window=self.fuel_vent_button)
        self.canvas1.create_window(self.width/2 - 120, self.startingHeight + self.heightSpacing*2, window=self.fuel_isolation_button)
        self.canvas1.create_window(self.width/2 - 120, self.startingHeight + self.heightSpacing*3, window=self.fuel_purge_button)
        self.canvas1.create_window(self.width/2 - 120, self.startingHeight + self.heightSpacing*4, window=self.fuel_main_button)

        self.canvas1.create_window(self.width/2 + self.width/4, self.startingHeight + self.heightSpacing*5, window=self.fire_button)
        self.canvas1.create_window(self.width/2 + self.width/4, self.startingHeight + self.heightSpacing*6, window=self.engine_start_up_button)

        self.canvas1.create_window(self.width/2 + self.width/4, self.startingHeight + self.heightSpacing*7, window=self.abort_button)

    # change button appearance after toggle
    def configure_buttons(self):
        if fuel_nogo_on:
            self.fuel_nogo_button.configure(text=' FUEL \'GO\' ', bg='green2')
        else:
            self.fuel_nogo_button.configure(text=' FUEL \'NOGO\' ', bg='red')

        if oxidizer_nogo_on:
            self.oxidizer_nogo_button.configure(text=' OXIDIZER \'GO\' ', bg='green2')
        else:
            self.oxidizer_nogo_button.configure(text=' OXIDIZER \'NOGO\' ', bg='red')

        if command_nogo_on:
            self.command_nogo_button.configure(text=' COMMAND \'GO\' ', bg='green2')
        else:
            self.command_nogo_button.configure(text=' COMMAND \'NOGO\' ', bg='red')

        if nanny_on:
            self.nanny_button.configure(text='    Nanny \'ON\'    ', bg='yellow')
        else:
            self.nanny_button.configure(text='    Nanny \'OFF\'    ', bg='pink')

        if sensor_stop_on:
            self.sensor_stop_button.configure(bg='gray60')
        else:
            self.sensor_stop_button.configure(bg='gray80')

        if cycle_valves_on:
            self.cycle_valves_button.configure(text=' Cycle Valves ON ', bg='bisque')
        else:
            self.cycle_valves_button.configure(text=' Valve Seq OFF ', bg='gray80')

        if cycle_vent_on:
            self.cycle_vent_button.configure(text=' Cycle Vent ON ', bg='bisque')
        else:
            self.cycle_vent_button.configure(text=' Cycle Vent OFF ', bg='gray80')

        if data_live_on:
            self.data_live_button.configure(text=' DATA LIVE ', bg='SteelBlue1')
        else:
            self.data_live_button.configure(text=' DATA PAUSED ', bg='gray90')

        if fuel_press_on:
            self.fuel_press_button.configure(bg='green2')
        else:
            self.fuel_press_button.configure(bg='red')

        if fuel_vent_on:
            self.fuel_vent_button.configure(bg='orange')
        else:
            self.fuel_vent_button.configure(bg='red')

        if fuel_isolation_on:
            self.fuel_isolation_button.configure(bg='orange')
        else:
            self.fuel_isolation_button.configure(bg='red')

        if fuel_purge_on:
            self.fuel_purge_button.configure(bg='orange')
        else:
            self.fuel_purge_button.configure(bg='red')

        if fuel_main_on:
            self.fuel_main_button.configure(bg='orange')
        else:
            self.fuel_main_button.configure(bg='red')

        if lox_press_on:
            self.lox_press_button.configure(bg='green2')
        else:
            self.lox_press_button.configure(bg='red')

        if lox_vent_on:
            self.lox_vent_button.configure(bg='cyan')
        else:
            self.lox_vent_button.configure(bg='red')

        if lox_isolation_on:
            self.lox_isolation_button.configure(bg='cyan')
        else:
            self.lox_isolation_button.configure(bg='red')

        if lox_chill_on:
            self.lox_chill_button.configure(bg='cyan')
        else:
            self.lox_chill_button.configure(bg='red')

        if lox_main_on:
            self.lox_main_button.configure(bg='cyan')
        else:
            self.lox_main_button.configure(bg='red')

        if lox_fill_on:
            self.lox_fill_button.configure(bg='cyan')
        else:
            self.lox_fill_button.configure(bg='red')

        if fire_on:
            self.fire_button.configure(text=' FIRING ', fg='black', bg='yellow')
        else:
            self.fire_button.configure(text=' FIRE ', fg='white', bg='black')

        if engine_start_up_on:
            self.engine_start_up_button.configure(text=' Start Up Timing ON ', bg='bisque')
        else:
            self.engine_start_up_button.configure(text=' Engine Start Up ', bg='gray80')

        if abort_on:
            self.abort_button.configure(text='    ABORT TRIPPED    ', bg='yellow')
        else:
            self.abort_button.configure(text='    ABORT    ', bg='red')


    def create_charts(self):
        # These are data values at the top of this function
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
        scatter1 = FigureCanvasTkAgg(figure7, self.root)
        scatter1.get_tk_widget().place(x=700, y=550)

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
        bar1 = FigureCanvasTkAgg(figure1, self.root)
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
        pie2 = FigureCanvasTkAgg(figure2, self.root)
        print("placing plot 2")
        pie2.get_tk_widget().place(x=0, y=250)

        figure3 = Figure(figsize=(4,3), dpi=plotDPI)
        subplot3 = figure3.add_subplot(111)
        xAxis2 = [float(x1),float(x2),float(x3)]
        yAxis2 = [float(x1),float(x2),float(x3)]
        subplot3.bar(xAxis2,yAxis2, color = 'lightsteelblue')
        bar2 = FigureCanvasTkAgg(figure3, self.root)
        print("placing plot 3")
        bar2.get_tk_widget().place(x=0, y=450)


        #Right side charts
        figure4 = Figure(figsize=(4,3), dpi=plotDPI)
        subplot4 = figure4.add_subplot(111)
        xAxis = [float(x1),float(x2),float(x3)]
        yAxis = [float(x1),float(x2),float(x3)]
        subplot4.bar(xAxis,yAxis, color = 'lightsteelblue')
        bar3 = FigureCanvasTkAgg(figure4, self.root)
        print("placing plot 4")
        bar3.get_tk_widget().place(x=1300, y=50)

        figure5 = Figure(figsize=(4,3), dpi=plotDPI)
        subplot5 = figure5.add_subplot(111)
        labels2 = 'Fuel Level', 'Oxidizer\nLevel', 'Regulator\npressure'
        pieSizes = [float(x1),float(x2),float(x3)]
        my_colors2 = ['lightblue','lightsteelblue','silver']
        explode2 = (0, 0, 0)
        subplot5.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=False, startangle=90)
        subplot5.axis('equal')
        pie3 = FigureCanvasTkAgg(figure5, self.root)
        print("placing plot 5")
        pie3.get_tk_widget().place(x=1300, y=250)

        figure6 = Figure(figsize=(4,3), dpi=plotDPI)
        subplot6 = figure6.add_subplot(111)
        xAxis2 = [float(x1),float(x2),float(x3)]
        yAxis2 = [float(x1),float(x2),float(x3)]
        subplot6.bar(xAxis2,yAxis2, color = 'lightsteelblue')
        bar4 = FigureCanvasTkAgg(figure6, self.root)
        print("placing plot 6")
        bar4.get_tk_widget().place(x=1300, y=450)

        self.create_charts()



class Screen2:
    #Setting variables for the GUI's main display
    width = 1600
    height = 900

    standardizedButtonHeight = 2
    standardizedButtonWidth = 25
    startingHeight = 350
    heightSpacing = 40

    #Dummy data
    x1 = 10
    x2 = 13
    x3 = 23

    root = tk.Toplevel()
    canvas1 = tk.Canvas(root, width = width, height = height)
    background_image = tk.PhotoImage(file = "./background2.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    canvas1.pack()

    label1 = tk.Label(root, text='Control Panel')
    label1.config(font=('Arial', 20))
    canvas1.create_window(width/2, 50, window=label1)

    # toggles state of buttons when clicked
    def command_nogo_toggle():
        global command_button_on
        command_button_on = not command_nogo_on

    def fuel_nogo_toggle():
        global fuel_nogo_on
        fuel_nogo_on = not fuel_nogo_on

    def oxidizer_nogo_toggle():
        global oxidizer_nogo_on
        oxidizer_nogo_on = not oxidizer_nogo_on

    def nanny_toggle():
        global nanny_on
        nanny_on = not nanny_on


    def sensor_stop_toggle():
        global sensor_stop_on
        sensor_stop_on = not sensor_stop_on

    def cycle_valves_toggle():
        global cycle_valves_on
        cycle_valves_on = not cycle_valves_on

    def cycle_vent_toggle():
        global cycle_vent_on
        cycle_vent_on = not cycle_vent_on

    def data_live_toggle():
        global data_live_on
        data_live_on = not data_live_on


    def fuel_vent_toggle():
        global fuel_vent_on
        fuel_vent_on = not fuel_vent_on

    def fuel_press_toggle():
        global fuel_press_on
        fuel_press_on = not fuel_press_on

    def fuel_isolation_toggle():
        global fuel_isolation_on
        fuel_isolation_on = not fuel_isolation_on

    def fuel_purge_toggle():
        global fuel_purge_on
        fuel_purge_on = not fuel_purge_on

    def fuel_main_toggle():
        global fuel_main_on
        fuel_main_on = not fuel_main_on


    def lox_vent_toggle():
        global lox_vent_on
        lox_vent_on = not lox_vent_on

    def lox_press_toggle():
        global lox_press_on
        lox_press_on = not lox_press_on

    def lox_isolation_toggle():
        global lox_isolation_on
        lox_isolation_on = not lox_isolation_on

    def lox_chill_toggle():
        global lox_chill_on
        lox_chill_on = not lox_chill_on

    def lox_main_toggle():
        global lox_main_on
        lox_main_on = not lox_main_on

    def lox_fill_toggle():
        global lox_fill_on
        lox_fill_on = not lox_fill_on


    def fire_toggle():
        global fire_on
        fire_on = not fire_on

    def engine_start_up_toggle():
        global engine_start_up_on
        engine_start_up_on = not engine_start_up_on

    def abort_toggle():
        global abort_on
        abort_on = not abort_on


    # Creating the data for the top three buttons
    fuel_nogo_button     = tk.Button(root, text=' FUEL \'NOGO\' ', command=fuel_nogo_toggle, bg='red', font=('Arial', 11))
    oxidizer_nogo_button = tk.Button(root, text=' OXIDIZER \'NOGO\' ', command=oxidizer_nogo_toggle, bg='red', font=('Arial', 11))
    command_nogo_button  = tk.Button(root, text=' COMMAND \'NOGO\' ', command=command_nogo_toggle, bg='red', font=('Arial', 11))
    nanny_button    = tk.Button(root, text='    Nanny \'OFF\'    ', command=nanny_toggle, bg='pink', font=('Arial', 11))

    # Side buttons
    sensor_stop_button  = tk.Button(root, text=' Sensor Stop ', command=sensor_stop_toggle, fg='red', bg='gray80', font=('Arial', 11))
    cycle_valves_button = tk.Button(root, text=' Valve Sequence OFF ', command=cycle_valves_toggle, bg='gray80', font=('Arial', 11))
    cycle_vent_button   = tk.Button(root, text=' Cycle Vent OFF ', command=cycle_vent_toggle, bg='gray80', font=('Arial', 11))
    data_live_button    = tk.Button(root, text=' DATA PAUSED ', command=data_live_toggle, bg='gray90', font=('Arial', 11))

    # Creating the data for the left column of center buttons
    fuel_press_button     = tk.Button(root, text=' ABV-PR-120 (FUEL PRESS) ', command=fuel_press_toggle, bg='green2', font=('Arial', 10))
    fuel_vent_button      = tk.Button(root, text=' ABV-FU-310 (FUEL VENT) ', command=fuel_vent_toggle, bg='orange', font=('Arial', 10))
    fuel_isolation_button = tk.Button(root, text=' ABV-FU-320 (FUEL ISOLATION) ', command=fuel_isolation_toggle, bg='orange', font=('Arial', 10))
    fuel_purge_button     = tk.Button(root, text=' ABV-FU-330 (FUEL PURGE) ', command=fuel_purge_toggle, bg='orange', font=('Arial', 10))
    fuel_main_button      = tk.Button(root, text=' ABV-FU-340 (FUEL MAIN) ', command=fuel_main_toggle, bg='orange', font=('Arial', 10))

    # Creating the data for the right column of center buttons
    lox_press_button     = tk.Button(root, text=' ABV-PR-110 (LOx PRESS) ', command=lox_press_toggle, bg='green2', font=('Arial', 10))
    lox_vent_button      = tk.Button(root, text=' ABV-OX-210 (LOx VENT) ', command=lox_vent_toggle, bg='cyan', font=('Arial', 10))
    lox_isolation_button = tk.Button(root, text=' ABV-OX-220 (LOx ISOLATION) ', command=lox_isolation_toggle, bg='cyan', font=('Arial', 10))
    lox_chill_button     = tk.Button(root, text=' ABV-OX-230 (LOx CHILL) ', command=lox_chill_toggle, bg='cyan', font=('Arial', 10))
    lox_main_button      = tk.Button(root, text=' ABV-OX-240 (LOx MAIN) ', command=lox_main_toggle, bg='cyan', font=('Arial', 10))
    lox_fill_button      = tk.Button(root, text=' ABV-OX-250 (LOx FILL) ', command=lox_fill_toggle, bg='cyan', font=('Arial', 10))

    fire_button            = tk.Button(root, text=' FIRE ', command=fire_toggle, fg='white', bg='black', font=('Arial', 10))
    engine_start_up_button = tk.Button(root, text=' Engine Start Up ', command=engine_start_up_toggle, bg='gray80', font=('Arial', 10))
    abort_button           = tk.Button(root, text='    ABORT    ', command=abort_toggle, bg='red', font=('Arial', 11))


    #set uniform sizes for buttons that don't have unique sizes
    def initialize_configurations(self):
        self.fuel_nogo_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.oxidizer_nogo_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.command_nogo_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)

        self.sensor_stop_button.config(height=self.standardizedButtonHeight, width= self.standardizedButtonWidth//2)
        self.cycle_valves_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth//2)
        self.cycle_vent_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth//2)

        self.data_live_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth//2)

        self.fuel_press_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.fuel_vent_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.fuel_isolation_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.fuel_purge_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.fuel_main_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)

        self.lox_press_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.lox_vent_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.lox_isolation_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.lox_chill_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.lox_main_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)
        self.lox_fill_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth)

        self.fire_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth//2 - 1)
        self.engine_start_up_button.config(height=self.standardizedButtonHeight, width=self.standardizedButtonWidth//2 - 1)


    def draw_buttons(self):
        #Draw the buttons based on their current state
        self.canvas1.create_window(self.width/2 + self.width/4, 180, window=self.fuel_nogo_button)
        self.canvas1.create_window(self.width/2 - self.width/4, 180, window=self.oxidizer_nogo_button)
        self.canvas1.create_window(self.width/2, 180, window=self.command_nogo_button)

        self.canvas1.create_window(self.width/2, 120, window=self.nanny_button)

        self.canvas1.create_window(self.width/2 - self.width/4, self.startingHeight + self.heightSpacing*0, window=self.sensor_stop_button)
        self.canvas1.create_window(self.width/2 - self.width/4, self.startingHeight + self.heightSpacing*2, window=self.cycle_valves_button)
        self.canvas1.create_window(self.width/2 - self.width/4, self.startingHeight + self.heightSpacing*3, window=self.cycle_vent_button)

        self.canvas1.create_window(self.width/2 + self.width/4 - 100, self.startingHeight + self.heightSpacing*0, window=self.data_live_button)

        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*0, window=self.lox_press_button)
        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*1, window=self.lox_vent_button)
        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*2, window=self.lox_isolation_button)
        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*3, window=self.lox_chill_button)
        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*4, window=self.lox_main_button)
        self.canvas1.create_window(self.width/2 + 120, self.startingHeight + self.heightSpacing*5, window=self.lox_fill_button)

        self.canvas1.create_window(self.width/2 - 120, self.startingHeight + self.heightSpacing*0, window=self.fuel_press_button)
        self.canvas1.create_window(self.width/2 - 120, self.startingHeight + self.heightSpacing*1, window=self.fuel_vent_button)
        self.canvas1.create_window(self.width/2 - 120, self.startingHeight + self.heightSpacing*2, window=self.fuel_isolation_button)
        self.canvas1.create_window(self.width/2 - 120, self.startingHeight + self.heightSpacing*3, window=self.fuel_purge_button)
        self.canvas1.create_window(self.width/2 - 120, self.startingHeight + self.heightSpacing*4, window=self.fuel_main_button)

        self.canvas1.create_window(self.width/2 + self.width/4, self.startingHeight + self.heightSpacing*5, window=self.fire_button)
        self.canvas1.create_window(self.width/2 + self.width/4, self.startingHeight + self.heightSpacing*6, window=self.engine_start_up_button)

        self.canvas1.create_window(self.width/2 + self.width/4, self.startingHeight + self.heightSpacing*7, window=self.abort_button)

    # change button appearance after toggle
    def configure_buttons(self):
        if fuel_nogo_on:
            self.fuel_nogo_button.configure(text=' FUEL \'GO\' ', bg='green2')
        else:
            self.fuel_nogo_button.configure(text=' FUEL \'NOGO\' ', bg='red')

        if oxidizer_nogo_on:
            self.oxidizer_nogo_button.configure(text=' OXIDIZER \'GO\' ', bg='green2')
        else:
            self.oxidizer_nogo_button.configure(text=' OXIDIZER \'NOGO\' ', bg='red')

        if command_nogo_on:
            self.command_nogo_button.configure(text=' COMMAND \'GO\' ', bg='green2')
        else:
            self.command_nogo_button.configure(text=' COMMAND \'NOGO\' ', bg='red')

        if nanny_on:
            self.nanny_button.configure(text='    Nanny \'ON\'    ', bg='yellow')
        else:
            self.nanny_button.configure(text='    Nanny \'OFF\'    ', bg='pink')

        if sensor_stop_on:
            self.sensor_stop_button.configure(bg='gray60')
        else:
            self.sensor_stop_button.configure(bg='gray80')

        if cycle_valves_on:
            self.cycle_valves_button.configure(text=' Cycle Valves ON ', bg='bisque')
        else:
            self.cycle_valves_button.configure(text=' Valve Seq OFF ', bg='gray80')

        if cycle_vent_on:
            self.cycle_vent_button.configure(text=' Cycle Vent ON ', bg='bisque')
        else:
            self.cycle_vent_button.configure(text=' Cycle Vent OFF ', bg='gray80')

        if data_live_on:
            self.data_live_button.configure(text=' DATA LIVE ', bg='SteelBlue1')
        else:
            self.data_live_button.configure(text=' DATA PAUSED ', bg='gray90')

        if fuel_press_on:
            self.fuel_press_button.configure(bg='green2')
        else:
            self.fuel_press_button.configure(bg='red')

        if fuel_vent_on:
            self.fuel_vent_button.configure(bg='orange')
        else:
            self.fuel_vent_button.configure(bg='red')

        if fuel_isolation_on:
            self.fuel_isolation_button.configure(bg='orange')
        else:
            self.fuel_isolation_button.configure(bg='red')

        if fuel_purge_on:
            self.fuel_purge_button.configure(bg='orange')
        else:
            self.fuel_purge_button.configure(bg='red')

        if fuel_main_on:
            self.fuel_main_button.configure(bg='orange')
        else:
            self.fuel_main_button.configure(bg='red')

        if lox_press_on:
            self.lox_press_button.configure(bg='green2')
        else:
            self.lox_press_button.configure(bg='red')

        if lox_vent_on:
            self.lox_vent_button.configure(bg='cyan')
        else:
            self.lox_vent_button.configure(bg='red')

        if lox_isolation_on:
            self.lox_isolation_button.configure(bg='cyan')
        else:
            self.lox_isolation_button.configure(bg='red')

        if lox_chill_on:
            self.lox_chill_button.configure(bg='cyan')
        else:
            self.lox_chill_button.configure(bg='red')

        if lox_main_on:
            self.lox_main_button.configure(bg='cyan')
        else:
            self.lox_main_button.configure(bg='red')

        if lox_fill_on:
            self.lox_fill_button.configure(bg='cyan')
        else:
            self.lox_fill_button.configure(bg='red')

        if fire_on:
            self.fire_button.configure(text=' FIRING ', fg='black', bg='yellow')
        else:
            self.fire_button.configure(text=' FIRE ', fg='white', bg='black')

        if engine_start_up_on:
            self.engine_start_up_button.configure(text=' Start Up Timing ON ', bg='bisque')
        else:
            self.engine_start_up_button.configure(text=' Engine Start Up ', bg='gray80')

        if abort_on:
            self.abort_button.configure(text='    ABORT TRIPPED    ', bg='yellow')
        else:
            self.abort_button.configure(text='    ABORT    ', bg='red')


    def create_charts(self):
        # These are data values at the top of this function
        global i
        global k
        figure7 = Figure(figsize=(4,3), dpi=plotDPI)
        subplot7 = figure7.add_subplot(111)
        x = np.linspace(0, 100, 200)
        #print("i is ", i)
        y = np.sin(2 * np.pi * x + k)
        subplot7.plot(x, y, color = 'lightsteelblue')
        #subplot4.title("Connected Scatterplot points with line")
        subplot7.set_xlabel("x")
        subplot7.set_ylabel("sinx")
        scatter1 = FigureCanvasTkAgg(figure7, self.root)
        scatter1.get_tk_widget().place(x=700, y=550)

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
        bar1 = FigureCanvasTkAgg(figure1, self.root)
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
        pie2 = FigureCanvasTkAgg(figure2, self.root)
        print("placing plot 2")
        pie2.get_tk_widget().place(x=0, y=250)

        figure3 = Figure(figsize=(4,3), dpi=plotDPI)
        subplot3 = figure3.add_subplot(111)
        xAxis2 = [float(x1),float(x2),float(x3)]
        yAxis2 = [float(x1),float(x2),float(x3)]
        subplot3.bar(xAxis2,yAxis2, color = 'lightsteelblue')
        bar2 = FigureCanvasTkAgg(figure3, self.root)
        print("placing plot 3")
        bar2.get_tk_widget().place(x=0, y=450)


        #Right side charts
        figure4 = Figure(figsize=(4,3), dpi=plotDPI)
        subplot4 = figure4.add_subplot(111)
        xAxis = [float(x1),float(x2),float(x3)]
        yAxis = [float(x1),float(x2),float(x3)]
        subplot4.bar(xAxis,yAxis, color = 'lightsteelblue')
        bar3 = FigureCanvasTkAgg(figure4, self.root)
        print("placing plot 4")
        bar3.get_tk_widget().place(x=1300, y=50)

        figure5 = Figure(figsize=(4,3), dpi=plotDPI)
        subplot5 = figure5.add_subplot(111)
        labels2 = 'Fuel Level', 'Oxidizer\nLevel', 'Regulator\npressure'
        pieSizes = [float(x1),float(x2),float(x3)]
        my_colors2 = ['lightblue','lightsteelblue','silver']
        explode2 = (0, 0, 0)
        subplot5.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=False, startangle=90)
        subplot5.axis('equal')
        pie3 = FigureCanvasTkAgg(figure5, self.root)
        print("placing plot 5")
        pie3.get_tk_widget().place(x=1300, y=250)

        figure6 = Figure(figsize=(4,3), dpi=plotDPI)
        subplot6 = figure6.add_subplot(111)
        xAxis2 = [float(x1),float(x2),float(x3)]
        yAxis2 = [float(x1),float(x2),float(x3)]
        subplot6.bar(xAxis2,yAxis2, color = 'lightsteelblue')
        bar4 = FigureCanvasTkAgg(figure6, self.root)
        print("placing plot 6")
        bar4.get_tk_widget().place(x=1300, y=450)

        #self.create_charts()


bruh = MainScreen()
bruh.initialize_configurations()
bruh.create_charts2()
bruh.draw_buttons()

oof = Screen2()
oof.initialize_configurations()
oof.create_charts2()
oof.draw_buttons()

# root2 = tk.Tk()
# canvas1 = tk.Canvas(root2, width = 1600, height = 900)
# background_label = tk.Label(root2)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
# canvas1.pack()

# label1 = tk.Label(root2, text='PANEL TWO')
# label1.config(font=('Arial', 20))
# canvas1.create_window(1600/2, 50, window=label1)

#Continuously display the Screens
while(True):
    #clear_output(wait=True)
    bruh.configure_buttons()
    bruh.create_charts()
    bruh.root.update()

    oof.configure_buttons()
    oof.create_charts()
    oof.root.update()
    #clear_charts()