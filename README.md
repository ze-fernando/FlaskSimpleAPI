# Crud API

## About
Simple api crud, where you can add your anime and if you already watched it or not
make with Flask e ProstgreSQL


## Endpoints
GET [*localhost:5000/animes*](localhost:5000/animes)

return
```json
[
    {
    "assistido": true,
    "id": 4,
    "name": "Boku no hero"
  },
  {
    "assistido": true,
    "id": 5,
    "name": "Jujutsu Kaizen"
  },
  {
    "assistido": false,
    "id": 2,
    "name": "Hajime no ippo"
  },
  {
    "assistido": false,
    "id": 7,
    "name": "Death Note"
  }
]
```
GET [*localhost:5000/animes/2*](localhost:5000/animes)

return
```json
  {
    "assistido": false,
    "id": 2,
    "name": "Hajime no ippo"
  }
```
POST [*localhost:5000/animes*](localhost:5000/animes)

send
```json
  {
    "assistido": true,
    "name": "Naruto"
  }
```
return
```json
{
  "dados": {
    "assistido": true,
    "name": "Naruto"
  },
  "message": "Successfully registered anime"
}
```
PUT [*localhost:5000/animes/8*](localhost:5000/animes)

send
```json
  {
    "assistido": false,
    "name": "Naruto"
  }
```

return all animes

DELETE [*localhost:5000/animes/8*](localhost:5000/animes)

return
```json
{
  "message": "Successfully deleted anime"
}
```