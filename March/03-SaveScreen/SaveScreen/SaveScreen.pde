void setup(){
  size(200, 200);
}

void draw(){
  background(155);
  line(0,0, mouseX, height);
  line(width, 0, 0, mouseY);
}

void mousePressed(){
  save("cross.tif");
}