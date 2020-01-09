from mysql.connector import connect
import keys


# Wrapper for connection to MySql server and initialization cursor
def wrapper(function):
    def connector(*args, **kwargs):
        cnx = connect(user=keys.sql_user,
                      password=keys.sql_password,
                      host=keys.sql_host,
                      database=keys.sql_database)
        cnx.connect()
        cursor = cnx.cursor()
        sql = function(*args, **kwargs)
        cursor.execute(sql)
        cnx.commit()
        cursor.close()
        cnx.close()

    return connector


@wrapper
def add_new(user_id, name, background='#FFFF66', text='#000001'):  # Adding new user
    return ("INSERT INTO users(user_id, name, background, text) VALUES({0}, '{1}', '{2}', '{3}')".format(user_id, name,
                                                                                                         background,
                                                                                                         text))


@wrapper
def background_color(user_id, background):  # Changing background color
    return ("UPDATE `users` SET `background` = '{1}' WHERE `users`.`user_id` = {0}; ".format(user_id, background))


@wrapper
def text_color(user_id, text):  # Changing text color
    return ("UPDATE `users` SET `text` = '{1}' WHERE `users`.`user_id` = {0}; ".format(user_id, text))


def query(user_id):  # Just Query
    cnx = connect(user=keys.sql_user,
                  password=keys.sql_password,
                  host='localhost',
                  database='textimage')
    cnx.connect()
    cursor = cnx.cursor()
    sql = ("SELECT text, background FROM `users` WHERE user_id = {};".format(user_id))
    cursor.execute(sql)
    for i, j in cursor:
        t_color, b_color = i, j
    cursor.close()
    cnx.close()
    return t_color, b_color
