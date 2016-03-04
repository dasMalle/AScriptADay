float mx;
float my;

void setup(){
    size(800,800);
    background(0,200,200);
    
}

void draw(){
  clear();
    noFill();
    stroke(255);
    strokeWeight(20);
    ellipse(250,250,400,400);
    smooth();  
    float mx = constrain(mouseX,190,300);
    float my = constrain(mouseY,190,300);
    fill(255);
    ellipse(mx,my,190,190);
   

}