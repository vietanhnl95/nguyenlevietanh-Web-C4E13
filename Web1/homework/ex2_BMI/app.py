from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    bmi = weight/(height*2)
    if bmi < 16:
        return "Severly Underweight"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
    
if __name__ == '__main__':
  app.run(debug=True)
