import sqlite3

def insert_init_data_db(id:int,fio:str,phone_number:str):
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM couch_bot'
    cursor.execute('INSERT INTO couch_bot (id, fio, phone_number) VALUES ("%s","%s","%s")' % (id,fio,phone_number))

    connection.commit()
    cursor.close()
    connection.close()



def insert_feature_db(id:int, feature:str):
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    cursor.execute('UPDATE couch_bot SET feature = "%s" WHERE id = "%s"' % (feature, id))

    connection.commit()
    cursor.close()
    connection.close()