import sqlite3

def insert_id(id:int):
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()
    #if cursor.execute('SELECT * FROM couch_bot WHERE id = ("%s")' % (id)):
    cursor.execute('INSERT INTO Users (id) VALUES ("%s")' % (id))

    connection.commit()
    cursor.close()
    connection.close()



def insert_fio(id:int, fio:str):
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    cursor.execute('UPDATE Users SET fio = "%s" WHERE id = "%s"' % (fio, id))

    connection.commit()
    cursor.close()
    connection.close()



def insert_phone_number(id:int, phone_number:str):
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    cursor.execute('UPDATE Users SET phone_number = "%s" WHERE id = "%s"' % (phone_number, id))

    connection.commit()
    cursor.close()
    connection.close()



def insert_work_place(id:int, work_place:str):
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    cursor.execute('UPDATE Users SET work_place = "%s" WHERE id = "%s"' % (work_place, id))

    connection.commit()
    cursor.close()
    connection.close()



def insert_feature(id:int, feature:str):
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    cursor.execute('UPDATE Users SET feature = "%s" WHERE id = "%s"' % (feature, id))

    connection.commit()
    cursor.close()
    connection.close()




