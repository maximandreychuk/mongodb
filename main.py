from pymongo import MongoClient
import pprint

# cоздаем клиента бд
client = MongoClient("mongodb://localhost:27017/")

# подключаемся к бд
db = client.shop

# подключаемся к коллекции бд
collection = db.series

# pprint.pprint(collection.find_one())
qt_mov = collection.find_one({"director": "director"})
print(qt_mov)
# for director in collection.find().pretty():
#    print(director)
# pprint.pprint(current_collection.find_all())
