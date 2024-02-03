import sqlite3
import re

def is_login(id:int):
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Users WHERE id = "%s"' % (id))
    result = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()

    return result



def is_ok_fio(id:int):
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Users WHERE id = "%s"' % (id))
    result = cursor.fetchall()
    print(result)
    if is_login(id):
        pattern = r'^[а-яА-Я]+\s[а-яА-Я]+\s[а-яА-Я]+$'
        match = re.match(pattern, result[0][1])
        if match:
            result = True
        else:
            result = False
    else:
        result = False 

    connection.commit()
    cursor.close()
    connection.close()

    return result


def get_feature(id:int):
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    cursor.execute('SELECT feature FROM Users WHERE id = "%s"' % (id))
    result = cursor.fetchall()
    if result == '[]':
        result = "None"
    else:
        result = str(result[0][0])

    connection.commit()
    cursor.close()
    connection.close()

    return result


def get_feature_list():
    string = ''
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    cursor.execute('SELECT feature FROM Users')
    result = [row[0] for row in cursor.fetchall()]

    connection.commit()
    cursor.close()
    connection.close()

    for index, value in enumerate(result, start=1):

        if value == None:
            value = "Не выбрано"
            
        string += f"Пользователь {index} - {value}\n"

    return string



def count_users():
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    cursor.execute('SELECT COUNT(id) FROM Users')
    result = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()

    return result[0][0]



def get_permission(id:int):
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    cursor.execute('SELECT permission FROM Users')
    result = cursor.fetchall()
    if result == '[]':
        result = "None"
    else:
        result = str(result[0][0])

    connection.commit()
    cursor.close()
    connection.close()

    return result



def get_permission_list():
    connection = sqlite3.connect('couch_bot.db')

    cursor = connection.cursor()

    cursor.execute('SELECT id, permission FROM Users WHERE permission = "super_user"')
    result = [row[0] for row in cursor.fetchall()]

    connection.commit()
    cursor.close()
    connection.close()

    return result
