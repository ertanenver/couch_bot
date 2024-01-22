import sqlite3

# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect('couch_bot.db')

cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
fio TEXT NOT NULL PRIMARY KEY,
permission TEXT NOT NULL,
work_place TEXT NOT NULL,
phone_number TEXT NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

connection.close()