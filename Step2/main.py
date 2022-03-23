import sqlite3
import flask


def get_from_db(sql):
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(sql).fetchall()

    return result


def search_by_years(year1, year2):  # поиск фильмов по диапазону лет
    respons = get_from_db(sql=f'''    
        SELECT title, release_year  
        from netflix
        WHERE release_year BETWEEN '{year1}' AND '{year2}'
        LIMIT 100
        ''')
    film_all = []
    for i in respons:
        film_all.append(dict(i))

    return film_all

