import sqlite3

conn = sqlite3.connect("mydatabase.db")  # подключаемся к базе
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")  # включаем проверку внешних ключей

# теперь создаём таблицы
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        is_bot INTEGER,
        first_name TEXT,
        last_name TEXT,
        username TEXT UNIQUE,
        is_premium INTEGER
    )
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS music (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT,
        file_id TEXT,
        url_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
"""
)

conn.commit()
conn.close()
