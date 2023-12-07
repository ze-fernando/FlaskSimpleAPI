import psycopg2
from flask import jsonify, request
from ..config.ConfigDb import ConfigDB as db

connect = psycopg2.connect(host=db.POSTGRES_HOST, database=db.POSTGRES_DATABASE, 
                           user=db.POSTGRES_USER, password=db.POSTGRES_PASSWORD)

cursor = connect.cursor()

sql = """CREATE TABLE IF NOT EXISTS animes (
        ID SERIAL PRIMARY KEY,
        NAME VARCHAR(100), 
        ASSISTIDO BOOLEAN NOT NULL
        );"""


cursor.execute(sql)


def get():
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


def getById(id:int):
    cursor.execute(f'SELECT * FROM animes WHERE ID = {id}')
    animeById = cursor.fetchall()
    animeJson = list()
    for anime in animeById:
        animeJson.append(
            {
                "id": anime[0],
                "name": anime[1],
                "assistido": anime[2]
            }
        )
    return animeJson


def create():
    newAnime = request.json
    cursor.execute(f"INSERT INTO animes (name, assistido) VALUES ('{newAnime['name']}','{newAnime['assistido']}')")
    connect.commit()

    return newAnime


def delete(id:int):
    cursor.execute(f"DELETE FROM animes WHERE ID = {id}")            
    connect.commit()

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


def put(id:int, body:dict):
    cursor.execute(f"UPDATE animes SET NAME='{body['name']}', ASSISTIDO='{body['assistido']}' WHERE ID = {id}")
    connect.commit()

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
