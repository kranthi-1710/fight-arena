from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Fight Arena"}

class player(BaseModel):
    username : str
    character: str

players = []

@app.post("/players")
def create_player(player: player):
    players.append(player)
    return player

@app.get("/players")
def list_players():
    return players

