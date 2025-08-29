import sqlite3


def create_tables():
    conn = sqlite3.connect("data/mydatabase.db")  # подключаемся к базе
    cursor = conn.cursor()

    # включаем проверку внешних ключей
    cursor.execute("PRAGMA foreign_keys = ON;")

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
            fileid_or_url TEXT,
            is_file_id INTEGER,
            url_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """
    )

    conn.commit()
    conn.close()
