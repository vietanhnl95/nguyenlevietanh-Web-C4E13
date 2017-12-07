import mlab
from mongoengine import *

mlab.connect()

class Item(Document):
    name = StringField()
    image = StringField()
    address = StringField()

# while True:
#     name = str(input("Cafe name: "))
#     img = str(input("Img URL: "))
#     add = str(input("Address: "))
#     cf = Item(
#         name = name,
#         image = img,
#         address = add
#     )
#     cf.save()
#     print('-'*10)
