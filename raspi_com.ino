int r;
int batteryPin = A0;  
float batteryVoltage;
 
void setup() {  
  Serial.begin(9600);  
} 
 
void loop() 
{  
    if(Serial.available())
    {
      raspi_com();
    }      
}
   
void raspi_com()
  {            
      //r =(Serial.read() - '0');  //conveting the value of chars to integer
      r = Serial.readString().toInt();
      //Serial.println(r);       
      if (r==1) //request parking info
      {
        Serial.println("{"Parking 1": "0", "Parking 2": "0", "Parking 3": "0", "Parking 4": "0"}"); 
      }      
      if (r==2) //request batteryVoltage
      {                  
        batteryVoltage= analogRead(batteryPin) * (5.0 / 1023.0);
        Serial.println(batteryVoltage,DEC);   
      }       
      
}
