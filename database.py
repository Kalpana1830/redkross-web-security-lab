
import sqlite3


def create_database():
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            role TEXT NOT NULL
        )
        """
    )
    connection.executemany(
        "INSERT INTO users (username, role) VALUES (?, ?)",
        [
            ("alice", "user"),
            ("bob", "admin"),
        ],
    )
    return connection


def find_user(connection, username):
    # Parameterized SQL keeps user input separate from SQL syntax.
    return connection.execute(
        "SELECT id, username, role FROM users WHERE username = ?",
        (username,),
    ).fetchall()
