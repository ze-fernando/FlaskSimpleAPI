from flask import Flask, jsonify, request, Blueprint
from ..services.services import *

route = Blueprint('routes', __name__)


@route.get("/animes")
def getAll():
    res = get()
    
    return jsonify(res)



@route.get("/animes/<int:id>")
def getOne(id:id): 
   res = getById(id)
   
   return jsonify(res)


@route.post("/animes")
def createAnime():
    res = create()

    return jsonify(message="Successfully registered anime", dados=res)


@route.delete("/animes/<int:id>")
def deleteById(id:int):
    res = delete(id)
    
    return jsonify(message="Successfully deleted anime", dados=res)


@route.put("/animes/<int:id>")
def editAnime(id:int):
    body = request.json
    res = put(id, body)
    return jsonify(message="Successfully updated anime", dados=res)
