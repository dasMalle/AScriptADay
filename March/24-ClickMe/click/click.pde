void setup(){
  size(600, 600);
  background(48, 145, 56);
  textSize(32);
  text("click me", 10, 30); 
}

void draw(){
 
}

void mouseClicked(){
  background(48, 145, 56);
  textSize(32);
  text("Click me", (mouseX + 50) % width, (mouseY+30) % height); 
}