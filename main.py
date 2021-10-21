import requests
from genrepopup import getGenre
from reccomend import showAnime

def getAnime(genre, page):
    #check if page 1 returns everything on page 1, check page 2
    query_params = {"order_by": "score", "genre": genre,"page": page}
    response = requests.get("https://api.jikan.moe/v3/search/anime", params=query_params).json()

    return response 

def main():
    genre = getGenre()
    if genre != None:
        page = 1
        while True:
            response = getAnime(genre, page)
            if showAnime(response):
                page += 1
            else:
                break

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