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



@app.get('game-start/{userID}/{gameID}'):
def gameStart(user: userID, game: gameID):
    #Starting a new game. The client should supply a user ID and game ID
    #when a game starts. If the user has already played the game,
    #they should receive an error.


@app.get('game-update/{userID}/{gameID}')
def gameUpdate():
    #Updating the state of a game. When a user makes a new guess for a game,
    #record the guess and update the number of guesses remaining.
    #If a user tries to guess more than six times, they should receive an error.

@app.get('game-restore/{userID}/{gameID}'):
def gameRestore():
    #Restoring the state of a game. Upon request, the user should be able to r
    #etrieve an object containing the current state of a game, including the
    #words guessed so far and the number of guesses remaining.
