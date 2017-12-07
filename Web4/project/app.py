from flask import Flask, render_template
import mlab
from mongoengine import *

app = Flask(__name__)

#1. Connect to database
mlab.connect()

#2. Design collection
class Item(Document):
    title = StringField()
    image = StringField()
    description = StringField()
    price = IntField()

#3. Try insert an item
# cassete = Item(
#     title="Old Cassete",
#     image="https://via.placeholder.com/300x300",
#     description="Old and uselss cassete",
#     price=200000
# )

# cassete.save()

# items = Item.objects()
# for item in items:
#     print(item.title)
#     print(item.price)

@app.route('/')
def index():
    return render_template('index.html',
                title="TV Cũ",
                image="https://cdn1.tgdd.vn/Files/2015/09/26/708646/bi-kip-chon-mua-tivi-cu-1.jpg")

@app.route('/list')
def title_list():
    return render_template('title_for.html', titles=['Tv cũ', 'Cát sét cũ', 'Điện thoại cũ'])

@app.route('/object')
def object():
    x = {
        'title': 'TV cũ giá cao',
        'image': 'https://cdn1.tgdd.vn/Files/2015/09/26/708646/bi-kip-chon-mua-tivi-cu-1.jpg',
        'description': 'Tv vì cũ nên giá cao'
    }
    return render_template('object.html', item=x)

@app.route('/object-list')
def object_list():
    data = Item.objects()
    # data = [
    #     {
    #         "title": "Old TV",
    #         "image": "https://via.placeholder.com/200x200",
    #         "description": "Old and useless TV"
    #     },
    #     {
    #         "title": "Old phone",
    #         "image": "https://via.placeholder.com/200x200",
    #         "description": "Old and useless phone"
    #     },
    #     {
    #         "title": "Old cassete",
    #         "image": "https://via.placeholder.com/200x200",
    #         "description": "Old and useless cassete"
    #     },
    # ]
    return render_template('object_list.html', items=data)

if __name__ == '__main__':
  app.run(debug=True)
