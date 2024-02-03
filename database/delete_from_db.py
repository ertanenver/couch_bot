import sqlite3

def delete_all(id:int):
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    cursor.execute('DELETE * FROM Users WHERE id = "%s"' % (id))
    result = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()

    return result