void setup() {
  size(300, 200);
  background(255);
  smooth();
  
  rectMode(CENTER); // show bounding boxes
  stroke(128);
  rect(35, 50, 50, 50);
  
  
}

void draw(){
stroke(128);
rect( mouseX, mouseY,5, 10);
}