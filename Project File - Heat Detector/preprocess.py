import numpy as np

def preprocess(data):
    temp= data['Temperature[C]']
    humidity= data['Humidity[%]']
    tvoc= data['TVOC[ppb]']
    co2= data['eCO2[ppm]']
    raw_h2o= data['Raw H2']
    raw_ethanol= data['Raw Ethanol']
    pressure_hpa= data['Pressure[hPa]']
    pm_1= data['PM1.0']
    pm_2= data['PM2.5']
    nc_0= data['NC0.5']
    nc_1= data['NC1.0']
    nc_2= data['NC2.5']
    cnt= data['CNT']
    final_data= [temp, humidity, tvoc, co2, raw_h2o, raw_ethanol, pressure_hpa, pm_1, pm_2, nc_0, nc_1, nc_2, cnt]
    return np.array(final_data)