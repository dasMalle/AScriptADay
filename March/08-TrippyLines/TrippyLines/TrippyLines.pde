float time = 0;
float c;
   
void setup() {
  size(400, 400);
  background(255);
  c = random(250);
}
   
void draw() {
  //background(random(255)); //use this for trippy
  background(c);
  stroke(random(255));
  float x = 0;
  while (x < width) {
    line(350  * noise(x / 100, time), x, 500 * noise(0.1 / 100, time), 350 * noise(x / 100, time));
    x += 8;
  }
  time += 0.03;
}