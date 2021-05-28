# Import Required Module
import tkinter as tk
from typing import Sized
import numpy as np
import random
import HALE
import input_handlers as gd
import output_handlers as oc

# This is the runnable portion of the code. Pretty much every individual line here is needed, as each line corresponds to something
# unique that's created and/or 

# This file should be the go-to file to add new things to the panel, to add additional panels, or to modify aspects of existing elements

# The interface/client is the term for the overall application in its entirety. In this case, it refers to the combination of panels
client = HALE.Interface()

# Adding the 3 panels to the application
main_panel = client.add_panel(HALE.Panel(size_x = 1600, size_y = 800))
engine_panel = client.add_panel(HALE.Panel(size_x = 1600, size_y = 800))
indicator_panel = client.add_panel(HALE.Panel(size_x = 1900, size_y = 950))


########## INDICATOR PANEL #########

# The following lines of code up until the next panel are adding elements to the indicator panel. 
# If you want to change something about the indicator panel elements you can change their value below


#top right
indicator_panel.add_element(HALE.Image(file="./IndicatorPanelBgNew.PNG", z=HALE.Depths.BACKGROUND, pos_x=0, pos_y=0, size_x=1000, size_y=1000))

indicator_panel.add_element(HALE.IndicatorLight(text="Command",             starting_color="#969696", font=("Arial", 8), get_data = gd.Command, pos_x=788, pos_y=45, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Ox",                  starting_color="#969696", font=("Arial", 8), get_data = gd.Ox, pos_x=788, pos_y=95, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Fuel",                starting_color="#969696", font=("Arial", 8), get_data = gd.Fuel, pos_x=788, pos_y=145, size_x = 55, size_y = 50, refresh_interval=1000))

indicator_panel.add_element(HALE.IndicatorLight(text="WS",                  starting_color="#969696", font=("Arial", 8), get_data = gd.WS, pos_x=829, pos_y=45, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Camera",              starting_color="#969696", font=("Arial", 8), get_data = gd.Camera, pos_x=829, pos_y=95, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Office",              starting_color="#969696", font=("Arial", 8), get_data = gd.Office, pos_x=829, pos_y=145, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Record",              starting_color="#969696", font=("Arial", 8), get_data = gd.Record, pos_x=829, pos_y=195, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Igniter GO",          starting_color="#969696", font=("Arial", 8), get_data = gd.IgniterGO, pos_x=829, pos_y=245, size_x = 55, size_y = 50, refresh_interval=1000))

indicator_panel.add_element(HALE.IndicatorLight(text="Nanny",               starting_color="#969696", font=("Arial", 8), get_data = gd.Nanny, pos_x=872, pos_y=45, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Sequence Flow Meter", starting_color="#969696", font=("Arial", 8), get_data = gd.SequenceFlowMeter, pos_x=872, pos_y=145, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Cold Flow",           starting_color="#969696", font=("Arial", 8), get_data = gd.ColdFlow, pos_x=872, pos_y=245, size_x = 55, size_y = 50, refresh_interval=1000))

indicator_panel.add_element(HALE.IndicatorLight(text="ABORT",               starting_color="#969696", font=("Arial", 8), get_data = gd.ABORT, pos_x=939, pos_y=45, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Igniter Armed",       starting_color="#969696", font=("Arial", 8), get_data = gd.IgniterArmed, pos_x=939, pos_y=145, size_x = 55, size_y = 50, refresh_interval=1000))
indicator_panel.add_element(HALE.IndicatorLight(text="Startup",             starting_color="#969696", font=("Arial", 8), get_data = gd.Startup, pos_x=939, pos_y=245, size_x = 55, size_y = 50, refresh_interval=1000))

#p&id
indicator_panel.add_element(HALE.IndicatorLight(text="ABV-WS-610", starting_color="#ff0000", get_data=gd.ABV_WS_SixTen, pos_x=65, pos_y=86, size_x = 87, size_y = 57, refresh_interval=3000)) # ABV-WS-610

indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#00da6d", get_data=gd.ABV_OX_TwoTen, pos_x=325, pos_y=148, size_x = 15, size_y = 23, refresh_interval=3000)) # ABV-OX-210
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#00da6d", get_data=gd.ABV_OX_TwoTwenty, pos_x=623, pos_y=436, size_x = 15, size_y = 23, refresh_interval=3000)) # ABV-OX-220
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#00da6d", get_data=gd.ABV_OX_TwoThirty, pos_x=695, pos_y=375, size_x = 15, size_y = 23, refresh_interval=3000)) # ABV-OX-230
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#00da6d", get_data=gd.ABV_OX_ThreeTwenty, pos_x=777, pos_y=578, size_x = 15, size_y = 23, refresh_interval=3000)) # ABV-OX-320
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#00da6d", get_data=gd.ABV_OX_TwoFifty, pos_x=487, pos_y=501, size_x = 15, size_y = 23, refresh_interval=3000)) # ABV-OX-250
                                                                                                               
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#00da6d", get_data=gd.ABV_PR_OneTen, pos_x=140, pos_y=342, size_x = 14, size_y = 24, refresh_interval=3000)) # ABV-PR-110
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#ff0000", get_data=gd.ABV_PR_OneTwenty, pos_x=139, pos_y=674, size_x = 14, size_y = 24, refresh_interval=3000)) # ABV-PR-120
                                                                                                               
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#00da6d", get_data=gd.ABV_FU_ThreeTen, pos_x=317, pos_y=858, size_x = 14, size_y = 23, refresh_interval=3000)) # ABV-FU-310
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#ff0000", get_data=gd.ABV_FU_ThreeTwenty, pos_x=619, pos_y=773, size_x = 14, size_y = 23, refresh_interval=3000)) # ABV-FU-320
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#ff0000", get_data=gd.ABV_FU_ThreeThirty, pos_x=786, pos_y=836, size_x = 14, size_y = 23, refresh_interval=3000)) # ABV-FU-330
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#ff0000", get_data=gd.ABV_FU_ThreeForty, pos_x=777, pos_y=719, size_x = 14, size_y = 23, refresh_interval=3000)) # ABV-FU-340
indicator_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#00da6d", get_data=gd.MBV_FU_ThreeFifty, pos_x=451, pos_y=846, size_x = 14, size_y = 23, refresh_interval=3000)) # MBV-FU-350

indicator_panel.add_element(HALE.NumericDisplay(text="PT-PR-140", font=("Arial", 9), get_data=gd.PT_PR_OneForty, pos_x=80, pos_y=160, size_x = 35, size_y = 45, refresh_interval=500)) 
indicator_panel.add_element(HALE.NumericDisplay(text="TC-OX-210", font=("Arial", 9), get_data=gd.TC_OX_TwoTen, pos_x=215, pos_y=140, size_x = 35, size_y = 45, refresh_interval=500)) 
indicator_panel.add_element(HALE.NumericDisplay(text="PT-OX-211", font=("Arial", 9), get_data=gd.PT_OX_TwoEleven, pos_x=270, pos_y=225, size_x = 35, size_y = 45, refresh_interval=500)) 

indicator_panel.add_element(HALE.NumericDisplay(text="TC-OX-220", font=("Arial", 9), get_data=gd.TC_OX_TwoTwenty, pos_x=430, pos_y=260, size_x = 35, size_y = 45, refresh_interval=500))
indicator_panel.add_element(HALE.NumericDisplay(text="TC-OX-221", font=("Arial", 9), get_data=gd.TC_OX_TwoTwentyOne, pos_x=430, pos_y=310, size_x = 35, size_y = 45, refresh_interval=500)) 
indicator_panel.add_element(HALE.NumericDisplay(text="TC-OX-222", font=("Arial", 9), get_data=gd.TC_OX_TwoTwentyTwo, pos_x=430, pos_y=360, size_x = 35, size_y = 45, refresh_interval=500)) 
indicator_panel.add_element(HALE.NumericDisplay(text="TC-OX-223", font=("Arial", 9), get_data=gd.TC_OX_TwoTwentyThree, pos_x=430, pos_y=410, size_x = 35, size_y = 45, refresh_interval=500)) 

indicator_panel.add_element(HALE.NumericDisplay(text="PT-PR-110", font=("Arial", 9), get_data=gd.PT_PR_OneTen, pos_x=30, pos_y=440, size_x = 35, size_y = 45, refresh_interval=500)) 
indicator_panel.add_element(HALE.NumericDisplay(text="PT-PR-130", font=("Arial", 9), get_data=gd.PT_PR_OneThirty, pos_x=175, pos_y=435, size_x = 35, size_y = 45, refresh_interval=500)) 
indicator_panel.add_element(HALE.NumericDisplay(text="PT-PR-120", font=("Arial", 9), get_data=gd.PT_PR_OneTwenty, pos_x=175, pos_y=575, size_x = 35, size_y = 45, refresh_interval=500)) 
indicator_panel.add_element(HALE.NumericDisplay(text="TC-PR-110", font=("Arial", 9), get_data=gd.TC_PR_OneTen, pos_x=75, pos_y=480, size_x = 35, size_y = 45, refresh_interval=500)) 

indicator_panel.add_element(HALE.NumericDisplay(text="PT-OX-210", font=("Arial", 9), get_data=gd.PT_OX_TwoTen, pos_x=350, pos_y=340, size_x = 35, size_y = 45, refresh_interval=500)) 
indicator_panel.add_element(HALE.NumericDisplay(text="PT-FU-310", font=("Arial", 9), get_data=gd.PT_FU_ThreeTen, pos_x=350, pos_y=650, size_x = 35, size_y = 45, refresh_interval=500)) 

indicator_panel.add_element(HALE.NumericDisplay(text="TC-FU-320", font=("Arial", 9), get_data=gd.TC_FU_ThreeTwenty, pos_x=430, pos_y=735, size_x = 35, size_y = 45, refresh_interval=500)) 

indicator_panel.add_element(HALE.NumericDisplay(text="TC-FU-310", font=("Arial", 9), get_data=gd.TC_FU_ThreeTen, pos_x=215, pos_y=730, size_x = 35, size_y = 45, refresh_interval=500)) 
indicator_panel.add_element(HALE.NumericDisplay(text="PT-FU-311", font=("Arial", 9), get_data=gd.PT_FU_ThreeEleven, pos_x=275, pos_y=790, size_x = 35, size_y = 45, refresh_interval=500)) 

indicator_panel.add_element(HALE.NumericDisplay(text="TC-FU-330", font=("Arial", 9), get_data=gd.TC_FU_ThreeThirty, pos_x=580, pos_y=770, size_x = 35, size_y = 45, refresh_interval=500)) 

indicator_panel.add_element(HALE.NumericDisplay(text="PT-OX-230", font=("Arial", 9), get_data=gd.PT_OX_TwoThirty, pos_x=675, pos_y=600, size_x = 35, size_y = 45, refresh_interval=500)) 
indicator_panel.add_element(HALE.NumericDisplay(text="PT-FU-230", font=("Arial", 9), get_data=gd.PT_FU_TwoThirty, pos_x=675, pos_y=650, size_x = 35, size_y = 45, refresh_interval=500)) 

indicator_panel.add_element(HALE.NumericDisplay(text="PT-OX-240", font=("Arial", 9), get_data=gd.PT_OX_TwoForty, pos_x=535, pos_y=550, size_x = 35, size_y = 45, refresh_interval=500)) 

indicator_panel.add_element(HALE.NumericDisplay(text="TC-OX-230", font=("Arial", 9), get_data=gd.TC_OX_TwoThirty, pos_x=580, pos_y=430, size_x = 35, size_y = 45, refresh_interval=500)) 
indicator_panel.add_element(HALE.NumericDisplay(text="TC-OX-240", font=("Arial", 9), get_data=gd.TC_OX_TwoForty, pos_x=650, pos_y=365, size_x = 35, size_y = 45, refresh_interval=500)) 
indicator_panel.add_element(HALE.NumericDisplay(text="TC-OX-250", font=("Arial", 9), get_data=gd.TC_OX_TwoFifty, pos_x=730, pos_y=295, size_x = 35, size_y = 45, refresh_interval=500)) 
indicator_panel.add_element(HALE.NumericDisplay(text="PT-OX-220", font=("Arial", 9), get_data=gd.PT_OX_TwoTwenty, pos_x=730, pos_y=470, size_x = 35, size_y = 45, refresh_interval=500)) 
indicator_panel.add_element(HALE.NumericDisplay(text="PT-FU-320", font=("Arial", 9), get_data=gd.PT_FU_ThreeTwenty, pos_x=730, pos_y=790, size_x = 35, size_y = 45, refresh_interval=500)) 

indicator_panel.add_element(HALE.BarChart(get_data=gd.BarChartOne, bgcolor = "#FFFFFF", barcolor = "#00FF00", pos_x=399, pos_y=281, size_x = 14, size_y = 127, refresh_interval=50)) 
indicator_panel.add_element(HALE.BarChart(get_data=gd.BarChartTwo, bgcolor = "#FFFFFF", barcolor = "#FF0000", pos_x=398, pos_y=621, size_x = 15, size_y = 128, refresh_interval=1000)) 


########## ENGINE PANEL ###########

# The following lines of code up until the next panel are adding elements to the engine panel. 
# If you want to change something about the engine panel elements you can change their value below

engine_panel.add_element(HALE.Image(file="./haleblack.png", pos_x=335, pos_y=50, size_x=291, size_y=269))

engine_panel.add_element(HALE.Image(file="./engine.png", pos_x=350, pos_y=320, size_x=246, size_y=180))


engine_panel.add_element(HALE.Chart(pos_x = 0, pos_y = 0, size_x = 300, size_y = 400, title="Tank Temps", xlabel="Time", ylabel="Amplitude", lines = [("TC-OX-220", "#FFFFFF"), ("TC-OX-221", "#FF00FF"), ("TC-OX-222", "#0000FF"), ("TC-OX-223", "#FF0000"), ("TC-FU-320", "#00FF00"), ("TC-CC-410", "#FFFF00"), ("TC-CC-411", "#00FFFF"), ("TC-CC-412", "#123456")], get_data = gd.TankTemps, refresh_interval = 4000))
engine_panel.add_element(HALE.Chart(pos_x = 650, pos_y = 0, size_x = 300, size_y = 400, title="Chamber Pressures", xlabel="Time", ylabel="Amplitude", lines = [("PT-CC-410", "#FFFFFF"), ("PT-CC-420", "#FF00FF")], get_data = gd.ChamberPressures, refresh_interval = 5000))
engine_panel.add_element(HALE.Chart(pos_x = 120, pos_y = 600, size_x = 700, size_y = 350, title="Pressures(psi) - Thrust (lbf)", xlabel="Time", ylabel="Thrust - Pressure", lines = [("Thrust", "#000000")], get_data = gd.Thrust , refresh_interval = 2000))

engine_panel.add_element(HALE.IndicatorLight(text="Ox Main Valve",   starting_color="#0e6e07", get_data = lambda : gd.OxMainValve(), pos_x = 20, pos_y = 640, size_x = 100, size_y = 50, refresh_interval = 50))
engine_panel.add_element(HALE.IndicatorLight(text="Fuel Main Valve", starting_color="#0e6e07", get_data = lambda : gd.FuelMainValve(), pos_x = 20, pos_y = 740, size_x = 100, size_y = 50, refresh_interval = 50))

########## MAIN PANEL ###########

# The following lines of code up until the next panel are adding elements to the main control panel. 
# If you want to change something about the main control panel elements you can change their value below

#logging box
log_box = main_panel.add_element(HALE.LoggingBox(pos_x = 0, pos_y = 800, size_x = 200, size_y = 100))


#top
main_panel.add_element(HALE.PushButton(onclick=oc.water_suppression, text="WATER SUPPRESSION", text_color="black", bgcolor = "#DDDDDD", font_size= 12, pos_x = 430, pos_y = 20, size_x = 140, size_y = 50))

main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.fuel_nogo_on   , on_toggleoff=oc.fuel_nogo_off  , off_text="FUEL NOGO",    on_text = "FUEL GO",    font_size= 16, pos_x = 270, pos_y = 110, size_x = 135, size_y = 60))
main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.command_nogo_on, on_toggleoff=oc.command_nogo_off, off_text="COMMAND NOGO", on_text = "COMMAND GO", font_size= 16, pos_x = 414, pos_y = 110, size_x = 183, size_y = 60))
main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.ox_nogo_on     , on_toggleoff=oc.ox_nogo_off     , off_text="OX NOGO",      on_text = "OX GO",      font_size= 16, pos_x = 606, pos_y = 110, size_x = 135, size_y = 60))

main_panel.add_element(HALE.IndicatorLight(text="ABV-WS-610 LED", starting_color="#0e6e07", get_data =  gd.ABV_WS_SixTen, pos_x = 600, pos_y = 30, size_x = 150, size_y = 50, refresh_interval = 50))


#right side, from top to bottom
main_panel.add_element(HALE.IndicatorLight(text="Igniter",        starting_color="#FF0000", get_data = gd.Igniter, pos_x = 815, pos_y = 30, size_x = 150, size_y = 50, refresh_interval = 500))
main_panel.add_element(HALE.IndicatorLight(text="ABV-WS-620 LED", starting_color="#0e6e07", get_data = gd.ABV_WS_SixTwenty, pos_x = 790, pos_y = 110, size_x = 150, size_y = 50, refresh_interval = 1000))

main_panel.add_element(HALE.PushButton(onclick=oc.go_away_fire, text="Go Away Fire (Please)", text_color="black", bgcolor = "#BBBBBB", font_size= 16, pos_x = 790, pos_y = 170, size_x = 140, size_y = 80))
main_panel.add_element(HALE.PushButton(onclick=oc.system_cycle, text="System Cycle OFF",      text_color="black", bgcolor = "#BBBBBB", font_size= 12, pos_x = 810, pos_y = 270, size_x = 100, size_y = 50))

main_panel.add_element(HALE.IndicatorLight(text="Flow Meter Installed",  starting_color="#0e6e07", get_data = gd.FlowMeterInstalled, pos_x = 750, pos_y = 340, size_x = 150, size_y = 50, refresh_interval = 250))
main_panel.add_element(HALE.IndicatorLight(text="Cryo Cold Flow Active", starting_color="#0e6e07", get_data = gd.CryoColdFlowActive, pos_x = 870, pos_y = 340, size_x = 150, size_y = 50, refresh_interval = 50))

main_panel.add_element(HALE.PushButton(onclick=oc.cold_flow, text="Cold Flow",             text_color="black",  bgcolor = "#BBBBBB", font_size= 12, pos_x = 800, pos_y = 400, size_x = 110, size_y = 60))
main_panel.add_element(HALE.PushButton(onclick=oc.engine_start_up, text="Engine Start Up", text_color="black", bgcolor = "#999999", font_size= 12, pos_x = 780, pos_y = 510, size_x = 160, size_y = 65))

main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.one_second_purge_on, on_toggleoff=oc.one_second_purge_off, off_text="1 Second Purge OFF",  on_text = "1 Second Purge ON", on_bgcolor="#AAAAAA", off_bgcolor = "#CCCCCC", on_text_color="#0022FF", off_text_color = "#010101", font_size= 10, pos_x = 765, pos_y = 590, size_x = 90, size_y = 50))
main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.two_second_purge_on, on_toggleoff=oc.two_second_purge_off, off_text="2 Second Purge OFF",  on_text = "2 Second Purge ON", on_bgcolor="#AAAAAA", off_bgcolor = "#CCCCCC", on_text_color="#0022FF", off_text_color = "#010101", font_size= 10, pos_x = 870, pos_y = 590, size_x = 90, size_y = 50))
main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.cycle_fuel_vent_on    , on_toggleoff=oc.cycle_fuel_vent_off , off_text="Cycle Fuel Vent OFF", on_text = "Cycle Fuel Vent ON", on_bgcolor="#AAAAAA", off_bgcolor = "#CCCCCC", on_text_color="#0022FF", off_text_color = "#010101", font_size= 10, pos_x = 765, pos_y = 690, size_x = 90, size_y = 50))
main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.cycle_ox_vent_on      , on_toggleoff=oc.cycle_ox_vent_off   , off_text="Cycle Ox Vent OFF",   on_text = "Cycle Ox Vent ON", on_bgcolor="#AAAAAA", off_bgcolor = "#CCCCCC", on_text_color="#0022FF", off_text_color = "#010101", font_size= 10, pos_x = 870, pos_y = 690, size_x = 90, size_y = 50))

main_panel.add_element(HALE.PushButton(onclick=oc.fuel_press_control, text="Fuel Press Control", text_color="black", bgcolor = "#BBBBBB", font_size= 12, pos_x = 755, pos_y = 775, size_x = 100, size_y = 45))
main_panel.add_element(HALE.PushButton(onclick=oc.ox_press_control,   text="Ox Press Control",   text_color="black", bgcolor = "#BBBBBB", font_size= 12, pos_x = 865, pos_y = 775, size_x = 100, size_y = 45))
main_panel.add_element(HALE.PushButton(onclick=oc.valve_firing_sim,   text="Valve Firing Sim",   text_color="black", bgcolor = "#BBBBBB", font_size= 12, pos_x = 820, pos_y = 845, size_x = 90, size_y = 45))


#left side, from top to bottom
main_panel.add_element(HALE.PushButton(onclick=oc.control_stop, text="Control Stop", text_color="red", bgcolor = "#BBBBBB", font_size= 24, pos_x = 10, pos_y = 100, size_x = 160, size_y = 60))

main_panel.add_element(HALE.IndicatorLight(text=None, starting_color="#0e6e07", get_data = gd.CryoFill, pos_x = 114, pos_y = 214, size_x = 22, size_y = 38, refresh_interval = 500))

main_panel.add_element(HALE.PushButton(onclick=oc.cryo_fill,   text="Cryo Fill",    text_color="black", bgcolor = "#BBBBBB", font_size= 12, pos_x = 100, pos_y = 260, size_x = 50, size_y = 250))
main_panel.add_element(HALE.PushButton(onclick=oc.record_data, text="RECORD DATA",  text_color="black", bgcolor = "#DDDDDD", font_size= 10, pos_x = 190, pos_y = 200, size_x = 75, size_y = 40))

main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.cam_nogo_on         , on_toggleoff=oc.cam_nogo_off        , off_text="CAM\nNOGO",          on_text = "CAM\nGO", font_size= 12, pos_x = 175, pos_y = 275, size_x = 90, size_y = 50))
main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.record_nogo_on      , on_toggleoff=oc.record_nogo_off      , off_text="RECORD\nNOGO",       on_text = "RECORD\nGO", font_size= 12, pos_x = 175, pos_y = 335, size_x = 90, size_y = 50))
main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.office_nogo_on      , on_toggleoff=oc.office_nogo_off      , off_text="OFFICE\nNOGO",       on_text = "OFFICE\nGO", font_size= 12, pos_x = 175, pos_y = 395, size_x = 90, size_y = 50))
main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.water_supply_nogo_on, on_toggleoff=oc.water_supply_nogo_off, off_text="WATER SUPPLY\nNOGO", on_text = "WATER SUPPLY\nGO", font_size= 12, pos_x = 175, pos_y = 455, size_x = 90, size_y = 50))
main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.igniter_safe_true   , on_toggleoff=oc.igniter_safe_false  , off_text="IGNITER\nSAFE",      on_text = "IGNITER\nARMED", font_size= 12, pos_x = 175, pos_y = 515, size_x = 90, size_y = 50))

main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.nanny_mode_on       , on_toggleoff=oc.nanny_mode_off       , off_text="NANNY MODE OFF", on_text = "NANNY MODE ON", on_bgcolor="#679876", off_bgcolor = "#2B3E4F", font_size= 14, pos_x = 60, pos_y = 650, size_x = 140, size_y = 90))



#center
main_panel.add_element(HALE.Rectangle(color="#b3b3b3", z = HALE.Depths.BACKGROUND, pos_x = 270, pos_y = 180, size_x = 470, size_y = 640))

main_panel.add_element(HALE.Image(file="./halegray.png", pos_x=445, pos_y=190, size_x=117, size_y=109))


fuel_press = main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.fuel_press_on, on_toggleoff=oc.fuel_press_off, on_text="ABV-PR-120 (FUEL PRESS)", off_text="ABV-PR-120 (FUEL PRESS)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=334, pos_y=308, size_x=166, size_y=48))
fuel_vent  = main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.fuel_vent_on, on_toggleoff=oc.fuel_vent_off, on_text="ABV-FU-310 (FUEL VENT)",  off_text="ABV-FU-310 (FUEL VENT)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=334, pos_y=394, size_x=166, size_y=48, starting_state=HALE.ToggleStates.ON))
fuel_iso   = main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.fuel_iso_on, on_toggleoff=oc.fuel_iso_off, on_text="ABV-FU-320 (FUEL ISO)",   off_text="ABV-FU-320 (FUEL ISO)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=334, pos_y=482, size_x=166, size_y=48))
fuel_purge = main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.fuel_purge_on, on_toggleoff=oc.fuel_purge_off, on_text="ABV-FU-330 (FUEL PURGE)", off_text="ABV-FU-330 (FUEL PURGE)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=334, pos_y=560, size_x=166, size_y=48))
fuel_main  = main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.fuel_main_on, on_toggleoff=oc.fuel_main_off, on_text="ABV-FU-340 (FUEL MAIN)",  off_text="ABV-FU-340 (FUEL MAIN)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=334, pos_y=641, size_x=166, size_y=48))

ox_press = main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.ox_press_on, on_toggleoff=oc.ox_press_off, on_text="ABV-PR-110 (OX PRESS)", off_text="ABV-PR-110 (OX PRESS)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=516, pos_y=308, size_x=166, size_y=48))
ox_vent  = main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.ox_vent_on, on_toggleoff=oc.ox_vent_off, on_text="ABV-OX-120 (OX VENT)",  off_text="ABV-OX-120 (OX VENT)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=516, pos_y=394, size_x=166, size_y=48, starting_state=HALE.ToggleStates.ON))
ox_iso   = main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.ox_iso_on, on_toggleoff=oc.ox_iso_off, on_text="ABV-OX-120 (OX ISO)",   off_text="ABV-OX-120 (OX ISO)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=516, pos_y=482, size_x=166, size_y=48))
ox_chill = main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.ox_chill_on, on_toggleoff=oc.ox_chill_off, on_text="ABV-OX-120 (OX CHILL)", off_text="ABV-OX-120 (OX CHILL)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=516, pos_y=560, size_x=166, size_y=48))
ox_main  = main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.ox_main_on, on_toggleoff=oc.ox_main_off, on_text="ABV-OX-120 (OX MAIN)",  off_text="ABV-OX-120 (OX MAIN)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=516, pos_y=641, size_x=166, size_y=48))
ox_fill  = main_panel.add_element(HALE.ToggleButton(on_toggleon=oc.ox_fill_on, on_toggleoff=oc.ox_fill_off, on_text="ABV-OX-120 (OX FILL)",  off_text="ABV-OX-120 (OX FILL)", on_bgcolor="#464646", off_bgcolor="#464646", font_size=12, pos_x=516, pos_y=724, size_x=166, size_y=48))

main_panel.add_element(HALE.ValveIndicator(state=HALE.ToggleStates.OFF, get_data=fuel_press.get_state, pos_x=280, pos_y=308, size_x=48, size_y=48, refresh_interval=50))
main_panel.add_element(HALE.ValveIndicator(state=HALE.ToggleStates.ON,  get_data=fuel_vent.get_state, pos_x=280, pos_y=394, size_x=48, size_y=48, refresh_interval=50))
main_panel.add_element(HALE.ValveIndicator(state=HALE.ToggleStates.OFF, get_data=fuel_iso.get_state, pos_x=280, pos_y=482, size_x=48, size_y=48, refresh_interval=50))
main_panel.add_element(HALE.ValveIndicator(state=HALE.ToggleStates.OFF, get_data=fuel_purge.get_state, pos_x=280, pos_y=560, size_x=48, size_y=48, refresh_interval=50))
main_panel.add_element(HALE.ValveIndicator(state=HALE.ToggleStates.OFF, get_data=fuel_main.get_state, pos_x=280, pos_y=641, size_x=48, size_y=48, refresh_interval=50))

main_panel.add_element(HALE.ValveIndicator(state=HALE.ToggleStates.OFF, get_data=ox_press.get_state, pos_x=686, pos_y=308, size_x=48, size_y=48, refresh_interval=50))
main_panel.add_element(HALE.ValveIndicator(state=HALE.ToggleStates.ON,  get_data=ox_vent.get_state, pos_x=686, pos_y=394, size_x=48, size_y=48, refresh_interval=50))
main_panel.add_element(HALE.ValveIndicator(state=HALE.ToggleStates.OFF, get_data=ox_iso.get_state, pos_x=686, pos_y=482, size_x=48, size_y=48, refresh_interval=50))
main_panel.add_element(HALE.ValveIndicator(state=HALE.ToggleStates.OFF, get_data=ox_chill.get_state, pos_x=686, pos_y=560, size_x=48, size_y=48, refresh_interval=50))
main_panel.add_element(HALE.ValveIndicator(state=HALE.ToggleStates.OFF, get_data=ox_main.get_state, pos_x=686, pos_y=641, size_x=48, size_y=48, refresh_interval=50))
main_panel.add_element(HALE.ValveIndicator(state=HALE.ToggleStates.OFF, get_data=ox_fill.get_state, pos_x=686, pos_y=723, size_x=48, size_y=48, refresh_interval=50))


#bottom
main_panel.add_element(HALE.PushButton(text="ABORT", onclick = lambda: log_box.add_message("Aborted!"), text_color="white", bgcolor = "#5dc926", font_size= 48, pos_x = 315, pos_y = 840, size_x = 380, size_y = 150))





# This function tells the application to start running and displaying stuff
client.display()

