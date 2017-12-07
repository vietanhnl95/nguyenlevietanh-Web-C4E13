import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds155634.mlab.com:55634/coffee_shops_db

host = "ds155634.mlab.com"
port = 55634
db_name = "coffee_shops_db"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
