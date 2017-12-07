from flask import Flask, render_template, get_template_attribute, request
import mlab
from input_app import Item
from mongoengine import *

app = Flask(__name__)

# @app.route('/backend', methods = ['POST'])
# def backend_insert():
#     mlab.
#     name = request.form.get['name']
#     image = request.form.get['img']
#     description = request.form.get['des']
#     Item.insert({'name': name, 'image': image, 'description': description})

@app.route('/addyourcafe')
def backend():
    return render_template('backend.html')

@app.route('/')
def index():
    return render_template('index.html', cf_shops = Item.objects)

if __name__ == '__main__':
  app.run(debug=True)
