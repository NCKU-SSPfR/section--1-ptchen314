import sqlite3
from contextlib import closing

def initialize():
    with closing(sqlite3.connect("game.db")) as conn:
        with closing(conn.cursor()) as cursor:
            # Create game_state table (with username column)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS game_state (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                current_level_name TEXT NOT NULL,
                map_size TEXT NOT NULL,
                health INTEGER NOT NULL,
                path TEXT NOT NULL,
                current_position TEXT NOT NULL
            )
            """)
            conn.commit()