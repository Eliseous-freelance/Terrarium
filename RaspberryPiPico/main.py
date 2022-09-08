import time
import board
import adafruit_dht
import analogio

dht = adafruit_dht.DHT11(board.GP27)
adc = analogio.AnalogIn(board.GP26)
def getIntense(sensor):
    return (sensor.value / 65535 * adc.reference_voltage)/3.7
#print(dht)
while True:
    print("Temperature",dht.temperature,"C")
    print("Humidity", dht.humidity,"%")
    print("Light intesnity",getIntense(adc)*100,"%")
    time.sleep(1)
    if dht.temperature>25:
        print("Damnnnn you hot dummy thiccc")
        
    

