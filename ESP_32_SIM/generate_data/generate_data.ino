int packetCounter = 0;

void setup(){
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  generate_data();
}

/* data packet format:-
pkt, RTC->(hh:mm:ss), ALTIMETER->(alt, pressure, temp), GPS->(lat, long, alt, speed, HEADING, GPS_time, GPS_date, GPS_sats), IMU->(ax, ay, az, gx, gy, gz), velocity, pitch, yaw, roll, magnetometer heading, voltage, flight state, RSSI
*/
void generate_data(){
  packetCounter++;
  Serial.print("A,");
  Serial.println(packetCounter);

  gen_time();

  //ALTIMETER--------
  gen_alt();
  gen_press();
  gen_temp();
  //GPS--------------
  gen_lat_long();
  gen_GPS_alt();
  gen_GPS_speed();
  gen_GPS_heading();
  gen_GPS_time();
  gen_GPS_date();
  gen_GPS_SATS();
  //IMU--------------
  gen_acc();
  gen_gyro();
  //MISC.-------------
  gen_velocity();
  gen_pitch_yaw_roll();
  gen_magnetometer_heading(); 
  gen_volt();
  gen_flight_state();
  gen_trigger();
  gen_RSSI();
}

void gen_time(){
  Serial.print("B,");
  Serial.println("hh:mm:ss");
}

//ALTIMETER=========================================================================================================

void gen_alt(){
  float alt = random(0, 100000) / 10.0;
  Serial.print("C,");
  Serial.println(alt, 3);
}

void gen_press(){
  float pressure = random(0, 100000) / 10.0;
  Serial.print("D,");
  Serial.println(pressure, 3);
}

void gen_temp(){
  float minTemp = 20.0;
  float maxTemp = 30.0;
  float temp = random(minTemp * 10, (maxTemp + 1) * 10) / 10.0;
  Serial.print("E,");
  Serial.println(temp);
}
//GPS=============================================================================================

void gen_lat_long(){
  float minLatitude = -90.0;
  float maxLatitude = 90.0;
  float latitude = random(minLatitude * 1000, (maxLatitude + 1) * 1000) / 1000.0;

  float minLongitude = -180.0;
  float maxLongitude = 180.0;
  float longitude = random(minLongitude * 1000, (maxLongitude + 1) * 1000) / 1000.0;
  Serial.print("F,");
  Serial.println(latitude);
  // Serial.print(",");
  Serial.print("G,");
  Serial.println(longitude);
}

void gen_GPS_alt(){
  float alt = random(0, 100000) / 10.0;
  Serial.print("H,");
  Serial.println(alt, 3);
}

void gen_GPS_speed(){
  float minSpeed = 0.0;
  float maxSpeed = 1000.0;
  float speed = random(minSpeed, (maxSpeed + 1) * 100) / 10.0;
  Serial.print("I,");
  Serial.println(speed, 3);
}

void gen_GPS_heading(){
  int min = 0;
  int max = 360;

  int pitch = random(min, max + 1);
  Serial.print("J,");
  Serial.println(pitch);
}

void gen_GPS_time(){
  Serial.print("K,");
  Serial.println("hh:mm:ss");
}

void gen_GPS_date(){
  Serial.print("L,");
  Serial.println("dd/mm/yyyy");
}

void gen_GPS_SATS(){
  Serial.print("M,");
  int sats = random(0, 30);
  Serial.println(sats);
}
//IMU====================================================================================================================

void gen_acc(){
  float min = -10.0;
  float max = 10.0;

  float ax = random(min * 1000, (max + 1) * 1000) / 1000.0;
  float ay = random(min * 1000, (max + 1) * 1000) / 1000.0;
  float az = random(min * 1000, (max + 1) * 1000) / 1000.0;
  Serial.print("N,");
  Serial.println(ax);
  Serial.print("O,");
  Serial.println(ay);
  Serial.print("P,");
  Serial.println(az);
}

void gen_gyro(){
  float min = -10.0;
  float max = 30.0;

  float gx = random(min * 1000, (max + 1) * 1000) / 1000.0;
  float gy = random(min * 1000, (max + 1) * 1000) / 1000.0;
  float gz = random(min * 1000, (max + 1) * 1000) / 1000.0;
  Serial.print("Q,");
  Serial.println(gx);
  Serial.print("R,");
  Serial.println(gy);
  Serial.print("S,");
  Serial.println(gz);
}
//MISC.=============================================================================

void gen_velocity(){
  float minSpeed = 0.0;
  float maxSpeed = 1000.0;
  float speed = random(minSpeed, (maxSpeed + 1) * 100) / 10.0;
  Serial.print("T,");
  Serial.println(speed, 3);
}

void gen_pitch_yaw_roll(){
  float min = -180.0;
  float max = 180.0;

  float pitch = random(min * 1000, (max + 1) * 1000) / 1000.0;
  float yaw = random(min * 1000, (max + 1) * 1000) / 1000.0;
  float roll = random(min * 1000, (max + 1) * 1000) / 1000.0;
  Serial.print("U,");
  Serial.println(pitch);
  Serial.print("V,");
  Serial.println(yaw);
  Serial.print("W,");
  Serial.println(roll);
}

void gen_magnetometer_heading(){
  int min = 0;
  int max = 360;

  int pitch = random(min, max + 1);
  Serial.print("X,");
  Serial.println(pitch);
}

void gen_volt(){
  float min = 0.0;
  float max = 5.0;

  float voltage = random(min * 1000, (max + 1) * 1000) / 1000.0;
  Serial.print("Y,");
  Serial.println(voltage);
}

void gen_flight_state(){
  float min = 0;
  float max = 4;
  float state = random(min, max);
  Serial.print("Z,");
  Serial.println(state);
}

void gen_trigger(){
  Serial.print("AB,");
  Serial.println("0011");
}

void gen_RSSI(){
  int minSpeed = -120;
  int maxSpeed = 0;
  int speed = random(minSpeed, maxSpeed + 1);
  Serial.print("BC,");
  Serial.println(speed);
}