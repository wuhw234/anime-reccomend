import sqlite3
import os
 
def connect():
    db_name = "blocklist.db"
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS blocked(id INTEGER PRIMARY KEY)"
        )
    conn.commit()
    return conn

def add(conn, id):
    c = conn.cursor()
    c.execute(
        f"""
        INSERT INTO blocked (id)
        VALUES ({id});
        """
        )
    conn.commit()
def retrieve(conn, id):
    c = conn.cursor()
    for entry in c.execute(f"SELECT id FROM blocked"):
        if entry[0] == id:
            return True
    return False
