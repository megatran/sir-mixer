#include <Servo.h>

void pourDrink(int, int);
void mix();

const int dig0 = 2;
const int dig1 = 3;
const int dig2 = 4;
const int dig3 = 5;
const int dig4 = 6;

Servo servo1, servo2, servo3, servo4;

int upAng1 = 0;
int upAng2 = 105;
int upAng3 = 180;
int upAng4 = 130;

int downAng1 = 55;
int downAng2 = 160;
int downAng3 = 130;
int downAng4 = 105;

int dur2 = 5000;
int dur4 = 9000;

bool runOnce = true;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(dig0, OUTPUT);
  pinMode(dig1, OUTPUT);
  pinMode(dig2, OUTPUT);
  pinMode(dig3, OUTPUT);
  pinMode(dig4, OUTPUT);

  digitalWrite(dig0, LOW);

  servo1.attach(dig1);
  servo1.write(upAng1);
  servo1.detach();
  delay(1000);

  servo2.attach(dig2);
  servo2.write(upAng2);
  servo2.detach();
  delay(1000);

  servo3.attach(dig3);
  servo3.write(upAng3);
  servo3.detach();
  delay(1000);

  servo4.attach(dig4);
  servo4.write(upAng4);
  servo4.detach();
  delay(1000);
}

void loop() {

  pourDrink(2, dur2);
  delay(1000);
  pourDrink(4, dur4);
  delay(1000);
  servo4.detach();

  //mix();

  while (runOnce);
}

void pourDrink(int whichServo, int duration)
{
  switch (whichServo)
  {
    case 1:
      if (!servo1.attached()) servo1.attach(dig1);
      if (servo2.attached()) servo2.detach();
      if (servo3.attached()) servo3.detach();
      if (servo4.attached()) servo4.detach();

      for (int i = upAng1; i <= downAng1; i++)
      {
        servo1.write(i);
        delay(25);
      }

      delay(duration);

      for (int j = downAng1; j >= upAng1; j--)
      {
        servo1.write(j);
        delay(25);
      }
      break;
    case 2:
      if (!servo2.attached()) servo2.attach(dig2);
      if (servo1.attached()) servo1.detach();
      if (servo3.attached()) servo3.detach();
      if (servo4.attached()) servo4.detach();

      for (int i = upAng2; i <= downAng2; i++)
      {
        servo2.write(i);
        delay(25);
      }

      delay(duration);

      for (int j = downAng2; j >= upAng2; j--)
      {
        servo2.write(j);
        delay(25);
      }
      break;
    case 3:
      if (!servo3.attached()) servo3.attach(dig3);
      if (servo2.attached()) servo2.detach();
      if (servo1.attached()) servo1.detach();
      if (servo4.attached()) servo4.detach();

      for (int i = upAng3; i >= downAng3; i--)
      {
        servo3.write(i);
        delay(25);
      }

      delay(duration);

      for (int j = downAng3; j <= upAng3; j++)
      {
        servo3.write(j);
        delay(25);
      }
      break;
    case 4:
      if (!servo4.attached()) servo4.attach(dig4);
      if (servo2.attached()) servo2.detach();
      if (servo3.attached()) servo3.detach();
      if (servo1.attached()) servo1.detach();

      for (int i = upAng4; i >= downAng4; i--)
      {
        servo4.write(i);
        delay(25);
      }

      delay(duration);

      for (int j = downAng4; j <= upAng4; j++)
      {
        servo4.write(j);
        delay(25);
      }
      break;
  }
}

void mix()
{
  digitalWrite(dig0, HIGH);
  delay(5000);
  digitalWrite(dig0, LOW);
}

