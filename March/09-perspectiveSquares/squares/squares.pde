//inspiration http://openprocessing.org/sketch/48671 
float rectWidth, rectHeight;
 
void setup()  {
  size(400,400);
  rectMode(CENTER);
  rectWidth = rectHeight = width;
  noFill();
  stroke(255, 20);
  background(0);
  
  for(int i = 0; i< 10; i++){
    folia();
  }
}
 
void draw()  {
  
}
 
void folia()  {
  rect(width/2, height/2, rectWidth, rectHeight);
  rectWidth = rectWidth/1.5;
  rectHeight = rectHeight/1.5;
  if (rectWidth > 10)  {
    folia();
  }
     
  println(rectWidth);
}