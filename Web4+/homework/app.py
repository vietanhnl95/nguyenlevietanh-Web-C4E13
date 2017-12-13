from flask import Flask, render_template, request, redirect, flash, redirect
import mlab
from mongoengine import *

app = Flask(__name__)

mlab.connect()

class Item(Document):
    name = StringField()
    image = StringField()
    address = StringField()

@app.route('/')
def index():
    cf_shops = Item.objects
    return render_template('index.html', cf_shops = cf_shops)

@app.route('/addyourcafe', methods = ['GET', 'POST'])
def backend_insert():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        image = form['image']
        address = form['address']
        new_cafe = Item(name= name, image = image, address = address)
        new_cafe.save()
        return redirect('http://localhost:5000/addyourcafe')

@app.route('/admin')
def admin():
    return render_template('admin.html',cf_shops = Item.objects())

@app.route('/edit/<shop_id>', methods = ['GET', 'POST'])
def edit_shop(shop_id):
    cf_shop = Item.objects().with_id(shop_id)
    if request.method == 'GET':
        return render_template ('edit.html', cf_shop = cf_shop)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        image = form['image']
        address = form['address']
        cf_shop.update(name= name, image = image, address = address)
        return render_template('edit.html', cf_shop = cf_shop)

@app.route('/delete/<shop_id>', methods = ['GET', 'POST'])
def delete_shop(shop_id):
    cf_shop = Item.objects().with_id(shop_id)
    if request.method == 'GET':
        return render_template('delete.html', cf_shop = cf_shop)
    elif request.method == 'POST':
        cf_shop.delete()
        return redirect('/after-delete')

@app.route('/after-delete')
def after_delete():
    return render_template('after_delete.html')

if __name__ == '__main__':
  app.run(debug=True)
