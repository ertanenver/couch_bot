import sqlite3

def delete_all(id:int):
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    cursor.execute('DELETE FROM Users WHERE id = "%s"' % (id))

    connection.commit()
    cursor.close()
    connection.close()



def delete_fio(id:int):
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    cursor.execute('DELETE fio FROM Users WHERE id = "%s"' % (id))

    connection.commit()
    cursor.close()
    connection.close()



def delete_phone_number(id:int):
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    cursor.execute('DELETE phone_number FROM Users WHERE id = "%s"' % (id))

    connection.commit()
    cursor.close()
    connection.close()