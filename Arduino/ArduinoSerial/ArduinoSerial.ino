void setup() 
{
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() 
{ 
  String readStringData = Serial.readString(); 
  readStringData.trim();

  if (readStringData == "on") 
  {
    digitalWrite(LED_BUILTIN, HIGH);
  }
   
  if (readStringData == "off")
  {
    digitalWrite(LED_BUILTIN, LOW);
  }
}
