// Learning Processing
// Daniel Shiffman
// http://www.learningprocessing.com

float r = 0;
float theta = 0;

void setup() {
  size(480, 270);
  background(255);
}

void draw() {
  // Polar to Cartesian conversion
  float x = r * cos(theta);
  float y = r * sin(theta);

  // Draw an ellipse at x,y
  noStroke();
  fill(0);
  // Adjust for center of window
  ellipse(x+width/2, y+height/2, 16, 16); 

  // Increment the angle
  theta += 0.1;
  // Increment the radius
  r += 0.5;
  
  rect(x, y, 16, 16);
}