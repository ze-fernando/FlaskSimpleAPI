from flask import Flask, jsonify, request
from flask_pydantic_spec import FlaskPydanticSpec
import psycopg2

POSTGRES_URL="postgres://default:x0iJr8jFOVcE@ep-late-poetry-27723165-pooler.us-east-1.postgres.vercel-storage.com:5432/verceldb"
POSTGRES_PRISMA_URL="postgres://default:x0iJr8jFOVcE@ep-late-poetry-27723165-pooler.us-east-1.postgres.vercel-storage.com:5432/verceldb?pgbouncer=true&connect_timeout=15"
POSTGRES_URL_NON_POOLING="postgres://default:x0iJr8jFOVcE@ep-late-poetry-27723165.us-east-1.postgres.vercel-storage.com:5432/verceldb"
POSTGRES_USER="default"
POSTGRES_HOST="ep-late-poetry-27723165-pooler.us-east-1.postgres.vercel-storage.com"
POSTGRES_PASSWORD="x0iJr8jFOVcE"
POSTGRES_DATABASE="verceldb"

connect = psycopg2.connect(host=POSTGRES_HOST, database=POSTGRES_DATABASE, 
                           user=POSTGRES_USER, password=POSTGRES_PASSWORD)

cursor = connect.cursor()

app = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='CRUD API')
spec.register(app)

sql = """CREATE TABLE IF NOT EXISTS animes (
        ID SERIAL PRIMARY KEY,
        NAME VARCHAR(100), 
        ASSISTIDO BOOLEAN NOT NULL
        );"""


cursor.execute(sql)


@app.get("/animes/")
def getAll():
    """Get all data in database"""
    cursor.execute('SELECT * FROM animes')
    allAnimes = cursor.fetchall()
    animeJson = list()
    for anime in allAnimes:
        animeJson.append(
            {
                "id": anime[0],
                "name": anime[1],
                "assistido": anime[2]
            }
        )
    return jsonify(animeJson)



@app.get("/animes/<int:id>")
def getById(id:id): 
    """Get data for id"""
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
    return jsonify(animeJson)


@app.post("/animes/")
def createAnime():
    """Create new data in database"""
    newAnime = request.json
    cursor.execute(f"INSERT INTO animes (name, assistido) VALUES ('{newAnime['name']}','{newAnime['assistido']}')")
    connect.commit()

    return jsonify(message="Successfully registered anime", dados=newAnime)


@app.delete("/animes/<int:id>")
def deleteById(id:int):
    """Delete data for id"""
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
    return jsonify(message="Successfully deleted anime", dados=animeJson)


@app.put("/animes/<int:id>")
def editAnime(id:int):
    """Edit data in database"""
    updatedAnime = request.json
    cursor.execute(f"UPDATE animes SET NAME='{updatedAnime['name']}', ASSISTIDO='{updatedAnime['assistido']}' WHERE ID = {id}")
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
    return jsonify(message="Successfully updated anime", dados=animeJson)
