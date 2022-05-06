#connect db shards to Redis
import redis
import sqlite3

#redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)

def get_top10StreaksRecordsFromShard1():
    con = sqlite3.connect('shard_1.db')
    cur = con.execute("SELECT user_id,streak FROM streaks ORDER BY streak DESC LIMIT 10")
    rows = cur.fetchall()
    dicts = {}
    print(rows)
    for row in rows:
        dicts[row[0]]= row[1]
    return dicts

def get_top10StreaksRecordsFromShard2():
    con = sqlite3.connect('shard_2.db')
    cur = con.execute("SELECT user_id,streak FROM streaks ORDER BY streak DESC LIMIT 10")
    rows = cur.fetchall()
    dicts = {}
    print(rows)
    for row in rows:
        dicts[row[0]]= row[1]
    return dicts

def get_top10StreaksRecordsFromShard3():
    con = sqlite3.connect('shard_3.db')
    cur = con.execute("SELECT user_id,streak FROM streaks ORDER BY streak DESC LIMIT 10")
    rows = cur.fetchall()
    dicts = {}
    print(rows)
    for row in rows:
        dicts[row[0]]= row[1]
    return dicts
