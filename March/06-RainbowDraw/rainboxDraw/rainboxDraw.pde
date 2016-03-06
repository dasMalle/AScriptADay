 
ArrayList history = new ArrayList();
float distthresh = 60;
 
void setup(){
  size(900,600);
  colorMode(HSB, width, height, 100);
  background(255);
  stroke(0,50);
  smooth();
}
 
 
 int barWidth = 5;
int lastBar = -1;

void draw(){
   
}
 
void mouseDragged(){
 int whichBar = mouseX / barWidth;
  if (whichBar != lastBar) {
    int barX = whichBar * barWidth;
    stroke(barX, mouseY, 66);
  PVector d = new PVector(mouseX,mouseY,0);
  history.add(0,d);
   
  for (int p=0; p<history.size(); p++){
    PVector v = (PVector) history.get(p);
    float joinchance = p/history.size() + d.dist(v)/distthresh;
    if (joinchance < random(0.4))  line(d.x,d.y,v.x,v.y);
  }
}
}
 
void keyPressed(){
  if (key == ' ') {
    background(255);
    history.clear();
  }
}