# from PIL import Image
# import requests
# from io import BytesIO

# response = requests.get(url)
# img = Image.open(BytesIO(response.content))

import PySimpleGUI as sg
import os.path

# First the window layout in 2 columns
def showAnime(response):

    index = 0
    file_list_column = [
        [
            sg.Text(response["results"][index]["title"], key = "title")
        ],
        [
            sg.Text("Rating: " + str(response["results"][0]["score"]), key = "score"),
            sg.Text(str(response["results"][index]["episodes"]) + " episodes", key = "episodes")
        ],
        [
            sg.Text(response["results"][index]["synopsis"], size=(50, 20), key = "description")
        ],
    ]

    # For now will only show the name of the file that was chosen
    button_column = [
        [sg.Button("Already Watched/Block")],
        [sg.Button("Next")],
        [sg.Button("I'll watch this!")]
    ]

    # ----- Full layout -----
    w_layout = [
        [
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(button_column),
        ]
    ]

    window = sg.Window(title="Anime Reccomender", layout=w_layout, margins=(100, 30))

    # Run the Event Loop
    while True:
        event, values = window.read()

        if event == "I'll watch this!" or event == sg.WIN_CLOSED:
            break
        else:
            index += 1
            if index >= len(response["results"]):
                window.close()
                return True
            window["title"].update(response["results"][index]["title"])
            window["score"].update("Rating: " + str(response["results"][index]["score"]))
            window["description"].update(response["results"][index]["synopsis"])
            window["episodes"].update(str(response["results"][index]["episodes"]) + " episodes")
            #add to blocked list
            # if event == "Already Watched/Block":
                
        
    window.close()