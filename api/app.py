from flask import Flask, jsonify, request
from flask_pydantic_spec import FlaskPydanticSpec
from src.services.services import *

app = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='CRUD API')
spec.register(app)


@app.get("/animes")
def getAll():
    res = get()
    
    return jsonify(res)



@app.get("/animes/<int:id>")
def getOne(id:id): 
   res = getById()
   
   return jsonify(res)


@app.post("/animes")
def createAnime():
    res = create()

    return jsonify(message="Successfully registered anime", dados=res)


@app.delete("/animes/<int:id>")
def deleteById(id:int):
    res = delete(id)
    
    return jsonify(message="Successfully deleted anime", dados=res)


@app.put("/animes/<int:id>")
def editAnime(id:int):
    body = request.json
    res = put(id, body)
    return jsonify(message="Successfully updated anime", dados=res)


if __name__ == "__main__":
    app.run(debug = True)