import input_json
import json
# RUN INPUT BOX GRAB JASON SEND TO SELENIUM

window = input_json.login()
input_json.closer(window)


def jhandler():
    # Opening JSON file
    f = open('read.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    for i in data["login"]:
        print(str(i))

    # Closing file
    f.close()

jhandler()