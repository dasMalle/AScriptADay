

void setup(){
  size(600, 600); 
  background(255);
}

void draw(){
  
  //ellipse(mouseX, mouseY, 70 % second(), 70 % second());
  
 int var =  second() % 6; 
 
 for(int i = 1; i <= var; i++){
   fill((int)second()*4.25, (int) minute() * 4.25, 60);
   translate(30 *i, 20*i);
   ellipse(mouseX, mouseY, 10, 10);
 }
  
  
  

}