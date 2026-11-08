from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from security import hash_password
from security import verify_password

from database import engine, Base, SessionLocal
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class PlayerCreate(BaseModel):
    username: str
    character: str
    password: str


class PlayerOut(BaseModel):
    id: int
    username: str
    character: str
    rating: int
    model_config = {"from_attributes": True}


class PlayerLogin(BaseModel):
    username: str
    password: str


@app.get("/")
def home():
    return {"message": "Welcome to the Fight Arena"}


@app.post("/players", response_model=PlayerOut)
def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Player).filter(
        models.Player.username == player.username
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already taken")

    new_player = models.Player(
        username=player.username, character=player.character, hashed_password=hash_password(player.password)
    )
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player


@app.get("/players", response_model=list[PlayerOut])
def list_players(db: Session = Depends(get_db)):
    return db.query(models.Player).all()


@app.post("/login")
def login(credentials: PlayerLogin, db: Session = Depends(get_db)):
    player = db.query(models.Player).filter(
        models.Player.username == credentials.username
    ).first()

    if not player or not verify_password(credentials.password, player.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"message": f"Welcome, {player.username}!"}