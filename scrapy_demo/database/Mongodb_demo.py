import pymongo

client = pymongo.MongoClient(host="127.0.0.1",port=27017)
db = client.foobar
collection = db.books
#插入
# collection.insert_one({"book_id":2,"name":"R"})
# collection.insert({"book_id":3,"name":"C"})
# collection.insert({"book_id":1,"name":"java"})

# collection.insert_many([{"book_id":333,"name":"C#"},{"book_id":33,"name":"C++"}])
# 查找
# cursor = collection.find()
# for document in cursor:
#     print(document)
# print("="*30)
#
# result = collection.find_one()
# print(result)
# print("="*30)
#
# cursor = collection.find({"book_id":1})
# for document in cursor:
#     print(document)

# update_many  update_one
# collection.update({"book_id":1},{"$set":{"name":"php"}})
collection.update_many({"book_id":1},{"$set":{"name":"php"}})

# delete_one delete_many
