#board packages
import time
import board
import lib.adafruit_dht as adafruit_dht
import analogio

import json

#temperature and humdity
dht = adafruit_dht.DHT11(board.GP27)
adc = analogio.AnalogIn(board.GP26)

#light intensity
def getIntense(sensor):
   return (sensor.value / 65535 * adc.reference_voltage)/3.7



while True:
    temperature = dht.temperature
    humidity = dht.temperature
    light_intensity = getIntense(adc)*100
    date_time = time.localtime()
        
    time.sleep(1)

    
    data = {"date":f"{date_time.tm_year}-{date_time.tm_mon}-{date_time.tm_mday}",
            "time":f"{date_time.tm_hour}:{date_time.tm_min}:{date_time.tm_sec}",
            "temp C":f"{temperature}",
            "relative humidity %":f"{humidity}",
            "light intensity %":f"{light_intensity}"
            }
            
    
    to_do = "work out delay of sensor change"
    
    print(json.dumps(data))

    try:
        file_ = open('/data.json')
        
        file_.write(json.dumps(data))
        file_.close()
    except Exception as e:
        print(e)
        
    #if os.dir.exists('/documents/terrarium_data/'):
    #   pd.DataFrame(data).to_csv('/Documents/terrarium_data/data.csv')
