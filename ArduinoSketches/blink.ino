#include "DHT.h"
#define DHTPIN 2     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
DHT dht(DHTPIN, DHTTYPE);

void setup() {
        Serial.begin(9600);
        Serial.println(F("DHTxx test!"));
        dht.begin();
}

void loop() {
        float h = dht.readHumidity();        // read humidity
        float t = dht.readTemperature();     // read temperature
        float f = dht.readTemperature(true);
        if (isnan(h) || isnan(t) || isnan(f)) {
                Serial.println(F("Failed to read from DHT sensor!"));
                return;
        }
    float hif = dht.computeHeatIndex(f, h);
        float hic = dht.computeHeatIndex(t, h, false);
        Serial.print(F(" Humidity: "));
        Serial.print(h);
        Serial.print(F("%  Temperature: "));
        Serial.print(t);
        Serial.print(F("°C "));
        Serial.print(f);
        Serial.print(F("°F  Heat index: "));
        Serial.print(hic);
        Serial.print(F("°C "));
        Serial.print(hif);
        Serial.println(F("°F"));
}


