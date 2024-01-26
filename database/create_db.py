import sqlite3



def create_db():
    # Создаем подключение к базе данных (файл my_database.db будет создан)
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    # Создаем таблицу Users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    fio TEXT UNIQUE,
    permission TEXT,
    work_place TEXT,
    phone_number TEXT,
    login_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    feature TEXT
    )
    ''')
    connection.commit()
    cursor.close()
    connection.close()

