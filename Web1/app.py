from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/')
# def index():
#     return "Hello C4E13"
#
# @app.route('/hello-me')
# def hello_me():
#     return "Hello Everyone"
#
# @app.route('/<lastname>/<firstname>')
# def hello(lastname, firstname):
#     return "Hello " + firstname + " " + lastname
#
# @app.route('/sum/<int:x>/<int:y>')
# def sum(x,y):
#     return str(x + y)

if __name__ == '__main__':
  app.run (debug=True)
