import PySimpleGUI as sg

sg.theme('DarkAmber')  # No gray windows please!

# STEP 1 define the layout
layout = [
            [sg.Text('This is a very basic PySimpleGUI layout')],
            [sg.Input()],
            [sg.Button('Button'), sg.Button('Abort')]
         ]

#STEP 2 - create the window
window = sg.Window('Control Panel', layout, grab_anywhere=True)

# STEP3 - the event loop
while True:
    event, values = window.read()   # Read the event that happened and the values dictionary
    print(event, values)

    #The person closed the interface or clicked the abort button
    if event == sg.WIN_CLOSED or event == 'Abort':     # If user closed window with X or if user clicked "Exit" button then exit
        #Add stuff to cancel the launch
        break

    if event == 'Button':
      print('You pressed the button')
window.close()