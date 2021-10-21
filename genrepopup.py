import PySimpleGUI as sg

def getGenre():
    genres = {
        "Anything": "",
        "Action": 1,
        "Adventure": 2,
        "Comedy": 4,
        "Mystery": 7,
        "Drama": 8,
        "Fantasy": 10,
        "Romance": 22,
        "Sci-Fi": 24,
        "Sports": 30,
        "Slice of Life": 36,
        "Supernatural": 37, 
    }
# For now will only show the name of the file that was chosen
    buttons = [
        [sg.Button("Anything"),],
        [
        sg.Button("Fantasy"),
        sg.Button("Action"),
        sg.Button("Romance"),
        ],
        [
        sg.Button("Adventure"),
        sg.Button("Slice of Life"),
        sg.Button("Comedy")
        ],
        [
        sg.Button("Drama"),
        sg.Button("Mystery"),
        sg.Button("Sci-Fi")
        ],
        [
        sg.Button("Supernatural"),
        sg.Button("Sports"),
        ],
    ]

    # ----- Full layout -----
    w_layout = [buttons]

    window = sg.Window(title="Mood", layout=w_layout, margins=(200, 100))

    # Run the Event Loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            return None
        else:
            window.close()
            return genres[event]
