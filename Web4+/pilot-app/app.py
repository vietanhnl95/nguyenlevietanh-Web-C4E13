from flask import Flask, render_template, request, flash
import mlab
from mongoengine import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "super_key"

#1. Connect to database
mlab.connect()

#2. Design collection
class Item(Document):
    title = StringField()
    image = StringField()
    description = StringField()
    price = IntField()

@app.route('/')
def index():
    items = Item.objects()
    return render_template('index.html', items=items)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'GET':
        return render_template('add_item.html')
    elif request.method == 'POST':
        form = request.form
        title = form['title'] #key from name attribute of input
        image = form['image']
        description = form['description']
        price = form['price']
        new_item = Item(title=title, image=image, description=description, price=price)
        new_item.save()
        return "OK"

@app.route('/admin')
def admin():
    return render_template('admin.html',items=Item.objects())

@app.route('/edit-item/<item_id>', methods = ['GET','POST'])
def edit_item(item_id):
    item = Item.objects().with_id(item_id)
    if request.method == 'GET':
        return render_template('edit_item.html',item=item)
    elif request.method == 'POST':
        form = request.form

        title = form['title']
        description = form['description']
        image = form['image']
        price = form['price']

        item.update(title=title,description=description,image=image,price=price)
        flash("Updated")
        flash("Continue")

        return render_template('edit_item.html',item=Item.objects().with_id(item_id))

if __name__ == '__main__':
  app.run(debug=True)
