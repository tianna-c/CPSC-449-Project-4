#connect db shards to Redis
import redis
import sqlite3

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)

r = redis.Redis()
conn = sqlite3.connect('shard_1.db')
cur = conn.cursor()
cur.execute("SELECT * FROM games")
allGames = cur.fetchall()

try:
	for row in allGames:
		#r.zadd("games", row) #returns (nil)
		#r.zadd("games", {"user_id": row[0]}, {"game_id": row[1]}, {"finished": row[2]}, {"guesses": row[3]}, {"won": row[4]})
		print("User ID: ", row[0])
		print("Game ID: ", row[1])
		print("Finished: ", row[2])
		print("Guesses: ", row[3])
		print("Won: ", row[4])
		print("\n")
		#r.zadd("games", row[0], row[1], row[2], row[3], row[4])
		#r.getall("games")
except:
	print("Done!")

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

conn = sqlite3.connect('userShard.db')
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
