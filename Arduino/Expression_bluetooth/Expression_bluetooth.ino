#include <Wire.h>
#include <Adafruit_GFX.h>
#include "Adafruit_LEDBackpack.h"
#include <Servo.h>

Servo s_1;
Servo s_2;

Adafruit_8x8matrix matrix = Adafruit_8x8matrix();

char data = 0;                 //Variable for storing received data

void setup()
{
    Serial.begin(9600);          //Sets the data rate in bits per second (baud) for serial data transmission
    pinMode(13, OUTPUT);         //Sets digital pin 13 as output pin

  matrix.begin(0x70);  // pass in the address
  s_1.attach(2);
  s_2.attach(3);

}

static const uint8_t PROGMEM

happy_bmp[] =
{
  B00000000,
  B01111000,
  B01000100,
  B01011010,
  B01011010,
  B01000100,
  B01111000,
  B00000000
},

neutral_bmp[] =
{
  B00000000,
  B00011000,
  B00100100,
  B01011010,
  B01011010,
  B00100100,
  B00011000,
  B00000000
},

surprised_bmp[] =
{
  B01111110,
  B10000001,
  B10000001,
  B10011001,
  B10011001,
  B10000001,
  B10000001,
  B01111110
},

love_bmp[] =
{
  B00011110,
  B00100001,
  B01000001,
  B10011010,
  B10011010,
  B01000001,
  B00100001,
  B00011110
},

meh_bmp[] =
{
  B00000000,
  B00000100,
  B00000100,
  B00000100,
  B00011100,
  B00011100,
  B00000100,
  B00000000
},

blink_bmp[] =
{
  B00000000,
  B00100000,
  B01000000,
  B01000000,
  B01000000,
  B01000000,
  B00100000,
  B00000000
},

sad_bmp[] =
{
  B00000000,
  B00000100,
  B01111100,
  B00000100,
  B00000100,
  B01111100,
  B00000100,
  B00000000
};


void neutral()
{
  s_1.write(107);
  s_2.write(50);

  matrix.clear();
  matrix.drawBitmap(0, 0, neutral_bmp, 8, 8, LED_ON);
  matrix.writeDisplay();
  delay(2050);

  matrix.clear();
  matrix.drawBitmap(0, 0, blink_bmp, 8, 8, LED_ON);
  matrix.writeDisplay();
  delay(250);
}

void sad()
{
  s_1.write(130);
  s_2.write(30);

  matrix.clear();
  matrix.drawBitmap(0, 0, sad_bmp, 8, 8, LED_ON);
  matrix.writeDisplay();
  delay(2050);

  matrix.clear();
  matrix.drawBitmap(0, 0, blink_bmp, 8, 8, LED_ON);
  matrix.writeDisplay();
  delay(250);

}

void surprised()
{

  s_1.write(70);
  s_2.write(80);

  matrix.clear();
  matrix.drawBitmap(0, 0, surprised_bmp, 8, 8, LED_ON);
  matrix.writeDisplay();
  delay(2050);

  matrix.clear();
  matrix.drawBitmap(0, 0, blink_bmp, 8, 8, LED_ON);
  matrix.writeDisplay();
  delay(250);

}

void meh()
{

  s_1.write(70);
  s_2.write(50);


  matrix.clear();
  matrix.drawBitmap(0, 0, meh_bmp, 8, 8, LED_ON);
  matrix.writeDisplay();
  delay(2050);

  matrix.clear();
  matrix.drawBitmap(0, 0, blink_bmp, 8, 8, LED_ON);
  matrix.writeDisplay();
  delay(250);
}

void happy()
{

  s_1.write(130);
  s_2.write(30);

  matrix.clear();
  matrix.drawBitmap(0, 0, happy_bmp, 8, 8, LED_ON);
  matrix.writeDisplay();
  delay(2050);

  matrix.clear();
  matrix.drawBitmap(0, 0, blink_bmp, 8, 8, LED_ON);
  matrix.writeDisplay();
  delay(250);
}

void love()
{

  s_1.write(130);
  s_2.write(30);

  matrix.clear();
  matrix.drawBitmap(0, 0, love_bmp, 8, 8, LED_ON);
  matrix.writeDisplay();
  delay(2050);

  matrix.clear();
  matrix.drawBitmap(0, 0, blink_bmp, 8, 8, LED_ON);
  matrix.writeDisplay();
  delay(250);

}

void bluetooth()
{
   if (Serial.available() > 0) // Send data only when you receive data:
        {
          data = Serial.read();       //Read the incoming data and store it into variable data
          Serial.write(data);         //Print Value inside data in Serial monitor
          Serial.write("\n");         //New line  

      if (data == '1') 
      {
        surprised();
      }

      else if (data == '2') 
          {
        meh();
      }


      else if (data == '3') 
          {
        happy();
      }


      else if (data == '4') 
          {
        love();
      }
      else if (data == '5') 
          {
        sad();
      }
    }
}

void loop()
{
   bluetooth();
   neutral();

}
 
