import pymongo
import json

conn = pymongo.MongoClient('mongodb://despean:des5300pean@ds155727.mlab.com:55727/music_scraping')
db = conn.music_scraping
data = json.load(open('music.json'))
coll = db['music']
if __name__ == '__main__':
    coll.insert_many(data)
    print('done')