import random
# Indicator Panel


def random_bool():
    number = random.randint(0, 5)
    if number <= 2:
        return True
    else:
        return False


def ox_barchart():
    return 60 +  random.randint(0,5)

def fuel_barchart():
    return 50 +  random.randint(0,5)

def command_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def ox_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def fuel_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def ws_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def camera_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def office_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def record_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def igniter_go_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def nanny_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def sequence_flow_meter_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def cold_flow_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def abort_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def igniter_armed_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def startup_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

# also used in command panel
def ABV_WS_610_led():
    if (random_bool()):
        return "#0000FF"
    else:
        return "#FF0000"

def ABV_OX_210_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def ABV_OX_220_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def ABV_OX_230_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def ABV_OX_240_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def ABV_OX_250_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"


def ABV_PR_110_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def ABV_PR_120_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"


def ABV_FU_310_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def ABV_FU_320_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def ABV_FU_330_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def ABV_FU_340_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def MBV_FU_350_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"


# These are numeric displays

def PT_OX_210_numdisplay():
    return random.randint(0, 10000)/10

def PT_OX_211_numdisplay():
    return random.randint(0, 10000)/10

def PT_OX_220_numdisplay():
    return random.randint(0, 10000)/10

def PT_OX_230_numdisplay():
    return random.randint(0, 10000)/10

def PT_OX_240_numdisplay():
    return random.randint(0, 10000)/10


def PT_FU_310_numdisplay():
    return random.randint(0, 10000)/10

def PT_FU_311_numdisplay():
    return random.randint(0, 10000)/10

def PT_FU_320_numdisplay():
    return random.randint(0, 10000)/10

def PT_FU_330_numdisplay():
    return random.randint(0, 10000)/10


def PT_PR_110_numdisplay():
    return random.randint(0, 10000)/10

def PT_PR_120_numdisplay():
    return random.randint(0, 10000)/10

def PT_PR_130_numdisplay():
    return random.randint(0, 10000)/10

def PT_PR_140_numdisplay():
    return random.randint(0, 10000)/10



def TC_OX_210_numdisplay():
    return random.randint(0, 10000)/10

def TC_OX_220_numdisplay():
    return random.randint(0, 10000)/10

def TC_OX_221_numdisplay():
    return random.randint(0, 10000)/10

def TC_OX_222_numdisplay():
    return random.randint(0, 10000)/10

def TC_OX_223_numdisplay():
    return random.randint(0, 10000)/10

def TC_OX_230_numdisplay():
    return random.randint(0, 10000)/10

def TC_OX_240_numdisplay():
    return random.randint(0, 10000)/10

def TC_OX_250_numdisplay():
    return random.randint(0, 10000)/10


def TC_FU_310_numdisplay():
    return random.randint(0, 10000)/10

def TC_FU_320_numdisplay():
    return random.randint(0, 10000)/10

def TC_FU_330_numdisplay():
    return random.randint(0, 10000)/10


def TC_PR_110_numdisplay():
    return random.randint(0, 10000)/10



# Engine Panel
def fuel_main_valve_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def ox_main_valve_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def tank_temps_chart():
    return (random.randint(50, 100), random.randint(60, 100),random.randint(70, 75),random.randint(80, 90),random.randint(0, 30),random.randint(0, 40), random.randint(25, 30), random.randint(80, 83));

def chamber_pressures_chart():
    return (random.randint(100, 105), random.randint(200, 210))

def thrust_chart():
    return tuple([random.randint(100, 105)])



# Main Panel
def ignitor_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

# ABV_WS_610_led is defined with the indicator panel LEDs

def ABV_WS_620_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def igniter_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def flow_meter_installed_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def cryo_cold_flow_active_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

def cryo_fill_led():
    if (random_bool()):
        return "#00FF00"
    else:
        return "#FF0000"

# Valve indicators that currently read the state of the given toggle button.
# These can be uncommented and changed to read data from physical switches instead, 
# and then passed as arguments to the constructors in panel_init.py.

'''
def ox_press_indicator(z):
    return z.get_state()

def ox_vent_indicator(z):
    return z.get_state()

def ox_iso_indicator(z):
    return z.get_state()

def ox_chill_indicator(z):
    return z.get_state()

def ox_main_indicator(z):
    return z.get_state()

def ox_fill_indicator(z):
    return z.get_state()


def fuel_press_indicator(z):
    return z.get_state()

def fuel_vent_indicator(z):
    return z.get_state()

def fuel_iso_indicator(z):
    return z.get_state()

def fuel_purge_indicator(z):
    return z.get_state()

def fuel_main_indicator(z):
    return z.get_state()

'''