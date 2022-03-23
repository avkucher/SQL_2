import sqlite3
import flask


def get_from_db(sql):
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(sql).fetchall()

    return result


def search_by_genre(listed_in):  # поиск 10 свежих фильмов по жанру
    respons = get_from_db(sql=f'''    
        SELECT title, description  
        from netflix
        WHERE listed_in ='{listed_in}'
        ORDER BY date_added DESC LIMIT 10
        ''')
    film_all = []
    for i in respons:
        film_all.append(dict(i))

    return film_all

