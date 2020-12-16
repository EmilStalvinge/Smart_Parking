
void setup() {
Serial.begin(9600);              //Starting serial communication
}
  
void loop() {  
  Serial.println("1 Unavaliable Avaliable Unavaliable Avaliable");   // send the data
  delay(10000);               
  Serial.println("2 Unavaliable Unvaliable Unavaliable Avaliable");   // send the data
  delay(10000);
  Serial.println("1 Unavaliable Unavaliable Unavaliable Avaliable");   // send the data
  delay(10000);               
  Serial.println("2 Unavaliable Unvaliable Unavaliable Unvaliable");   // send the data
  delay(10000);
  Serial.println("1 Unavaliable Unavaliable Unavaliable Unvaliable");   // send the data
  delay(10000); 
  
}
