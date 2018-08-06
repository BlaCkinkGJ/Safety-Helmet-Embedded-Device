#include <cactus_io_DS18B20.h>
  
int DS18B20_Pin = 10; //DS18S20 Signal pin on digital 2
// Create DS18B20 object
DS18B20 ds(DS18B20_Pin);
  
void setup() {
    Serial.begin(9600);
    ds.readSensor();
    // we pass the serial number byte array into the printSerialNumber function
}
  
void loop() {
    ds.readSensor();
    Serial.println(ds.getTemperature_C());
    delay(100);
}
