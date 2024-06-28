int packetCounter = 0;
#include <LoRa.h>
#include "Wire.h"
void setup(){
  // put your setup code here, to run once:
  
  Wire.begin();
  //delay(10);
  Serial.begin(115200);
  while (!Serial);

  //Serial.println("LoRa Sender");
  LoRa.setPins(5,32,33);
  LoRa.setTxPower(20);
    
  if (!LoRa.begin(915E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}

void loop() {
  generate_data();
}

/* data packet format:-
pkt, RTC->(hh:mm:ss), ALTIMETER->(alt, pressure, temp), GPS->(lat, long, alt, speed, HEADING, GPS_time, GPS_date, GPS_sats), IMU->(ax, ay, az, gx, gy, gz), velocity, pitch, yaw, roll, magnetometer heading, voltage, flight state, RSSI
*/
void generate_data(){
  LoRa.beginPacket();
  packetCounter++;
  Serial.print(packetCounter);LoRa.print(packetCounter);
  Serial.print(",");LoRa.print(",");

  gen_time();
  Serial.print(",");LoRa.print(",");

  //ALTIMETER--------
  gen_alt();
  Serial.print(",");LoRa.print(",");
  gen_press();
  Serial.print(",");LoRa.print(",");
  gen_temp();
  Serial.print(",");LoRa.print(",");

  //GPS--------------
  gen_lat_long();
  Serial.print(",");LoRa.print(",");
  gen_GPS_alt();
  Serial.print(",");LoRa.print(",");
  gen_GPS_speed();
  Serial.print(",");LoRa.print(",");
  gen_GPS_heading();
  Serial.print(",");LoRa.print(",");
  gen_GPS_time();
  Serial.print(",");LoRa.print(",");
  gen_GPS_date();
  Serial.print(",");LoRa.print(",");
  gen_GPS_SATS();
  Serial.print(",");LoRa.print(",");

  //IMU--------------
  gen_acc();
  Serial.print(",");LoRa.print(",");
  gen_gyro();
  Serial.print(",");LoRa.print(",");

  //MISC.-------------
  gen_velocity();
  Serial.print(",");LoRa.print(",");
  gen_pitch_yaw_roll();
  Serial.print(","); LoRa.print(",");
  gen_magnetometer_heading();
  Serial.print(","); LoRa.print(",");
  gen_volt();
  Serial.print(",");LoRa.print(",");
  gen_flight_state();
  Serial.print(",");LoRa.print(",");
  gen_trigger();
  Serial.print(",");LoRa.print(",");
  //==en_RSSI();
  LoRa.endPacket();

  //delay(1000);
}

void gen_time(){
  Serial.print("hh:mm:ss");LoRa.print("hh:mm:ss");
}

//ALTIMETER=========================================================================================================

void gen_alt(){
  float alt = random(0, 100000) / 10.0;
  Serial.print(alt, 3);LoRa.print(alt,3);
}

void gen_press(){
  float pressure = random(0, 100000) / 10.0;
  Serial.print(pressure, 3);LoRa.print(pressure, 3);
}

void gen_temp(){
  float minTemp = 20.0;
  float maxTemp = 30.0;
  float temp = random(minTemp * 10, (maxTemp + 1) * 10) / 10.0;
  Serial.print(temp);LoRa.print(temp);
}
//GPS=============================================================================================

void gen_lat_long(){
  float minLatitude = -90.0;
  float maxLatitude = 90.0;
  float latitude = random(minLatitude * 1000, (maxLatitude + 1) * 1000) / 1000.0;

  float minLongitude = -180.0;
  float maxLongitude = 180.0;
  float longitude = random(minLongitude * 1000, (maxLongitude + 1) * 1000) / 1000.0;
  Serial.print(latitude);LoRa.print(latitude);
  Serial.print(",");LoRa.print(",");
  Serial.print(longitude);LoRa.print(longitude);
}

void gen_GPS_alt(){
  float alt = random(0, 100000) / 10.0;
  Serial.print(alt, 3);LoRa.print(alt, 3);
}

void gen_GPS_speed(){
  float minSpeed = 0.0;
  float maxSpeed = 1000.0;
  float speed = random(minSpeed, (maxSpeed + 1) * 100) / 10.0;
  Serial.print(speed, 3);LoRa.print(speed, 3);
}

void gen_GPS_heading(){
  Serial.print("gps_HEADING");LoRa.print("gps_HEADING");
}

void gen_GPS_time(){
  Serial.print("hh:mm:ss");LoRa.print("hh:mm:ss");
}

void gen_GPS_date(){
  Serial.print("dd/mm/yyyy");LoRa.print("dd/mm/yyyy");
}

void gen_GPS_SATS(){
  int sats = random(0, 30);
  Serial.print(sats);LoRa.print(sats);
}
//IMU====================================================================================================================

void gen_acc(){
  float min = -10.0;
  float max = 10.0;

  float ax = random(min * 1000, (max + 1) * 1000) / 1000.0;
  float ay = random(min * 1000, (max + 1) * 1000) / 1000.0;
  float az = random(min * 1000, (max + 1) * 1000) / 1000.0;

  Serial.print(ax);LoRa.print(ax);
  Serial.print(",");LoRa.print(",");
  Serial.print(ay);LoRa.print(ay);
  Serial.print(",");LoRa.print(",");
  Serial.print(az);LoRa.print(az);
}

void gen_gyro(){
  float min = -10.0;
  float max = 30.0;

  float gx = random(min * 1000, (max + 1) * 1000) / 1000.0;
  float gy = random(min * 1000, (max + 1) * 1000) / 1000.0;
  float gz = random(min * 1000, (max + 1) * 1000) / 1000.0;

  Serial.print(gx);LoRa.print(gx);
  Serial.print(",");LoRa.print(",");
  Serial.print(gy);LoRa.print(gy);
  Serial.print(",");LoRa.print(",");
  Serial.print(gz);LoRa.print(gz);
}
//MISC.=============================================================================

void gen_velocity(){
  float minSpeed = 0.0;
  float maxSpeed = 1000.0;
  float speed = random(minSpeed, (maxSpeed + 1) * 100) / 10.0;
  Serial.print(speed, 3);LoRa.print(speed,3);
}

void gen_pitch_yaw_roll(){
  float min = -180.0;
  float max = 180.0;

  float pitch = random(min * 1000, (max + 1) * 1000) / 1000.0;
  float yaw = random(min * 1000, (max + 1) * 1000) / 1000.0;
  float roll = random(min * 1000, (max + 1) * 1000) / 1000.0;

  Serial.print(pitch);LoRa.print(pitch);
  Serial.print(",");LoRa.print(",");
  Serial.print(roll);LoRa.print(roll);
  Serial.print(",");LoRa.print(",");
  Serial.print(yaw);LoRa.print(yaw);
}

void gen_magnetometer_heading(){
  Serial.print("magnetometer heading");LoRa.print("magnetometer heading");
}

void gen_volt(){
  float min = 0.0;
  float max = 5.0;

  float voltage = random(min * 1000, (max + 1) * 1000) / 1000.0;

  Serial.print(voltage);LoRa.print(voltage);
}

void gen_flight_state(){
  float min = 0;
  float max = 4;
  float state = random(min, max);
  Serial.print(state);LoRa.print(state);
}

void gen_trigger(){
  Serial.print("0000");LoRa.print("0000");
}

void gen_RSSI(){
  float minSpeed = 0.0;
  float maxSpeed = 1000.0;
  float speed = random(minSpeed, (maxSpeed + 1) * 100) / 10.0;
  Serial.println(speed, 3);LoRa.println(speed, 3);
}
