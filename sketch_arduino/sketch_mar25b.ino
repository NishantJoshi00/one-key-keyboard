void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(8, INPUT);
  pinMode(9, OUTPUT);
}
int stat;
void loop() {
  // put your main code here, to run repeatedly:n
  stat = digitalRead(8);
  Serial.print(!stat);
  if (stat == 0) {
    digitalWrite(9, HIGH);
  } else {
    digitalWrite(9, LOW);
  }
  delay(10);
}
