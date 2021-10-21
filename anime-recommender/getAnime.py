import requests
from database import retrieve

def getAnime(genre, conn, page):
    """
    Retrieves JSON data through the Jikan API.
    parameters: 
    conn -- pointer to database
    genre -- the selected genre
    page -- which page of results the data is retrieved from
    return: the 'results' key of the retrieved JSON data
    """
    while True:
        query_params = {"order_by": "score", "genre": genre,"page": page}
        response = requests.get("https://api.jikan.moe/v3/search/anime", params=query_params).json()
        results = [anime for anime in response["results"] if not retrieve(conn, anime["mal_id"])]
        if len(results) > 0:
            return results
        else:
            page += 1
