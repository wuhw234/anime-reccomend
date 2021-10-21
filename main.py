import requests
from genrepopup import getGenre
from reccomend import showAnime
from database import connect, add, retrieve

"""
TODO:
add case for when you run out of anime (optional-ish)
add sqlite database for storing watched/blocked anime
"""


def getAnime(genre, page):
    query_params = {"order_by": "score", "genre": genre,"page": page}
    response = requests.get("https://api.jikan.moe/v3/search/anime", params=query_params).json()
    return response 
    

def main():
    conn = connect()
    print(type(conn))
    genre = getGenre()
    if genre != None:
        page = 1
        while True:
            response = getAnime(genre, page)
            if showAnime(response, conn):
                page += 1
            else:
                break
    conn.close()

if __name__ == "__main__":
    main()

"""
Ask user for their current mood (action, romance, fantasy, drama, etc)
Users can choose don't show again/already watched,
show me later, or select show.
Store watched/blocked shows in a set??? or some type of
local json object?
Use basic gui
"""