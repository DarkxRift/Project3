#include <Wire.h>
#include <I2Cdev.h>
#include "MPU6050.h"

 

MPU6050 accelgyro;

//make running things asyncronously call within the loop and give it the argument of after how many milliseconds it should run
#define runEvery(t) for (static long _lasttime;\
                         (uint16_t)((uint16_t)millis() - _lasttime) >= (t);\
                         _lasttime += (t))
 

 
//int16_t is a 16bit integer. Store accelerometer x ,y and z value in unsigned 16bit integer.
int16_t ax, ay, az;
//Set up accelerometer variables
float accBiasX, accBiasY, accBiasZ;  
float accAngleX, accAngleY;
double accPitch, accRoll;

 
//int16_t is a 16bit integer. Store gyroscope x ,y and z value in unsigned 16bit integer.
int16_t gx, gy, gz;

//Set up gyroscope variables
float gyroBiasX, gyroBiasY, gyroBiasZ;
float gyroRateX, gyroRateY, gyroRateZ;
float gyroBias_oldX, gyroBias_oldY, gyroBias_oldZ;
float gyroPitch = 180;
float gyroRoll = -180;
float gyroYaw = 0;

 
//set up a 32 bit timer
uint32_t timer;

 
// input
double InputPitch, InputRoll;

 
// initial values
double InitialRoll;

 

// Motors drivers pins
int enablea = 3;
int enableb = 6;
int a1 = 4;
int a2 =8;
int b1 = 5 ;
int b2 = 7;

  

void setup() 
{

  Wire.begin();
  Serial.begin(9600);
  Serial.println("Initializing I2C devices...");
  accelgyro.initialize();


  // verify connection
  Serial.println("Testing device connections...");
  Serial.println(accelgyro.testConnection() ? "MPU6050 connection successful" : "MPU6050 connection failed");

 
  delay(1500);

 

  // Motor 
  pinMode(enablea, OUTPUT);
  pinMode(enableb, OUTPUT);
  pinMode(a1, OUTPUT);
  pinMode(a2, OUTPUT);
  pinMode(b1, OUTPUT);
  pinMode(b2, OUTPUT);

  digitalWrite(a1, HIGH);
  digitalWrite(a2, HIGH);
  digitalWrite(b1, HIGH);
  digitalWrite(b2, HIGH);

 

 // calibration

 accelgyro.setXAccelOffset(-914);
 accelgyro.setYAccelOffset(-115);
 accelgyro.setZAccelOffset(916);
 accelgyro.setXGyroOffset(24);
 accelgyro.setYGyroOffset(2);
 accelgyro.setZGyroOffset(-11);

 gyroBiasX = -1;
 gyroBiasY = 0;
 gyroBiasZ = 1;

 accBiasX = 3;
 accBiasY = -5;
 accBiasZ = 16387;

 

  //Get accelerometer/gyroscope readings

  accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);


  accPitch = (atan2(-ax, -az) + PI) * RAD_TO_DEG; //converts angle position units from radians to degrees
  accRoll = (atan2(ay, -az) + PI) * RAD_TO_DEG;   //converts angle position units from radians to degrees

 
  //Calcuation for roll and pitch 
  
  if (accPitch <= 360 & accPitch >= 180) 
  {

    accPitch = accPitch - 360;

  }

  if (accRoll <= 360 & accRoll >= 180) 
  {

    accRoll = accRoll - 360;

  }

 

  gyroPitch = accPitch;
  gyroRoll = accRoll;

  timer = micros();
  delay(1000);
  initializeValues();  //Run InitializeValue Function

 

}

double Setpoint;

void MotorControl(double out) {

  if (out > 0) {

    digitalWrite(a1, HIGH);
    digitalWrite(a2, LOW);
    digitalWrite(b1, HIGH);
    digitalWrite(b2,LOW);

  } else {

    digitalWrite(a1,LOW);
    digitalWrite(a2,HIGH);
    digitalWrite(b1, LOW);
    digitalWrite(b2, HIGH);

  }

 

  byte vel = abs(out);

  if (vel < 0)
    vel = 0;
  if (vel > 255)
    vel = 255;

 

  analogWrite(enablea, vel);
  analogWrite(enableb, vel);

}

 

void initializeValues() {

//Get accelerometer/gyroscope readings
  accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

 

  //////////////////////

  //  Accelerometer   //

  //////////////////////

  accPitch = (atan2(-ax/182.0, -az/182.0) + PI) * RAD_TO_DEG; //converts angle position units from radians to degrees

  accRoll = (atan2(ay/182.0, -az/182.0) + PI) * RAD_TO_DEG;  //converts angle position units from radians to degrees


 
//Calcuation for roll and pitch 

  if (accRoll <= 360 & accRoll >= 180) {

    accRoll = accRoll - 360;

  }

 

  //////////////////////

  //      GYRO        //

  //////////////////////

 

  gyroRateX = ((int)gx - gyroBiasX) * 131;

 

  gyroPitch += gyroRateY * ((double)(micros() - timer) / 1000000);

  timer = micros();

  InitialRoll = accRoll;
  Setpoint = InitialRoll;

}

 

double filtered = 0;

void loop() {

 
//This will call the first print every 10 milliseconds forever
  runEvery(10) {

    accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

    //////////////////////

    //  Accelerometer   //

    //////////////////////

    accRoll = (atan2(ay/182.0, -az/182.0) + PI) * RAD_TO_DEG;


    if (accRoll <= 360 & accRoll >= 180) {

      accRoll = accRoll - 360;

    }


    //////////////////////

    //      GYRO        //

    //////////////////////

 

    gyroRateX = -((int)gx - gyroBiasX) / 131;

    double gyroVal = gyroRateX * ((double)(micros() - timer) / 1000000);

    timer = micros();

    //Complementary filter

    filtered = 0.98 * (filtered + gyroVal) + 0.02 * (accRoll);

    MotorControl(Compute(filtered - InitialRoll));

 

  }

 

}

 

   //////////////////////

  //      PID       //

 //////////////////////
 
int outMax = 255;
int outMin = -255;
float lastInput = 0;   // Keeps track of error over time
double ITerm = 0;      // Used to accumalate error (intergral)
double kp =100;//100
double ki =52;//80
double kd =0;

 

double Compute(double input)

{

 
  // Calculate our PID terms
  double error = Setpoint - input;
  ITerm += (ki * error);

  if (ITerm > outMax) ITerm = outMax;
  else if (ITerm < outMin) ITerm = outMin;
  double dInput = (input - lastInput);

 
  /*Compute PID Output*/

  double output = kp * error + ITerm + kd * dInput;

 

  if (output > outMax) output = outMax;
  else if (output < outMin) output = outMin;


  /*Remember some variables for next time*/

  lastInput = input;
  return output;

}

 


 

 


