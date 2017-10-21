int pin = 12;

void setup() {
	pinMode(pin, OUTPUT);
//	digitalWrite(pin, HIGH);
//	delay(3000);
//	digitalWrite(pin, LOW);
}

void loop()
{
//	exit(0);
	digitalWrite(pin, HIGH);
	delay(3000);
	digitalWrite(pin, LOW);
	delay(3000);
	exit(0);
}
