import numpy as np 
from flask import flask,request,jsonify,render_template
import joblib
import requests
app = flask(__name__)
model = joblib.load('power_prediction.sav')
@app.route('/')
def home():
    return render_template('intro.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/windapi',methods=['POST'])
def windapi():
    city=request.form.get('city')
    apikey="020d9cf529b79ed9f12891308e7e3c91"
    url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apikey
    resp = requests.get(url)
    resp=resp.json()
    temp = str(resp["main"]["temp"])+"°c"
    humid = str(resp["main"]["humidity"])+"%"
    presuure = str(resp["main"]["pressure"])+"mmHG"
    speed = str(str["main"]["speed"])+"m/s"
    return render_template('prdict.html', temp=temp, humid=humid,pressure=pressure, speed=speed)

@app.route('/y_predict',methods=['POST'])
def y_predict():
    ''' for rendering results on html gui '''
    x_test = [[float(x) for x in request.form.values()]]

    prediction = model.predict(x_test)
    print(prediction)
    output=prediction(0)
    return render_template('predict.html',prediction_text='the energy prediction is {:.2} kwh'.format(output))
if __name__ == "__main__":
    app.run(debug=false)