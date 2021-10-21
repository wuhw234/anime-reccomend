from genrepopup import getGenre
from reccomend import showAnime
from database import connect
from getAnime import getAnime
    
"""
When run, this scripts opens a GUI that recommends
anime shows based on the selected genre.
"""
def main():
    conn = connect()
    while True:
        genre = getGenre()
        if genre != None:
            results = getAnime(genre, conn, 1)
            if showAnime(results, conn, genre, 1):
                break
        else:
            break
    conn.close()

if __name__ == "__main__":
    main()
