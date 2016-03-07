// Set up dimensions
size(200, 200);
int cols = width;
int rows = height;

// Declare 2D array
int[][] myArray = new int[cols][rows];

// Initialize 2D array values
for (int i = 0; i < cols; i ++ ) {
  for (int j = 0; j < rows; j ++ ) {
    myArray[i][j] = int(i * j/ 255);
  }
}

// Draw points
for (int i = 0; i < cols; i ++ ) {
  for (int j = 0; j < rows; j ++ ) {
    stroke(myArray[i][j], i, j);    
    point(i, j);
  }
}