import os

import pymysql
import pymysql.cursors
import dotenv

TABLE_NAME = 'costumers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, idade) '
            'VALUES (%s, %s) '
        )
        data1 = ('Richard', 17)
        result = cursor.execute(sql, data1)

        # print(sql, data1)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, idade) '
            'VALUES (%(nome)s, %(idade)s) '
        )
        data2 = {
            "nome": "Denise", "idade": 41
        }
        result = cursor.execute(sql, data2)  # type:ignore

        # print(sql, data2)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, idade) '
            'VALUES'
            '(%(nome)s, %(idade)s) '
        )
        data3 = (
            {"nome": "Vida", "idade": 10, },
            {"nome": "Raiane", "idade": 10, },
            {"nome": "Marisa", "idade": 42, },
            {"nome": "Aurora", "idade": 48, },
        )
        result = cursor.executemany(sql, data3)  # type:ignore

        # print(sql, data3)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, idade) '
            'VALUES'
            '(%s, %s) '
        )
        data4 = (
            ("Eder", 50, ),
            ("Lorena", 90, ),
        )
        result = cursor.executemany(sql, data4)  # type:ignore

        # print(sql, data4)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        # menor_id = int(input('digite o menor ID: '))
        # maior_id = int(input('digite o maior ID: '))

        menor_id = 0
        maior_id = 10
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s'
        )
        cursor.execute(sql, (menor_id, maior_id))
        # print(cursor.mogrify(sql, (menor_id, maior_id)))
        data5 = cursor.fetchall()

        for row in data5:
            ...
            # print(row)

    with connection.cursor() as cursor:

        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = 4'
        )
        cursor.execute(sql)
        connection.commit()
        cursor.execute(f'SELECT * FROM {TABLE_NAME}')

        # for row in cursor.fetchall():

        #     print(row)

    with connection.cursor() as cursor:

        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET name = %s, idade=%s '
            'WHERE id = %s '
        )
        cursor.execute(sql, ('Raiane', 29, 2))

        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME}')

        # for row in cursor.fetchall():
        #     _id, name, age = row
        #     print(_id, name, age)

        data6 = cursor.fetchall()

        for row in data6:
            print(row)
        connection.commit()
