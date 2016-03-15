String imagepath;
PImage img;
PImage brand;
int margin;

void setup(){
  size(1200, 1200);
  selectInput("Select a file to process:", "fileSelected");
  brand = loadImage("eyes.png");
  
}

void fileSelected(File selection) {
  if (selection == null) {
    println("Window was closed or the user hit cancel.");
  } else {
    println("User selected " + selection.getAbsolutePath());
    imagepath = selection.getPath();
    img = loadImage(imagepath);
    println("done");
  }
}

void draw(){
  if(img!= null){
    /* //size(i.width, i.height); 
     imageMode(CENTER);
     image(i, i.width/2 , i.height/2); //center image
     i.resize(0, height/2); //make it smaller
     
     image(brand, i.width- brand.width/2 -10, i.height-brand.height/2 -10);
     i.save("branded.jpg");*/
     
     PImage branded = createImage(img.width, img.height, RGB);
     branded.loadPixels();
     img.loadPixels();
     brand.loadPixels();
     
     for(int i = 0; i < branded.pixels.length; i++){
       branded.pixels[i] = img.pixels[i];
     }
     branded.updatePixels();
     for(int j = 0; j<branded.pixels.length; j++){
       branded.pixels[j] = brand.pixels[j];
     }
     //println("brand pixels:"+ brand.pixels.length);
     branded.updatePixels();
     image(branded, 0, 0);
     
  }
}