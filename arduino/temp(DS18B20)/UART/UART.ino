#include <cactus_io_DS18B20.h>
  
int DS18B20_Pin = 10; //DS18S20 Signal pin on digital 2
// Create DS18B20 object
DS18B20 ds(DS18B20_Pin);
  
void setup() {
    ds.readSensor();
  
    Serial.begin(9600);
    Serial.println("Maxim Integrated DS18B20 Temperature Sensor | cactus.io");
    Serial.println("DS18B20 Serial Number: ");
      
    // we pass the serial number byte array into the printSerialNumber function
    printSerialNumber(ds.getSerialNumber());
      
    Serial.println("");
    Serial.println("");
    Serial.println("Temp (C)\tTemp (F)");
}
  
void loop() {
    ds.readSensor();
      
    Serial.print(ds.getTemperature_C()); Serial.print(" *C\t");
    Serial.print(ds.getTemperature_F()); Serial.println(" *F");
      
    // Add a 2 second delay.
    delay(100);
}
  
// We call this function to display the DS18B20 serial number.
// It takes an array of bytes for printing
void printSerialNumber(byte *addr) {
    byte i;
    for( i = 0; i < 8; i++) {
        Serial.print("0x");
        if (addr[i] < 16) {
            Serial.print('0');
        }
      
        Serial.print(addr[i], HEX);
        if (i < 7) {
            Serial.print(", ");
        }
    }
}

