# from PIL import Image
# import requests
# from io import BytesIO

# response = requests.get(url)
# img = Image.open(BytesIO(response.content))

import PySimpleGUI as sg

def showAnime(response):

    index = 0
    file_list_column = [
        [
            sg.Text(response["results"][index]["title"], 
            font='Courier 20', justification="center", key = "title" )
        ],
        [
            sg.Text("Rating: " + str(response["results"][0]["score"]), 
            font='Courier 15', key = "score"),
            sg.Text(str(response["results"][index]["episodes"]) + " episodes", 
            font='Courier 15', key = "episodes")
        ],
        [
            sg.Text(response["results"][index]["synopsis"], 
            size=(80, 20), font='Courier 13', key = "description")
        ],
    ]

    button_column = [
        [sg.Button("Already Watched/Block",size=(11, 3))],
        [sg.Button("Next", size=(11, 3))],
        [sg.Button("I'll watch this!", size=(11, 3))]
    ]

    w_layout = [
        [
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(button_column),
        ]
    ]

    window = sg.Window(title="Anime Reccomender", layout=w_layout)

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