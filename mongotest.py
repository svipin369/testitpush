import pymongo
client = pymongo.MongoClient("mongodb+srv://svipin369:hacker11march@cluster0.psw29lq.mongodb.net/?retryWrites=true&w=majority")
db=client.test
print(db)

d= {
    "name" : "sudhanshu",
    "email": "sudhanshu@ineuron.ai",
    "surname": "kumar"
    "place" : "bangaluru"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)