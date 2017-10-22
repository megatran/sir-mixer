const int led = 3;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(460800);
  pinMode(led, OUTPUT);
  digitalWrite(led, LOW);
}
void loop() {
  // put your main code here, to run repeatedly:
  Serial.print("Serial received: ");
  if(Serial.available() > 0)
    {
      int test = Serial.readString().toInt();
	if(test == 1)
      {
        digitalWrite(led, HIGH);
	delay(5000);
      }
      else digitalWrite(led, LOW);
    }
    
}
