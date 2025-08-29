import sqlite3

conn = sqlite3.connect("data/mydatabase.db")
cursor = conn.cursor()


def add_to_user(user_id, is_bot, first_name, last_name, username, is_premium):
    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id, is_bot, first_name, last_name, username, is_premium) VALUES (?, ?, ?, ?, ?, ?)",
        (user_id, is_bot, first_name, last_name, username, is_premium),
    )
    conn.commit()


def get_user_by_id(user_id):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    return cursor.fetchone()


def add_to_music(user_id, title, fileid_or_url, is_file_id, url_id):
    # Проверяем, существует ли пользователь
    if not get_user_by_id(user_id):
        print(f"Ошибка: пользователь с user_id {user_id} не найден!")
        return

    cursor.execute(
        "INSERT INTO music (user_id, title, fileid_or_url, is_file_id, url_id) VALUES (?, ?, ?, ?, ?)",
        (user_id, title, fileid_or_url, is_file_id, url_id),
    )
    conn.commit()
    print(f"Музыка '{title}' добавлена для пользователя {user_id}.")


def get_music_by_url_id(url_id):
    url_id = url_id[1]
    cursor.execute("SELECT * FROM music WHERE url_id = ?", (url_id,))
    return cursor.fetchone()
