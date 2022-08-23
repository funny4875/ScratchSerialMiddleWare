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
  保留下列通訊埠
  A4: SDA
  A5: SCL
  D2 D3: interrupt 0,1
  D10~D13: SPI
  */
  //PWM for analogWrite
  pinMode(D5, OUTPUT);
  pinMode(D6, OUTPUT);
  pinMode(D9, OUTPUT);
  //port for digitalWrite
  pinMode(D7, OUTPUT);
  pinMode(D8, OUTPUT);
  Serial.begin(9600);
  for(i=0;i<2;i++){analogWrite(D13,255);delay(500);analogWrite(D13,0); delay(500);}
}
int tag;
unsigned char buf[10];
int len;
void loop()
{
  delay(50);
  if(Serial.available())
  {
    tag = Serial.read();    
    if (tag == 0x49)
    {
        if(Serial.readBytes(buf,1)>0)
        {
          //寫入類比埠(PWM)
          len = buf[0];
          Serial.readBytes(buf,len);
          for(i=0;i<len;i+=2)
            analogWrite(buf[i],buf[i+1]);
            
          /*讀取類比埠 A0~A3 及 數位埠D4
           * analogRead() 預設輸出為 0~1023 之 int
           * 為控制輸入為 unsigned char(8bit) 0~255
           * 將讀到之結果除以4(向右平移2位元)
           */
          buf[0]=analogRead(A0)>>2;
          buf[1]=analogRead(A1)>>2;
          buf[2]=analogRead(A2)>>2;
          buf[3]=analogRead(A3)>>2;
          buf[4]=digitalRead(D4);
          
          //將Arduino上類比埠 A0~A3 及 數位埠D4之內容寫到序列埠中
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
