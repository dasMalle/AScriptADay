void setup(){
  size(600, 600);
  background(200, 180, 240);
}

void draw(){
  fill(second() * 4,mouseX, mouseY);
  rect(mouseX, mouseY, second(), millis() % 100);
}