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
   if request.method == 'GET':
      #Add all variables in the same way
      Fo = float(request.form.get('MDVP:Fo(Hz)'))
      Fhi = float(request.form.get('MDVP:Fhi(Hz)'))
      Flo = float(request.form.get('MDVP:Flo(Hz)'))
      JitterPercent = float(request.form.get('MDVP:Jitter(%)'))
      Jitter = float(request.form.get('MDVP:Jitter(Abs)'))
      RAP = float(request.form.get('MDVP:RAP'))
      PPQ = float(request.form.get('MDVP:PPQ'))
      DDP = float(request.form.get('Jitter:DDP'))
      Shimmer =  float(request.form.get('MDVP:Shimmer'))
      ShimmerDb =  float(request.form.get('MDVP:Shimmer(dB)'))
      ShimmerAPQ3 =  float(request.form.get('Shimmer:APQ3'))
      ShimmerAPQ5 =  float(request.form.get('Shimmer:APQ5'))
      APQ =  float(request.form.get('MDVP:APQ'))
      ShimmerDDA =  float(request.form.get('Shimmer:DDA'))
      NHR =  float(request.form.get('NHR')) 
      HNR =  float(request.form.get('HNR'))
      RPDE =  float(request.form.get('RPDE'))
      DFA =  float(request.form.get('DFA'))
      spread1 =  float(request.form.get('spread1'))
      spread2 =  float(request.form.get('spread2'))
      D2 =  float(request.form.get('D2'))
      PPE =  float(request.form.get('PPE'))
        
      #Add all the above variables in 2D list as below
      a1 = [[Fo, Fhi, Flo, JitterPercent, Jitter, RAP, PPQ, DDP, Shimmer, ShimmerDb, ShimmerAPQ3, ShimmerAPQ5, APQ, ShimmerDDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]]

      prediction = int(model.predict(a1))

      if prediction == 0:
         prediction = "You do not have Parkinson's Disease"
      elif prediction == 1:
         prediction = "You have Parkinson's Disease"
      else:
         prediction = 'Something went wrong!'
         
      return render_template('result.html', prediction = prediction)

if __name__ == '__main__':
   app.run(debug = True)
