import sqlite3
import flask


def get_from_db(sql):
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(sql).fetchall()

    return result


def search_by_complex(type, release_year, listed_in):  # поиск по типу, году, жанру
    response = get_from_db(sql=f'''    
        SELECT title, description  
        from netflix
        WHERE "type" = "{type}" and "release_year" = "{release_year}" and "listed_in" LIKE '%{listed_in}%'
        ''')
    film_all = []
    for i in response:
        film_all.append(dict(i))

    return film_all

if __name__ == '__main__':
    print(search_by_complex("Movie", "1997", "Dramas"))


