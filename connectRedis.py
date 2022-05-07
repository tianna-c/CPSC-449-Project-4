#connect db shards to Redis
import redis
import sqlite3

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)
conn = sqlite3.connect('shard_1.db')
cur = conn.cursor()
cur.execute("SELECT * FROM games")
allGames = cur.fetchall()
stats = {}
games = "Games"

for row in allGames:
	#r.zadd("games", {"user_id": row[0]}, {"game_id": row[1]}, {"finished": row[2]}, {"guesses": row[3]}, {"won": row[4]})
	user_id = row[0]
	game_id = row[1]
	finished = row[2]
	guesses = row[3]
	won = row[4]
	redisClient.zadd(games, user_id, "user_id", game_id, "game_id")
	redisClient.zadd(games, finished, "finished", guesses, "guesses", won, "won")
	#r.zadd("games", row[0], row[1], row[2], row[3], row[4])
	#r.getall("games")
print("Success!")
	

conn = sqlite3.connect('shard_2.db')
cur = conn.cursor()
cur.execute("SELECT * FROM games")

try:
	for row in cur.fetchall():
		#r.zadd("games", row) #returns (nil)
		#r.zadd("games", {"user_id": row[0]}, {"game_id": row[1]}, {"finished": row[2]}, {"guesses": row[3]}, {"won": row[4]})
		r.getall("games")
except:
	print("Done!")

conn = sqlite3.connect('shard_3.db')
cur = conn.cursor()
cur.execute("SELECT * FROM games")

try:
	for row in cur.fetchall():
		#r.zadd("games", row) #returns (nil)
		#r.zadd("games", {"user_id": row[0]}, {"game_id": row[1]}, {"finished": row[2]}, {"guesses": row[3]}, {"won": row[4]})
		r.getall("games")
except:
	print("Done!")

conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute("SELECT * FROM users")

try: 
	for row in cur.fetchall():
		#r.zadd("users", row) #returns (nil)
		#r.zadd("users", {"user_id": row[0]}, {"usename": row[1]}, {"uuid": row[2]})
		r.getall("users")
except:
	print("Done!")

cur.close()
conn.close()
