#add
#delete
#prices, user, item name, image array
import pymongo
import json
import textdistance as td
from bson import ObjectId
from bson.json_util import dumps
from pymongo import MongoClient
from flask import Flask, request, jsonify
from flask_cors import CORS

#Create instance of Flask App
app = Flask(__name__)
CORS(app)

#Connects to Mongo Database
connection_url = 'mongodb+srv://ruteam:ruscrew@cluster0.bvss2.mongodb.net/marketplace?retryWrites=true&w=majority'
client = pymongo.MongoClient(connection_url)

def removeduplicate(it):
    seen = []
    for x in it:
        if x not in seen:
            yield x
            seen.append(x)
    return seen

#clean up and standardize
def textFormat(text):
    newtext = ""
    for a in text:
        if a.isalpha() == True or a.isspace() == True:
            newtext+=a
    newtext.lower()
    newtext = list(newtext.split(" "))
    #print(newtext)
    return newtext
    
#Search items in database - basic search
@app.route('/search', methods=['GET'])
def search():
    db = client['marketplace']
    items = db['items']
    items.create_index([('tags', 1)])
    items.create_index([('title', 1)])
    items.create_index([('description', 1)])
    search_info = request.get_json()
    search_items = []
    
    search_term = search_info['search_term'].lower()
    search_t = textFormat(search_term)
    #match terms in tags,title and description
    for tags in search_t:
        search_tags = items.find({'tags': {'$elemMatch': { '$eq' : tags } } })
        search_items.extend(list(search_tags))
    
    search_title = items.find({'title': {'$regex': ".*" + search_term + ".*"  } })
    search_desc = items.find({'description': {'$regex': ".*" + search_term + ".*" } })
    
     
    search_items.extend(list(search_title))
    search_items.extend(list(search_desc))
    #string similarity- leveshtein algorithm for scanning title and description
    for query in items.find():
        try:
            desc = query["description"]
            title = query["title"]
            
            title_t = textFormat(title)
            desc_t = textFormat(desc)
            
            flag = 0
            for input_1 in search_t:
                for input_2 in title_t:
                    #print(td.levenshtein.normalized_similarity(input_1, input_2))
                    if td.levenshtein.normalized_similarity(input_1, input_2) > .5:
                        search_items.append(query)
                        print(query)
                        flag = 1
                    if flag == 1:
                        break
                if flag == 1:
                    break
                
                for input_3 in desc_t:
                    #print(td.levenshtein.normalized_similarity(input_1, input_3))
                    if td.levenshtein.normalized_similarity(input_1, input_3) > .5:
                        search_items.append(query)
                        flag = 1
                        break
                    if flag == 1:
                        break
                if flag == 1:
                    break
        except:
            pass
    jsondata = dumps(search_items)
    jsonlist = json.loads(jsondata)
    #remove duplicate objects
    jsons = { repr(each): each for each in jsonlist }.values()

    return dumps(jsons)

#Deletes Item from items database
@app.route('/deleteItem', methods=['POST'])
def delete_item():
    db = client['marketplace']
    items = db['items']
    del_item = request.get_json()
    my_query = {"_id": ObjectId(del_item['_id'])}
    item = items.find(my_query)
    for x in item:
        items.delete_one(x)
    return "success"

#Adds Item to items database
@app.route('/addItem', methods=['POST'])
def add_item():
    db = client['marketplace']
    items = db['items']
    new_item = request.get_json()
    items.insert_one(new_item)
    return "success"

#Adds new user to database
@app.route('/addUser', methods=['POST'])
def add_user():
    db = client['marketplace']
    users = db['users']
    new_user = request.get_json()
    for document in users.find({}, projection={"_id": False}):
        if document["netid"] == new_user['netid']:
            return json.dumps({"msg": "exists"})
    users.insert_one(new_user)
    return json.dumps({"msg": "created"})

#Checks login credentials
@app.route('/login', methods=['POST'])
def login():
    db = client['marketplace']
    users = db['users']
    attempt = request.get_json()
    for document in users.find({}, projection = {"_id" : False}):
        if document["netid"] == attempt['netid']:
            if document["password"] == attempt['password']:
                return json.dumps({"msg": "correct"} )
            else:
                return json.dumps({"msg": "incorrect information"})
    return json.dumps({"msg": "user not found"})

if __name__ == "__main__":
    app.run()