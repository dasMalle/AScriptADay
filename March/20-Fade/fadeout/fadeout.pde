//https://amnonp5.wordpress.com/2012/01/28/25-life-saving-tips-for-processing/
void setup() {
  size(500, 500);
  noStroke();
  smooth();
}
 
void draw() {
  fill(255, 10); // semi-transparent white
  rect(0, 0, width, height);
 
  fill(27, 68, 150);
  ellipse(mouseX, mouseY, 100, 100);
}