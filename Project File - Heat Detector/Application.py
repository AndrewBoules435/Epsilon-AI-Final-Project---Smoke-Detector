import joblib
from flask import Flask, render_template, request
import preprocess
import numpy as np

app= Flask(__name__)
scaling= joblib.load('Models/scaling.h5')
model= joblib.load('Models/model.h5')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods= ['POST', 'GET'])

def get_prediction():
    if request.method == 'POST':
        temp= request.form['temp']
        humidity= request.form['Humidity']
        tvoc= request.form['tvoc']
        co2= request.form['co2']
        raw_h2o= request.form['raw_h2o']
        raw_ethanol= request.form['raw_ethanol']
        pressure_hpa= request.form['pressure_hpa']
        pm_1= request.form['pm_1']
        pm_2= request.form['pm_2']
        nc_0= request.form['nc_0']
        nc_1= request.form['nc_1']
        nc_2= request.form['nc_2']
        cnt= request.form['cnt']
    data= {'Temperature[C]':temp, 'Humidity[%]':humidity, 'TVOC[ppb]':tvoc, 'eCO2[ppm]':co2, 'Raw H2':raw_h2o,
           'Raw Ethanol':raw_ethanol, 'Pressure[hPa]':pressure_hpa, 'PM1.0':pm_1, 'PM2.5':pm_2, 'NC0.5':nc_0,
           'NC1.0':nc_1, 'NC2.5':nc_2, 'CNT':cnt}

    final_data= preprocess.preprocess(data)
    scaled_data= scaling.transform([final_data])
    prediction= int(model.predict(scaled_data)[0])
    return render_template('prediction.html', Fire_Alarm_Status= str(prediction))

if __name__ == '__main__':
    app.run(debug = True)
