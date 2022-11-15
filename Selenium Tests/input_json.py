import PySimpleGUI as sg
import json
import os
from os.path import exists as file_exists
file_exists('read.json')

def login(lg):
    sg.theme('DarkGrey15')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Provide login credentials for future use: ')],
              [sg.Text('Enter Username: ', size=(15, 1)), sg.InputText(lg[1])],
              [sg.Text('Enter Password: ', size=(15, 1)), sg.InputText(lg[2], password_char='*')],
              [sg.Text('URL of Page: ', size=(15, 1)), sg.InputText(lg[3])],
              [sg.Button('Ok'), sg.Button('Cancel')]],


    # Create the Window
    window = sg.Window('Eporner Importer', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        dic = {
            "login": [{
                'username': str(values[0]),
                'password': str(values[1]),
                'url': str(values[2])}]}

        # u = (str(values[0]))
        # p = (str(values[1]))
        # dic["username"] = {u}
        # dic["password"] = {p}
        json_object = json.dumps(dic, indent=4)

        with open('read.json', 'w') as f:
            json.dump(dic, f)
        f.close()
        window.close()
    return window


def closer(window):
    window.close()


def jhandler():
    # Opening JSON file
    if os.path.exists('read.json'):

        f = open('read.json')

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        # Iterating through the json
        # list
        for i in data["login"]:
            un = (str(i["username"]))
            pw = (str(i["password"]))
            ur = (str(i["url"]))
            lg = {1: un, 2: pw, 3: ur}
        # Closing file
        f.close()
    return lg
