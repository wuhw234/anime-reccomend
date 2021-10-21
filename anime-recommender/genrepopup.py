import PySimpleGUI as sg

def getGenre():
    """
    Creates GUI that allows users to select the 
    desired genre
    return: returns a number representing the genre or
    None if the user exits
    """
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

    w_layout = [
        [
        sg.Text("Choose the genre:", font="impact 15", justification="center")
        ],
        [
        sg.Button("Anything",size=(9, 2)),
        sg.Button("Action", size=(9, 2)), 
        sg.Button("Romance", size=(9, 2)),
        ],
        [
        sg.Button("Adventure", size=(9, 2)), 
        sg.Button("Slice of Life", size=(9, 2)), 
        sg.Button("Comedy", size=(9, 2))
        ],
        [
        sg.Button("Drama", size=(9, 2)), 
        sg.Button("Mystery", size=(9, 2)), 
        sg.Button("Sci-Fi", size=(9, 2))
        ],
        [
        sg.Button("Fantasy", size=(9, 2)), 
        sg.Button("Supernatural", size=(9, 2)), 
        sg.Button("Sports", size=(9, 2)),
        ],
    ]

    window = sg.Window(title="Mood", layout=w_layout, margins=(200, 100))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            return None
        else:
            window.close()
            return genres[event]
