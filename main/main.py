from flask import Flask, jsonify, request
from Animes import animes

app = Flask(__name__)




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