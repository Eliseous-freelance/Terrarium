#board packages
import time
import board
import adafruit_dht
import analogio

#temperature and humdity
dht = adafruit_dht.DHT11(board.GP27)
adc = analogio.AnalogIn(board.GP26)
#light intensity
def getIntense(sensor):
    return (sensor.value / 65535 * adc.reference_voltage)/3.7


from github import Github
import pandas as pd
g = Github("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")

repo = g.get_user().get_repo('Terrarium')

print(pd.read_csv(repo.get_contents('data/database.csv').download_url))


#while True:
#  
#    temperature = dht.temperature
#    humdity = dht.temperature
#    light_intensity = getIntense(adc)*100
#    
#    
#    time.sleep(1)

    #print("Temperature",temperature,"C")
    #print("Humidity", humdity,"%")
    #print("Light intesnity",light_intensity,"%")
    #if temperature>25:
    #    print("Damnnnn you hot dummy thiccc")
        
        



