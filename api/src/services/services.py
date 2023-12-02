import psycopg2
from flask import jsonify, request
from src.config.ConfigDb import ConfigDB as db

connect = psycopg2.connect(host=db.POSTGRES_HOST, database=db.POSTGRES_DATABASE, 
                           user=db.POSTGRES_USER, password=db.POSTGRES_PASSWORD)

cursor = connect.cursor()

sql = """CREATE TABLE IF NOT EXISTS animes (
        ID SERIAL PRIMARY KEY,
        NAME VARCHAR(100), 
        ASSISTIDO BOOLEAN NOT NULL
        );"""


cursor.execute(sql)


def allAnimes():
    cursor.execute('SELECT * FROM animes')
    animes = cursor.fetchall()
    animeJson = list()
    for anime in animes:
        animeJson.append(
            {
                "id": anime[0],
                "name": anime[1],
                "assistido": anime[2]
            }
        )
    return animeJson