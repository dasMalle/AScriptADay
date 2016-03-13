int xspacing = 16;   // How far apart should each horizontal location be spaced
int w;              // Width of entire wave

float theta = 0.0;  // Start angle at 0
float amplitude = 125.0;  // Height of wave
float period = 500.0;  // How many pixels before the wave repeats
float dx;  // Value for incrementing X, a function of period and xspacing
float[] yvalues;  // Using an array to store height values for the wave
int cooldown = 4;
int cdStart;
color k;
int barWidth = 5;
int lastBar = -1;

void setup(){
   colorMode(HSB, width, height, 100);
  size(600, 300);
  background(15, 15, 89);
  w = width+16;
  dx = (TWO_PI / period) * xspacing;
  yvalues = new float[w/xspacing];
  cdStart = second();
  w = 255;
}

void draw(){

  if(second() > cdStart+cooldown){
    //background(15, 15, 89);
    cdStart = second();
    //amplitude += 5;
  }     
  calcWave();
  renderWave(k);
  
}

void mouseClicked(){
  int whichBar = mouseX / barWidth;
  if (whichBar != lastBar) {
    int barX = whichBar * barWidth;
    k = color(barX, mouseY, 66);
  }
}

void calcWave() {
  // Increment theta (try different values for 'angular velocity' here
  theta += 0.02;

  // For every x value, calculate a y value with sine function
  float x = theta;
  for (int i = 0; i < yvalues.length; i++) {
    yvalues[i] = sin(x)*amplitude;
    x+=dx;
  }
}

void renderWave(color c) {
  noStroke();
  fill(c);
  // A simple way to draw the wave with an ellipse at each location
  for (int x = 0; x < yvalues.length; x++) {
    ellipse(x*xspacing, height/2+yvalues[x], 16, 16);
  }
}