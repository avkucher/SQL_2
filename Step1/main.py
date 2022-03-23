import sqlite3
import flask


def get_from_db(sql):
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(sql).fetchall()

    return result


def get_dict():  # поиск фильма по году
    for i in get_from_db(sql='''    
        SELECT *
        from netflix
        ORDER BY date_added DESC LIMIT 1'''):
        dict_all = dict(i)
    return dict_all


def search_by_title(title):  # поиск фильма по году
    for i in get_from_db(sql=f'''    
    SELECT *
    from netflix
    where title = '{title}'
    '''):

        return dict(i)


def get_dict_end():  # Получаем словарь с определенными полями фильма
    dict_old = get_dict()
    dict_end = {}
    for key, value in dict_old.items():
        if key == 'title' or key == "release_year" or key == "genre" or key == "listed_in" or key == "description":
            i = {key: value}
            dict_end.update(i)
        elif key == 'country':
            i = {key: value}
            dict_end.update(i)
    return (dict_end)



