import sqlite3
import os
 
def connect():
    """
    Connects to a local SQLite database and 
    creates a table if it doesn't exist.
    return: pointer to the database
    """
    db_name = "blocklist.db"
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS blocked(id INTEGER PRIMARY KEY)"
        )
    conn.commit()
    return conn

def add(conn, id):
    """
    Adds an entry to the local database.
    parameters: 
    conn -- pointer to database
    id -- id to be added to the table
    """
    c = conn.cursor()
    c.execute(
        f"""
        INSERT INTO blocked (id)
        VALUES ({id});
        """
        )
    conn.commit()
def retrieve(conn, id):
    """
    Checks if an id is in the local database.
    parameters: 
    conn -- pointer to database
    id -- id to be checked
    """
    c = conn.cursor()
    for entry in c.execute(f"SELECT id FROM blocked"):
        if entry[0] == id:
            return True
    return False
