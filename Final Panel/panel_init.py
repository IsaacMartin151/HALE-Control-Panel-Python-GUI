# Import Required Module
import tkinter as tk
from typing import Sized
import numpy as np
import random
import HALE
import enums

client = HALE.Interface()

main_panel = client.add_panel(HALE.Panel(size_x = 1600, size_y = 800))
engine_panel = client.add_panel(HALE.Panel(size_x = 1600, size_y = 800))
indicator_panel = client.add_panel(HALE.Panel(size_x = 1900, size_y = 950))


########## INDICATOR PANEL #########

#top right
indicator_panel.add_element(HALE.Image(file="./IndicatorPanelBg.PNG", z=HALE.Depths.BACKGROUND, pos_x=0, pos_y=0, size_x=1000, size_y=1000))

indicator_panel.add_element(HALE.IndicatorLight(text="Command",             starting_color="#969696", font=("Arial", 8), get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF0000" ), pos_x=788, pos_y=45, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Ox",                  starting_color="#969696", font=("Arial", 8), get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF0000" ), pos_x=788, pos_y=95, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Fuel",                starting_color="#969696", font=("Arial", 8), get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF0000" ), pos_x=788, pos_y=145, size_x = 55, size_y = 50, refresh_interval=1000))

indicator_panel.add_element(HALE.IndicatorLight(text="WS",                  starting_color="#969696", font=("Arial", 8), get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF0000" ), pos_x=829, pos_y=45, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Camera",              starting_color="#969696", font=("Arial", 8), get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF0000" ), pos_x=829, pos_y=95, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Office",              starting_color="#969696", font=("Arial", 8), get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF0000" ), pos_x=829, pos_y=145, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Record",              starting_color="#969696", font=("Arial", 8), get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF0000" ), pos_x=829, pos_y=195, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Igniter GO",          starting_color="#969696", font=("Arial", 8), get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF0000" ), pos_x=829, pos_y=245, size_x = 55, size_y = 50, refresh_interval=1000))

indicator_panel.add_element(HALE.IndicatorLight(text="Nanny",               starting_color="#969696", font=("Arial", 8), get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF0000" ), pos_x=872, pos_y=45, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Sequence Flow Meter", starting_color="#969696", font=("Arial", 8), get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF0000" ), pos_x=872, pos_y=145, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Cold Flow",           starting_color="#969696", font=("Arial", 8), get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF0000" ), pos_x=872, pos_y=245, size_x = 55, size_y = 50, refresh_interval=1000))

indicator_panel.add_element(HALE.IndicatorLight(text="ABORT",               starting_color="#969696", font=("Arial", 8), get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF0000" ), pos_x=939, pos_y=45, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Igniter Armed",       starting_color="#969696", font=("Arial", 8), get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF0000" ), pos_x=939, pos_y=145, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Startup",             starting_color="#969696", font=("Arial", 8), get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF0000" ), pos_x=939, pos_y=245, size_x = 55, size_y = 50, refresh_interval=1000))

#p&id
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#ff0000", get_data=None, pos_x=65, pos_y=86, size_x = 17, size_y = 29, refresh_interval=1000)) # ABV-WS-610

indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#00da6d", get_data=None, pos_x=325, pos_y=148, size_x = 15, size_y = 23, refresh_interval=1000)) # ABV-OX-210
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#00da6d", get_data=None, pos_x=623, pos_y=436, size_x = 15, size_y = 23, refresh_interval=1000)) # ABV-OX-220
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#00da6d", get_data=None, pos_x=695, pos_y=375, size_x = 15, size_y = 23, refresh_interval=1000)) # ABV-OX-230
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#00da6d", get_data=None, pos_x=777, pos_y=578, size_x = 15, size_y = 23, refresh_interval=1000)) # ABV-OX-320
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#00da6d", get_data=None, pos_x=487, pos_y=501, size_x = 15, size_y = 23, refresh_interval=1000)) # ABV-OX-250

indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#00da6d", get_data=None, pos_x=140, pos_y=342, size_x = 14, size_y = 24, refresh_interval=1000)) # ABV-PR-110
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#ff0000", get_data=None, pos_x=139, pos_y=674, size_x = 14, size_y = 24, refresh_interval=1000)) # ABV-PR-120

indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#00da6d", get_data=None, pos_x=317, pos_y=858, size_x = 14, size_y = 23, refresh_interval=1000)) # ABV-FU-310
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#ff0000", get_data=None, pos_x=619, pos_y=773, size_x = 14, size_y = 23, refresh_interval=1000)) # ABV-FU-320
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#ff0000", get_data=None, pos_x=786, pos_y=836, size_x = 14, size_y = 23, refresh_interval=1000)) # ABV-FU-330
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#ff0000", get_data=None, pos_x=777, pos_y=719, size_x = 14, size_y = 23, refresh_interval=1000)) # ABV-FU-340
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#00da6d", get_data=None, pos_x=451, pos_y=846, size_x = 14, size_y = 23, refresh_interval=1000)) # MBV-FU-350





########## ENGINE PANEL ###########
engine_panel.add_element(HALE.Image(file="./haleblack.png", pos_x=335, pos_y=50, size_x=291, size_y=215))

engine_panel.add_element(HALE.PushButton(text="Second Panel", onclick = lambda : (log_box.add_message(text="Second panel label clicked", color="Red")), text_color="black", bgcolor = "#DDDDDD", font_size= 30, pos_x = 1500, pos_y = 700, size_x = 100, size_y = 100))

tank_temps        = engine_panel.add_element(HALE.Chart(pos_x = 0, pos_y = 0, size_x = 300, size_y = 400, title="Tank Temps", xlabel="Time", ylabel="Pressure"))
chamber_pressures = engine_panel.add_element(HALE.Chart(pos_x = 650, pos_y = 0, size_x = 300, size_y = 400, title="Chamber Pressures", xlabel="Time", ylabel="Amplitude"))
thrust_pressure   = engine_panel.add_element(HALE.Chart(pos_x = 120, pos_y = 600, size_x = 700, size_y = 350, title="Pressures(psi) - Thrust (lbf)", xlabel="Time", ylabel="Thrust - Pressure"))

engine_panel.add_element(HALE.IndicatorLight(text="Ox Main Valve",   starting_color="#0e6e07", get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#0e6e07" ), pos_x = 20, pos_y = 640, size_x = 100, size_y = 50, refresh_interval = 50))
engine_panel.add_element(HALE.IndicatorLight(text="Fuel Main Valve", starting_color="#0e6e07", get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF00FF" ), pos_x = 20, pos_y = 740, size_x = 100, size_y = 50, refresh_interval = 50))

########## MAIN PANEL ###########


#logging box
log_box = main_panel.add_element(HALE.LoggingBox(pos_x = 0, pos_y = 800, size_x = 200, size_y = 100))

#top
main_panel.add_element(HALE.PushButton(text="WATER SUPPRESSION", text_color="black", bgcolor = "#DDDDDD", font_size= 12, pos_x = 430, pos_y = 20, size_x = 140, size_y = 50))

main_panel.add_element(HALE.ToggleButton(off_text="FUEL NOGO",    on_text = "FUEL GO",    font_size= 16, pos_x = 270, pos_y = 110, size_x = 135, size_y = 60))
main_panel.add_element(HALE.ToggleButton(off_text="COMMAND NOGO", on_text = "COMMAND GO", font_size= 16, pos_x = 414, pos_y = 110, size_x = 183, size_y = 60))
main_panel.add_element(HALE.ToggleButton(off_text="OX NOGO",      on_text = "OX GO",      font_size= 16, pos_x = 606, pos_y = 110, size_x = 135, size_y = 60))

main_panel.add_element(HALE.IndicatorLight(text="ABV-WS-610 LED", starting_color="#0e6e07", get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#0e6e07" ), pos_x = 600, pos_y = 30, size_x = 150, size_y = 50, refresh_interval = 50))


#right side, from top to bottom
main_panel.add_element(HALE.IndicatorLight(text="Igniter",        starting_color="#FF0000", get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF0000" ), pos_x = 815, pos_y = 30, size_x = 150, size_y = 50, refresh_interval = 500))
main_panel.add_element(HALE.IndicatorLight(text="ABV-WS-620 LED", starting_color="#0e6e07", get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#0e6e07" ), pos_x = 790, pos_y = 110, size_x = 150, size_y = 50, refresh_interval = 1000))

main_panel.add_element(HALE.PushButton(text="Go Away Fire (Please)", text_color="black", bgcolor = "#BBBBBB", font_size= 16, pos_x = 790, pos_y = 170, size_x = 140, size_y = 80))
main_panel.add_element(HALE.PushButton(text="System Cycle OFF",      text_color="black", bgcolor = "#BBBBBB", font_size= 12, pos_x = 810, pos_y = 270, size_x = 100, size_y = 50))

main_panel.add_element(HALE.IndicatorLight(text="Flow Meter Installed",  starting_color="#0e6e07", get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#0e6e07" ), pos_x = 750, pos_y = 340, size_x = 150, size_y = 50, refresh_interval = 250))
main_panel.add_element(HALE.IndicatorLight(text="Cryo Cold Flow Active", starting_color="#0e6e07", get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF00FF" ), pos_x = 870, pos_y = 340, size_x = 150, size_y = 50, refresh_interval = 50))

main_panel.add_element(HALE.PushButton(text="Cold Flow",       text_color="black",  bgcolor = "#BBBBBB", font_size= 12, pos_x = 800, pos_y = 400, size_x = 110, size_y = 60))
main_panel.add_element(HALE.PushButton(text="Engine Start Up", text_color="black", bgcolor = "#999999", font_size= 12, pos_x = 780, pos_y = 510, size_x = 160, size_y = 65))

main_panel.add_element(HALE.ToggleButton(off_text="1 Second Purge OFF",  on_text = "1 Second Purge ON", on_bgcolor="#AAAAAA", off_bgcolor = "#CCCCCC", on_text_color="#0022FF", off_text_color = "#010101", font_size= 10, pos_x = 765, pos_y = 590, size_x = 90, size_y = 50))
main_panel.add_element(HALE.ToggleButton(off_text="2 Second Purge OFF",  on_text = "2 Second Purge ON", on_bgcolor="#AAAAAA", off_bgcolor = "#CCCCCC", on_text_color="#0022FF", off_text_color = "#010101", font_size= 10, pos_x = 870, pos_y = 590, size_x = 90, size_y = 50))
main_panel.add_element(HALE.ToggleButton(off_text="Cycle Fuel Vent OFF", on_text = "Cycle Fuel Vent ON", on_bgcolor="#AAAAAA", off_bgcolor = "#CCCCCC", on_text_color="#0022FF", off_text_color = "#010101", font_size= 10, pos_x = 765, pos_y = 690, size_x = 90, size_y = 50))
main_panel.add_element(HALE.ToggleButton(off_text="Cycle Ox Vent OFF",   on_text = "Cycle Ox Vent ON", on_bgcolor="#AAAAAA", off_bgcolor = "#CCCCCC", on_text_color="#0022FF", off_text_color = "#010101", font_size= 10, pos_x = 870, pos_y = 690, size_x = 90, size_y = 50))

main_panel.add_element(HALE.PushButton(text="Fuel Press Control", text_color="black", bgcolor = "#BBBBBB", font_size= 12, pos_x = 755, pos_y = 775, size_x = 100, size_y = 45))
main_panel.add_element(HALE.PushButton(text="Ox Press Control",   text_color="black", bgcolor = "#BBBBBB", font_size= 12, pos_x = 865, pos_y = 775, size_x = 100, size_y = 45))
main_panel.add_element(HALE.PushButton(text="Valve Firing Sim",   text_color="black", bgcolor = "#BBBBBB", font_size= 12, pos_x = 820, pos_y = 845, size_x = 90, size_y = 45))


#left side, from top to bottom
main_panel.add_element(HALE.PushButton(text="Control Stop", text_color="red", bgcolor = "#BBBBBB", font_size= 24, pos_x = 10, pos_y = 100, size_x = 160, size_y = 60))
main_panel.add_element(HALE.PushButton(text="Cryo Fill",    text_color="black", bgcolor = "#BBBBBB", font_size= 12, pos_x = 100, pos_y = 260, size_x = 50, size_y = 250))
main_panel.add_element(HALE.PushButton(text="RECORD DATA",  text_color="black", bgcolor = "#DDDDDD", font_size= 10, pos_x = 190, pos_y = 200, size_x = 75, size_y = 40))

main_panel.add_element(HALE.ToggleButton(off_text="CAM\nNOGO",          on_text = "CAM\nGO", font_size= 12, pos_x = 175, pos_y = 275, size_x = 90, size_y = 50))
main_panel.add_element(HALE.ToggleButton(off_text="RECORD\nNOGO",       on_text = "RECORD\nGO", font_size= 12, pos_x = 175, pos_y = 335, size_x = 90, size_y = 50))
main_panel.add_element(HALE.ToggleButton(off_text="OFFICE\nNOGO",       on_text = "OFFICE\nGO", font_size= 12, pos_x = 175, pos_y = 395, size_x = 90, size_y = 50))
main_panel.add_element(HALE.ToggleButton(off_text="WATER SUPPLY\nNOGO", on_text = "WATER SUPPLY\nGO", font_size= 12, pos_x = 175, pos_y = 455, size_x = 90, size_y = 50))
main_panel.add_element(HALE.ToggleButton(off_text="IGNITER\nSAFE",      on_text = "IGNITER\nARMED", font_size= 12, pos_x = 175, pos_y = 515, size_x = 90, size_y = 50))

main_panel.add_element(HALE.ToggleButton(off_text="NANNY MODE OFF", on_text = "NANNY MODE ON", on_bgcolor="#679876", off_bgcolor = "#2B3E4F", font_size= 14, pos_x = 60, pos_y = 650, size_x = 140, size_y = 90))



#center
main_panel.add_element(HALE.Rectangle(color="#b3b3b3", z = HALE.Depths.BACKGROUND, pos_x = 270, pos_y = 180, size_x = 470, size_y = 640))

# resize_x and resize_y are absolute pixel dimensions, size_x and size_y are according to the 1000x1000 grid
main_panel.add_element(HALE.Image(file="./halegray.png", pos_x=(270+470/2)-(117/2), pos_y=190, resize_x=187, resize_y=87, size_x=117, size_y=109))


fuel_press = main_panel.add_element(HALE.ToggleButton(on_text="ABV-PR-120 (FUEL PRESS)", off_text="ABV-PR-120 (FUEL PRESS)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=334, pos_y=308, size_x=166, size_y=48))
fuel_vent  = main_panel.add_element(HALE.ToggleButton(on_text="ABV-FU-310 (FUEL VENT)",  off_text="ABV-FU-310 (FUEL VENT)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=334, pos_y=394, size_x=166, size_y=48, starting_state=enums.ToggleStates.ON))
fuel_iso   = main_panel.add_element(HALE.ToggleButton(on_text="ABV-FU-320 (FUEL ISO)",   off_text="ABV-FU-320 (FUEL ISO)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=334, pos_y=482, size_x=166, size_y=48))
fuel_purge = main_panel.add_element(HALE.ToggleButton(on_text="ABV-FU-330 (FUEL PURGE)", off_text="ABV-FU-330 (FUEL PURGE)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=334, pos_y=560, size_x=166, size_y=48))
fuel_main  = main_panel.add_element(HALE.ToggleButton(on_text="ABV-FU-340 (FUEL MAIN)",  off_text="ABV-FU-340 (FUEL MAIN)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=334, pos_y=641, size_x=166, size_y=48))

ox_press = main_panel.add_element(HALE.ToggleButton(on_text="ABV-PR-110 (OX PRESS)", off_text="ABV-PR-110 (OX PRESS)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=516, pos_y=308, size_x=166, size_y=48))
ox_vent  = main_panel.add_element(HALE.ToggleButton(on_text="ABV-OX-120 (OX VENT)",  off_text="ABV-OX-120 (OX VENT)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=516, pos_y=394, size_x=166, size_y=48, starting_state=enums.ToggleStates.ON))
ox_iso   = main_panel.add_element(HALE.ToggleButton(on_text="ABV-OX-120 (OX ISO)",   off_text="ABV-OX-120 (OX ISO)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=516, pos_y=482, size_x=166, size_y=48))
ox_chill = main_panel.add_element(HALE.ToggleButton(on_text="ABV-OX-120 (OX CHILL)", off_text="ABV-OX-120 (OX CHILL)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=516, pos_y=560, size_x=166, size_y=48))
ox_main  = main_panel.add_element(HALE.ToggleButton(on_text="ABV-OX-120 (OX MAIN)",  off_text="ABV-OX-120 (OX MAIN)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=516, pos_y=641, size_x=166, size_y=48))
ox_fill  = main_panel.add_element(HALE.ToggleButton(on_text="ABV-OX-120 (OX FILL)",  off_text="ABV-OX-120 (OX FILL)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=516, pos_y=724, size_x=166, size_y=48))

main_panel.add_element(HALE.ValveIndicator(state=enums.ToggleStates.OFF, get_data=fuel_press.get_state(), pos_x=280, pos_y=308, size_x=48, size_y=48, refresh_interval=500))
main_panel.add_element(HALE.ValveIndicator(state=enums.ToggleStates.ON,  get_data=fuel_vent.get_state(), pos_x=280, pos_y=394, size_x=48, size_y=48, refresh_interval=500))
main_panel.add_element(HALE.ValveIndicator(state=enums.ToggleStates.OFF, get_data=fuel_iso.get_state(), pos_x=280, pos_y=482, size_x=48, size_y=48, refresh_interval=500))
main_panel.add_element(HALE.ValveIndicator(state=enums.ToggleStates.OFF, get_data=fuel_purge.get_state(), pos_x=280, pos_y=560, size_x=48, size_y=48, refresh_interval=500))
main_panel.add_element(HALE.ValveIndicator(state=enums.ToggleStates.OFF, get_data=fuel_main.get_state(), pos_x=280, pos_y=641, size_x=48, size_y=48, refresh_interval=500))

main_panel.add_element(HALE.ValveIndicator(state=enums.ToggleStates.OFF, get_data=ox_press.get_state(), pos_x=686, pos_y=308, size_x=48, size_y=48, refresh_interval=500))
main_panel.add_element(HALE.ValveIndicator(state=enums.ToggleStates.ON,  get_data=ox_vent.get_state(), pos_x=686, pos_y=394, size_x=48, size_y=48, refresh_interval=500))
main_panel.add_element(HALE.ValveIndicator(state=enums.ToggleStates.OFF, get_data=ox_iso.get_state(), pos_x=686, pos_y=482, size_x=48, size_y=48, refresh_interval=500))
main_panel.add_element(HALE.ValveIndicator(state=enums.ToggleStates.OFF, get_data=ox_chill.get_state(), pos_x=686, pos_y=560, size_x=48, size_y=48, refresh_interval=500))
main_panel.add_element(HALE.ValveIndicator(state=enums.ToggleStates.OFF, get_data=ox_main.get_state(), pos_x=686, pos_y=641, size_x=48, size_y=48, refresh_interval=500))
main_panel.add_element(HALE.ValveIndicator(state=enums.ToggleStates.OFF, get_data=ox_fill.get_state(), pos_x=686, pos_y=723, size_x=48, size_y=48, refresh_interval=500))


#bottom
main_panel.add_element(HALE.PushButton(text="ABORT", text_color="white", bgcolor = "#5dc926", font_size= 48, pos_x = 315, pos_y = 840, size_x = 380, size_y = 150))


main_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#0e6e07", get_data = lambda : ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(1)], pos_x = 114, pos_y = 214, size_x = 22, size_y = 38, refresh_interval = 500))


#Adding dummy data to the charts on the engine panel so it looks nice, also to show how to update data

#Tank temps dummy data
x = np.linspace(0, 100, 50)
y = np.sin(2 * np.pi * x)
tank_temps.add_info(x, y, "#82e2ff", "TC-OX-220")
y = np.sin(2 * np.pi * x + .3)
tank_temps.add_info(x, y, "#53a0b8", "TC-OX-221")
y = np.sin(2 * np.pi * x + .6)
tank_temps.add_info(x, y, "#377e94", "TC-OX-222")
y = np.sin(2 * np.pi * x + .9)
tank_temps.add_info(x, y, "#185669", "TC-OX-223")

y = np.sin(2 * np.pi * x + 1.2)
tank_temps.add_info(x, y, "#fa3e3e", "TC-FU-320")
y = np.sin(2 * np.pi * x + 1.5)
tank_temps.add_info(x, y, "#bf3030", "TC-CC-410")
y = np.sin(2 * np.pi * x + 1.8)
tank_temps.add_info(x, y, "#8f1313", "TC-CC-411")
y = np.sin(2 * np.pi * x + 2.1)
tank_temps.add_info(x, y, "#690606", "TC-CC-412")

#Chamber pressures dummy data
y = np.sin(2 * np.pi * x) * 510
chamber_pressures.add_info(x, y, "#bf3030", "PT-CC-410")
y = np.sin(2 * np.pi * x + 1.3) * 510
chamber_pressures.add_info(x, y, "#8f1313", "PT-CC-420")

#Thrust-Pressure dummy data
y = np.sin(2 * np.pi * x) * 2150
thrust_pressure.add_info(x, y, "#bf3030", "Thrust")


get_data = lambda : ("#00FF00" if random.randint(0, 5) < 3 else "#FF0000" )

client.display()

#self.elements.append(pushbutton.PushButton(text="Bruh", anchor=enums.AnchorPoints.BOTTOMRIGHT, size_x = 600, size_y = 600, pos_x = 600, pos_y = 600))
#self.elements.append(togglebutton.ToggleButton( anchor=enums.AnchorPoints.BOTTOMLEFT, size_x = 600, size_y = 600, pos_x = 600, pos_y = 600))
         
#self.elements.append(rectangle.Rectangle(z = enums.Depths.FOREGROUND, color="#222222",  anchor=enums.AnchorPoints.CENTER, size_x = 100, size_y = 100, pos_x = 850, pos_y = 850, refresh_interval = 200))
#self.elements.append(indicatorlight.IndicatorLight(get_data = lambda : ("green" if random.randint(0, 5) < 3 else "red" ) ,   anchor=enums.AnchorPoints.CENTER, size_x = 200, size_y = 200, pos_x = 800, pos_y = 800, refresh_interval = 200))        
