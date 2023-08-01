from flask import Flask, jsonify, request

app = Flask(__name__)

animes = [
    {
        "id": 1,
        "name": "Boku no hero",
    },
    {
        "id": 2,
        "name": "Bersek",
    },
    {
        "id": 3,
        "name": "Naruto",
    },
    {
        "id": 4,
        "name": "Attack on Titan",
    },
    {
        "id": 5,
        "name": "Fire Force",
    },
    {
        "id": 6,
        "name": "Hajime no Ippo",
    },
    {
        "id": 7,
        "name": "Baki Hanma",
    },
    {
        "id": 8,
        "name": "Ashita no joe",
    },
    {
        "id": 9,
        "name": "Bleach",
    }

]


@app.get("/animes/")
def getAll():
    return jsonify(animes)



@app.get("/animes/<int:id>")
def getById(id:id): 
    for anime in animes:
        if anime.get('id') == id:
            return jsonify(anime)


@app.post("/animes/")
def createAnime():
    newAnime = request.json
    animes.append(newAnime)

    return jsonify(animes)


@app.delete("/animes/<int:id>")
def deleteById(id:int):
    for i,anime in enumerate(animes):
        if anime.get('id') == id:
            del animes[i]
    
    return jsonify(animes)


@app.put("/animes/<int:id>")
def editAnime(id:int):
    updatedAnime = request.json
    for i,anime in enumerate(animes):
        if anime.get('id') == id:
            animes[i].update(updatedAnime)

    return jsonify(animes)
    


app.run(debug=True)