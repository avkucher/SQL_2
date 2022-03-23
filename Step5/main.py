import sqlite3
import flask


def get_from_db(sql):
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(sql).fetchall()

    return result


def search_by_name(name1, name2):  # поиск актеров
    response = get_from_db(sql=f'''    
        SELECT * 
        from netflix
        WHERE "cast" LIKE '%{name1}%' and "cast" LIKE '%{name2}%'
        ''')
    names = []
    result = []
    for i in response:
        c = dict(i).get('cast').split(', ')
        for k in c:
            names.append(k)

    b = [name1, name2]
    names = set(names) - set(b)

    for name in names:
        k =0
        for i in response:
            if name in dict(i).get('cast'):
                    k+=1

            if k>2:
                result.append(name)



    return result

if __name__ == '__main__':
    print(search_by_name("Jack Black", "Dustin Hoffman"))


