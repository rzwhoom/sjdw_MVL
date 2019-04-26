//arduino5\8\9控制左电机，6\10\11控制右电机

long unsigned nowti;
long unsigned passti=0;
byte bt;
int dy=80;
void setup() 
{
Serial.begin(115200);//wifi模块串口波特率
pinMode(8,OUTPUT);
pinMode(9,OUTPUT);
pinMode(5,OUTPUT);//左侧电机
pinMode(10,OUTPUT);
pinMode(11,OUTPUT);
pinMode(6,OUTPUT);//右侧电机
digitalWrite(8,LOW);
digitalWrite(9,LOW);
digitalWrite(5,LOW);
digitalWrite(10,LOW);
digitalWrite(11,LOW);
digitalWrite(6,LOW);
}

void zanting()//暂停
{
  digitalWrite(8,LOW);
  digitalWrite(9,LOW);
  digitalWrite(5,LOW);
  digitalWrite(10,LOW);
  digitalWrite(11,LOW);
  digitalWrite(6,LOW);
}

void qianjin()//前进
{
  digitalWrite(8,LOW);
  digitalWrite(9,HIGH);
  analogWrite(5,dy);
  digitalWrite(10,LOW);
  digitalWrite(11,HIGH);
  analogWrite(6,dy);
}

void sszz()//顺时针转
{
  digitalWrite(8,LOW);
  digitalWrite(9,HIGH);
  analogWrite(5,dy);
  digitalWrite(10,HIGH);
  digitalWrite(11,LOW);
  analogWrite(6,dy);
}

void nszz()//逆时针转
{
  digitalWrite(8,HIGH);
  digitalWrite(9,LOW);
  analogWrite(5,dy);
  digitalWrite(10,LOW);
  digitalWrite(11,HIGH);
  analogWrite(6,dy);
}

void zpz()//左偏转
{
  digitalWrite(8,LOW);
  digitalWrite(9,HIGH);
  analogWrite(5,dy-30);
  digitalWrite(10,LOW);
  digitalWrite(11,HIGH);
  analogWrite(6,dy);
}

void ypz()//右偏转
{
  digitalWrite(8,LOW);
  digitalWrite(9,HIGH);
  analogWrite(5,dy);
  digitalWrite(10,LOW);
  digitalWrite(11,HIGH);
  analogWrite(6,dy-30);
}

void loop() {
nowti = millis();
if (nowti - passti <= 10000)  //10秒无数据则暂停
{
   if (Serial.available())
  {
    passti=nowti;
    bt = Serial.read();
    switch (bt)
    {
      case 'a': qianjin();break;
      case 'b': zanting();break;
      case 'c': sszz();break;
      case 'd': nszz();break;
      case 'e': zpz();break;
      case 'f': ypz();break;
    }
  }
}
else
{
zanting();
passti=nowti;
}
}