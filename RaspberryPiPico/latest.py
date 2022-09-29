#board packages
import time
import board
import lib.adafruit_dht as adafruit_dht #adafruit library for dht11 sensor
import analogio

import json 
import os #paths and files package
import io

#storage packages
import busio
import sdcardio
import storage

"""

"""
class Ecosystem:
    """
    class constructor
    """
    def __init__(self):
        #temperature and humdity
        self.dht = adafruit_dht.DHT11(board.GP22) #original 27
        self.adc = analogio.AnalogIn(board.GP26) #original 26
        
        self.temperature, self.humidity, self.light_intensity = self.get_paramaters()
    
    """
    reads from sensors
    return: temperature
    return: humidity
    return: light_intensity
    """
    def get_paramaters(self):
        temperature = dht.temperature
        humidity = dht.temperature
        light_intensity = self.get_intensity(adc)*100
        return temperature, humditiy, light_intensity

    """
    light intensity getter
    return: light intensity
    """
    def get_intensity(self, sensor):
       return (sensor.value / 65535 * self.adc.reference_voltage)/3.7

"""
reads existing data in data.json file
return: existing_data data that has been previously stored
"""
def get_existing_data():
    try:
        with open('/sd/data.json') as f:
                existing_data = json.load(f)
    except Exception as e:
        print('error loading existing data', e)
    return existing_data

time.sleep(1)
#load board and pins
spi = busio.SPI(board.GP10, MOSI=board.GP11, MISO=board.GP12)
cs = board.GP15
sd = sdcardio.SDCard(spi, cs)

vfs = storage.VfsFat(sd)
storage.mount(vfs, '/sd')

while True:
    try:
        date_time = time.localtime()
        year = date_time.tm_year
        month = date_time.tm_mon
        day = date_time.tm_mday
        hour = date_time.tm_hour
        minute = date_time.tm_min
        second = date_time.tm_sec
        
        date_and_time = f"{year}/{month}/{day} {hour}:{minute}:{second}"
        
        print(date_and_time)
        
        terrarium = Ecosystem()
        
        time.sleep(1)

        existing_data = get_existing_data()
        
        data = {"date and time":date_and_time,
                "temp C":terrarium.temperature,
                "relative humidity %":terrarium.humidity,
                "light intensity %":terrarium.light_intensity
                }
                
        
#        to_do = "work out delay of sensor change"
        
#        print(json.dumps(data))
        
#        with open('/sd/data.json', 'a') as f:
#            f.write(json.dumps(data))
#            f.close()
    
        
    except Exception as e:
        print(e)


