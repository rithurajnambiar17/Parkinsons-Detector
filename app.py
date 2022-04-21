from flask import Flask, render_template, request
import joblib
import numpy as np
app = Flask(__name__)

model = joblib.load('model.h5')

app.static_folder = 'static'

@app.route('/')
def student():
   return render_template('Page2.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      #Add all variables in the same way
      # latitude = float(request.form.get('lat'))
      # longitude = float(request.form.get('lon'))
      # housing_age = float(request.form.get('age'))
      # total_rooms = float(request.form.get('rooms'))
      # total_bedrooms = float(request.form.get('bed'))
      # population = float(request.form.get('pop'))
      # households = float(request.form.get('holds'))
      # income = float(request.form.get('inc'))
      # ocean_proximity =  float(request.form.get('oceanp'))

      #Add all the above variables in 2D list as below
      # a1 = [[longitude, latitude, housing_age, total_rooms, total_bedrooms, population, households, income, ocean_proximity, rph, bpr, pph]]

      prediction = int(model.predict(a1))

      if prediction == 0:
         prediction = 'You dont have parkinson'
      elif prediction == 1:
         prediction = 'You have parkinson'
      else:
         prediction = 'Something went wrong!'
         
      return render_template('result.html', prediction = prediction)

if __name__ == '__main__':
   app.run(debug = True)