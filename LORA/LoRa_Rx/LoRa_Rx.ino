#include <SPI.h>
#include <Wire.h>
#include <LoRa.h>
//#include <Adafruit_GFX.h>
//#include <Adafruit_SSD1306.h>
//
//#define SCREEN_WIDTH 128
//#define SCREEN_HEIGHT 64
//#define OLED_RESET     -1
//#define SCREEN_ADDRESS 0x3c
//
//Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
//


void setup() {
  Serial.begin(115200);
  while (!Serial);
  LoRa.setGain(6);
  LoRa.setPins(5,32,33);

  Serial.println("LoRa Receiver");

  if (!LoRa.begin(915E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);  
  }
  
//  LoRa.setSyncWord(0xF3);
//  display.clearDisplay();
//  display.setTextSize(1);      // Normal 1:1 pixel scale
//  display.setTextColor(SSD1306_WHITE); // Draw white text
//  display.setCursor(0, 0);     // Start at top-left corner
//  display.cp437(true);         // Use full 256 char 'Code Page 437' font

  
}

void loop() {
  // try to parse packet
  int packetSize = LoRa.parsePacket();

  
  if (packetSize) {
    // received a packet
    //Serial.print("");
                                            // read packet
    while (LoRa.available()) {
      Serial.print((char)LoRa.read());
    }
    // Serial.println();
    // print RSSI of packet
    // Serial.print(",RSSI:");
    Serial.println(LoRa.packetRssi());
    //display.print(LoRa.packetRssi());
    //display.display();
  }
}
