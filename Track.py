import sqlite3
import redis
import contextlib
import uuid

from typing import List
from pydantic import BaseModel, Field, BaseSettings
from fastapi import Depends, FastAPI, Request

class Settings(BaseSettings):
	database1: str
	database2: str
	database3: str
	databaseUser: str

	class Config:
		env_file = ".env"

class gameStart(BaseModel):
	userID: int
	gameID: int

class updateState(BaseModel):
    userID: int
    gameID: int
    guess: str
    numberGuesses: int

class restoreState(BaseModel):
    userID: int
    gameID: int
    wordsGuessed: str
    remainingGuesses: int

app = FastAPI(root_path="/api/v1")
settings = Settings()

def get_db():
    with contextlib.closing(sqlite3.connect(settings.database1)) as db:
        db.row_factory = sqlite3.Row
        yield db

def get_db2():
    with contextlib.closing(sqlite3.connect(settings.database2)) as db:
        db.row_factory = sqlite3.Row
        yield db

def get_db3():
    with contextlib.closing(sqlite3.connect(settings.database3)) as db:
        db.row_factory = sqlite3.Row
        yield db

def get_db_user():
    with contextlib.closing(sqlite3.connect(settings.databaseUser)) as db:
        db.row_factory = sqlite3.Row
        yield db

def calcShardNum(user, userDB):
	con = userDB

	try:
		fetch = con.execute("SELECT * FROM users WHERE user_id = ?", (user,))
	except:
		print("ERROR FETCHING")

	for row in fetch:
		num = int(uuid.UUID(row[2])) % 3

	con.close()
	return num

@app.get('game-start/{userID}/{gameID}')
def gameStart(dbUser: sqlite3.Connection = Depends(get_db_user), db1: sqlite3.Connection = Depends(get_db), db2: sqlite3.Connection = Depends(get_db2), db3: sqlite3.Connection = Depends(get_db3)):
    #Starting a new game. The client should supply a user ID and game ID
    #when a game starts. If the user has already played the game,
    #they should receive an error.

	sqlite3.register_converter('GUID', lambda b: uuid.UUID(bytes_le=b))
	sqlite3.register_adapter(uuid.UUID, lambda u: u.bytes_le)

	num = calcShardNum(userResults.userID, dbUser)
	shardSelection = None

	if(num == 0):
		shardSelection = db1
	elif(num == 1):
		shardSelection = db2
	elif(num == 2):
		shardSelection = db3

	print(num)
	con = shardSelection

	try:
		con.execute("SELECT userID, gameID FROM games where userID = ? OR gameID = ?", userID, gameID)
		gameStart = con.fetchone()

		if gameStart:
			print("You already played this game!")
		else:
			con.execute(
				"""
				INSERT INTO games(user_id, game_id)
				VALUES(?, ?, ?, ?, ?)
                """, (userResults.userID, userResults.gameID)
                )
			con.commit()
	except sqlite3.IntegrityError:
		print("ERROR POSTING")

	return {"Status": "Success!"}

@app.get('game-update/{userID}/{gameID}')
def gameUpdate():
    #Updating the state of a game. When a user makes a new guess for a game,
    #record the guess and update the number of guesses remaining.
    #If a user tries to guess more than six times, they should receive an error.

	#update guess row


@app.get('game-restore/{userID}/{gameID}')
def gameRestore():
    #Restoring the state of a game. Upon request, the user should be able to r
    #etrieve an object containing the current state of a game, including the
    #words guessed so far and the number of guesses remaining.
