from flask import Flask, render_template, request, redirect
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
        return render_template('backend.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        image = form['image']
        address = form['address']
        new_cafe = Item(name= name, image = image, address = address)
        new_cafe.save()
        return redirect('http://localhost:5000/addyourcafe')


if __name__ == '__main__':
  app.run(debug=True)
