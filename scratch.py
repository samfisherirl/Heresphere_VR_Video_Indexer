import PySimpleGUI as sg
import json


def login():
    sg.theme('DarkGrey15')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Provide login credentials for future use: ')],
              [sg.Text('Enter Username: '), sg.InputText()],
              [sg.Text('Enter Password: '), sg.InputText()],
              [sg.Button('Ok'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Eporner Importer', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        dic = {'username': values[0], 'password': values[1]}

        tit = f'login [' + str(dic) + ']'
        # u = (str(values[0]))
        # p = (str(values[1]))
        # dic["username"] = {u}
        # dic["password"] = {p}
        json_object = json.dumps(tit, indent=4)

        with open('read.json', 'w') as f:
            json.dump(tit, f)
        f.close()
        window.close()
    return window

def closer(window):
    window.close()


win = login()

closer(win)
