#include <cactus_io_DS18B20.h>

/*** Function declaration is here ***/
String  getTemperature     (void);
String  getConnectedState  (void);
char    readDataFromSerial (void);
int     sendDataToSerial   (String data);
int     alertByBuzzer      (int   alert);
/*** Function declaration is here ***/

/*** Port information is here ***/
enum port {
    PORT_DS18B20       = 2,
    PORT_BUZZER        = 5,
    PORT_CONNECTOR_IN  = 4,
    PORT_CONNECTOR_OUT = 3
};
/*** Port information is here ***/

/*** Global Variables are here ***/
DS18B20   temperModule(PORT_DS18B20);
/*** Global Variables are here ***/


////////////// main sequence //////////////
void setup() {
  Serial.begin(9600);

  pinMode(PORT_BUZZER,        OUTPUT);
  pinMode(PORT_CONNECTOR_IN,  INPUT );
  pinMode(PORT_CONNECTOR_OUT, OUTPUT);

  // Make connector can get value
  digitalWrite(PORT_CONNECTOR_OUT, HIGH);

  // Start the read DS18B20 module
  temperModule.readSensor();
}
void loop() {
    String temper = getTemperature();
    String  state  = getConnectedState();
    
    sendDataToSerial(String(temper + "\t" + state));
    if(Serial.available()){
        char data = readDataFromSerial();
        alertByBuzzer(data == 50);
    }
    
    delay(10);
}
////////////// main sequence //////////////


/*** Function definition is here ***/
String getTemperature(void){
    temperModule.readSensor();
    float temper = temperModule.getTemperature_C();

    int upper = (int)temper;
    int lower = (int)((temper - upper)*100);

    String result = (String(upper) + "." + String(lower));
    return result;
}

String getConnectedState(void){
   // ONLY OUTPUT PORT CAN DISCONNECTED
    return String(digitalRead(PORT_CONNECTOR_IN)==HIGH);
}

char readDataFromSerial(void){
    return Serial.read();
}

int sendDataToSerial(String data){
    // number of bytes returned FOR DEBUG
    return Serial.println(data);
}

int alertByBuzzer(int alert){
    if(alert) tone  (PORT_BUZZER, 1000);
    else      noTone(PORT_BUZZER);

    return alert;
}
/*** Function definition is here ***/
