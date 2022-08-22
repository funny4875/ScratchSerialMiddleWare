// C++ code
//
#define D2 2
#define D3 3

#define D4 4
#define D5 5
#define D6 6
#define D7 7
#define D8 8
#define D9 9
#define D10 10
#define D13 13
int i;
void setup()
{
  analogReference (DEFAULT);
  //for analogRead
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  //port for digitalRead
  pinMode(D4, INPUT_PULLUP);
  
  
  /*
  A4: SDA
  A5: SCL
  D2 D3: interrupt 0,1
  D10~D13: SPI
  */
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D10, OUTPUT);
  digitalWrite(D2,LOW);
  digitalWrite(D3,LOW);
  digitalWrite(D10,LOW);
  //PWM for analogWrite
  pinMode(D5, OUTPUT);
  pinMode(D6, OUTPUT);
  pinMode(D9, OUTPUT);
  //port for digitalWrite
  pinMode(D7, OUTPUT);
  pinMode(D8, OUTPUT);
  pinMode(D9, OUTPUT);
  /*
  digitalWrite(A0,HIGH);
  digitalWrite(A1,HIGH);
  digitalWrite(A2,HIGH);
  digitalWrite(A3,HIGH);
  */
  Serial.begin(9600);
  //analogWrite(D7,0xF0);
  for(i=0;i<2;i++){analogWrite(D13,255);delay(500);analogWrite(D13,0); delay(500);}
}
int tag;
unsigned char buf[10];
//int d5,d6,d9,d7,d8,d13;
//int myPins[] = {5, 6, 9 7, 8,9};
int len;
void loop()
{
  
  //Serial.println(analogRead(A1)>>2);
  delay(50);
  if(Serial.available())
  {
    tag = Serial.read();    
    if (tag == 0x49)
    {
        if(Serial.readBytes(buf,1)>0)
        {
          len = buf[0];
          Serial.readBytes(buf,len);
          for(i=0;i<len;i+=2)
            analogWrite(buf[i],buf[i+1]);
          
          buf[0]=analogRead(A0)>>2;
          buf[1]=analogRead(A1)>>2;
          buf[2]=analogRead(A2)>>2;
          buf[3]=analogRead(A3)>>2;
          buf[4]=digitalRead(D4);
          
          Serial.write(buf,5);
          Serial.flush();
        }        
    }
    
  }

  /*
  Serial.println(analogRead(A0));
  Serial.println(analogRead(A1));
  Serial.println(analogRead(A2));
  Serial.println(analogRead(A3));
  delay(100);
  int a = Serial.read();
  if(a >= 0) analogWrite(10,a);
  else digitalWrite(10,LOW);*/
}
