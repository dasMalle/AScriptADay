//https://amnonp5.wordpress.com/2012/01/28/25-life-saving-tips-for-processing/

void setup() {
  size(500, 500);
  noStroke();
  smooth();
}
 
void draw() {
  background(255);
 
  int rX = 40;
  int rY = 60;
  int rW = 150;
  int rH = 170;
  if (mouseOverRect(rX, rY, rW, rH)) { fill(0, 0, 255); }
  else { fill(255, 0, 0); }
  rect(rX, rY, rW, rH);
 
  int cX = 340;
  int cY = 280;
  float cD = 250;
  if (mouseOverCircle(cX, cY, cD)) { fill(0, 255, 0); }
  else { fill(255, 0, 0); }
  ellipse(cX, cY, cD, cD);
}
 
boolean mouseOverCircle(int x, int y, float diameter) {
  return (dist(mouseX, mouseY, x, y) < diameter*0.5);
}
 
boolean mouseOverRect(int x, int y, int w, int h) {
  return (mouseX >= x && mouseX <= x+w && mouseY >= y && mouseY <= y+h);
}