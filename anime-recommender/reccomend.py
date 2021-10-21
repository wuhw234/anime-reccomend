import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import HorizontalSeparator
from database import add
from getAnime import getAnime

def showAnime(results, conn, genre, page):
    """
    Creates GUI that shows anime with buttons that
    allow the user to navigate and block.
    parameters: 
    results -- array of anime shows parsed from JSON
    conn -- pointer to database
    genre -- the selected genre
    page -- which page of results the data is retrieved from
    return: True to exit out of GUI, False to go back to genre
    selection
    """
    index = 0
    file_list_column = [
        [
            sg.Text(results[index]["title"], 
            font='Courier 20', justification="center", key = "title" )
        ],
        [
            sg.Text("Rating: " + str(results[0]["score"]), 
            font='Courier 15', key = "score"),
            sg.Text(str(results[index]["episodes"]) + " episodes", 
            font='Courier 15', key = "episodes")
        ],
        [
            sg.Text(results[index]["synopsis"], 
            size=(80, 20), font='Courier 13', key = "description")
        ],
    ]

    button_column = [
        [sg.Button("Already Watched/Block",size=(11, 3))],
        [sg.Button("Next", size=(11, 3))],
        [sg.Button("Previous", size=(11, 3))],
        [sg.Button("I'll watch this!", size=(11, 3))],
        [sg.HorizontalSeparator()],
        [sg.Button("Go Back", size=(11, 3))]
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
    page = 1
    while True:
        event, values = window.read()
        if event == "I'll watch this!" or event == sg.WIN_CLOSED:
            window.close()
            return True
        elif event == "Go Back":
            window.close()
            return False
        elif event == "Already Watched/Block":
            add(conn, results[index]["mal_id"])
            results = [result for result in results if result["mal_id"] != results[index]["mal_id"]]
            if index >= len(results):
                page += 1
                index = 0
                results = getAnime(genre, conn, page)
                if len(results) == 0:
                    return True
        elif event == "Previous":
            if index - 1 < 0:
                if page-1 > 0:
                    page -= 1
                    results = getAnime(genre, conn, page)
                    index = len(results) - 1
            else:
                index -= 1
        elif event == "Next":          
            index += 1
            if index >= len(results):
                page += 1
                index = 0
                results = getAnime(genre, conn, page)
                if len(results) == 0:
                    return True
        window["title"].update(results[index]["title"])
        window["score"].update("Rating: " + str(results[index]["score"]))
        window["description"].update(results[index]["synopsis"])
        window["episodes"].update(str(results[index]["episodes"]) + " episodes")
        #add to blocked list
        # if event == "Already Watched/Block":
                
        
    window.close()