import sqlite3
import flask


def get_from_db(sql):
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(sql).fetchall()

    return result


def search_by_rating(rating):  # поиск фильмов по рейтингу

    if rating == 'children':
        response = get_from_db(sql=f'''    
            SELECT title, rating, description  
            from netflix
            WHERE rating = 'G'
            LIMIT 100
        ''')
        film_all = []
        for i in response:
            film_all.append(dict(i))
    elif rating == 'family':
        response = get_from_db(sql=f'''    
            SELECT title, rating, description  
            from netflix
            WHERE rating = 'G' or rating = 'PG' or rating = 'PG-13'
            LIMIT 100
            ''')
        film_all = []
        for i in response:
            film_all.append(dict(i))
    elif rating == 'adult':
        response = get_from_db(sql=f'''    
            SELECT title, rating, description  
            from netflix
            WHERE rating = 'R' or rating = 'NC-17'
            LIMIT 100
            ''')
        film_all = []
        for i in response:
            film_all.append(dict(i))

    return film_all

