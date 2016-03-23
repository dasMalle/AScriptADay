//http://openprocessing.org/sketch/332807
//still sick and jet lagged, I am getting back to original stuff tomorrow
 
float wNoise, hNoise, tNoise;
float noiseScale = 0.003;
float step = 10;
 
void setup(){
  size(500, 500);
  frameRate(30);
  wNoise = random(1000);
  hNoise = random(1000);
  tNoise = random(1000);
}
 
void draw(){
  background(0);
  stroke(255);
   
  float time = frameCount * 0.02;
  for(int w = 0; w < width; w += step){
    for(int h = 0; h < height; h += step){
      // for javascript mode
      int pNum = int(map(pow(noise(wNoise + w * noiseScale, hNoise + h * noiseScale, tNoise + time), 2), 0.1, 0.9, 0, 20));
      //for java mode
//      int pNum = int(map(pow(noise(wNoise + w * noiseScale, hNoise + h * noiseScale, tNoise + time), 2), 0, 1, 0, 20));
      for(int i = 0; i < pNum; i++){
        float pw = map(random(1), 0, 1, w, w + step);
        float ph = map(random(1), 0, 1, h, h + step);
        point(pw, ph);
      }
    }
  }
}