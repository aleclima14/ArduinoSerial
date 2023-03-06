#include <Arduino.h>

bool statusLed = false;
String readStringData = "";
String ledOn = "on";
String ledOff = "off";

void setup() 
{
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
}

void loop() 
{ 
  if(Serial.available() > 0)
  {
    readStringData= Serial.readString(); 
    readStringData.trim();
  }

  if (readStringData == ledOn) 
  {
    digitalWrite(LED_BUILTIN, LOW);
    statusLed = true;
  }
  if (readStringData == ledOff)
  {
    digitalWrite(LED_BUILTIN, HIGH);
    statusLed = false;
  }

  if(statusLed)
  {
    Serial.println("Led On");
  }
  else
  {
    Serial.println("Led Off");
  }
}
