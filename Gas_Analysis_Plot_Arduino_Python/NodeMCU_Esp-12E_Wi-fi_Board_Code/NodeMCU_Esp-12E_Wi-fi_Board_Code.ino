#include <Blynk.h>
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>
#define BLYNK_PRINT Serial
BlynkTimer timer;

/* Fill-in your Template ID (only if using Blynk.Cloud) */
//#define BLYNK_TEMPLATE_ID   "YourTemplateID"
#define BLYNK_TEMPLATE_ID "TMPLcMsLPHR1"
#define BLYNK_DEVICE_NAME "GAS MONITORING"
#define BLYNK_AUTH_TOKEN "fxx-gdOJV2R7DuCrMgl-H-9I8YeHdyRS"


// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = BLYNK_AUTH_TOKEN;

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "hiii";
char pass[] = "123456789";

int mq2 = A0; // smoke sensor is connected with the analog pin A0 
int data = 0;

void setup()
{
  // Debug consolew
  Serial.begin(115200);
  timer.setInterval(1000L, getSendData);
  Blynk.begin(auth, ssid, pass,"blynk.cloud",80);
}

void loop()
{
  timer.run();
  Blynk.run();
}
void getSendData()
{
data = analogRead(mq2); 
Serial.println(data);
  Blynk.virtualWrite(V2, data);
 
  if (data > 200 )
  {
    Blynk.notify("Smoke Detected!"); 
  }
 
}
