const int buzzer = 3;

void setup(){
  Serial.begin(9600);
  pinMode(buzzer, OUTPUT);
}

void loop(){
  static int counter = 101;
  static int up = 1;
  tone(buzzer, counter);
  if(Serial.available() > 0){
    char val = Serial.read();
    Serial.println(val);
  }
  
  if(counter > 500 || counter < 100)
    up ^= 1;
   
   if(up == 1)
     counter++;
    else
     counter--;
 
   delay(5);
}
