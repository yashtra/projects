//currently can only handle a single path gets confused on order of solving 

#include<iostream>
using namespace std;


void print(char grid[5][5]){
    for(int r=0;r<5;r++){
for (int c=0;c<5;c++){
    cout<<grid[r][c]<<" ";
}cout<<endl;
}

}


bool reached(int row, int col){
    if(row==4 && col==4){  // end coordinates
        return true;
    }

    return false;
}

bool solvemaze(char (&grid)[5][5] , int row , int col ){int c=0;
  // base 
    if(reached(row ,col)){
        grid[row][col]='1';
        return true;
    }

grid[row][col]='1';  //set

    //move 
// check up 


    if(grid[row-1][col]=='0'){
    

       if(!solvemaze(grid , row-1,col)){c++;}
        
     
    }else c++;


// check down 


    if(grid[row+1][col]=='0'){     
       if(!solvemaze(grid , row+1, col)){c++;}

    }else {c++;}


// check right


    if(grid[row][col+1]=='0'){
      if(!solvemaze(grid , row, col+1)){
        c++;
      }
        

    }else c++;


// check left 


    if(grid[row][col-1]=='0'){ 
      if(!solvemaze(grid , row, col-1)){c++;}

    }else c++;


if(c<4){
    return true;
}

else {
    grid[row][col]='0';
    return false;
}


}

int main(){
//driver 

char arr[5][5];
for(int r=0;r<5;r++){
for (int c=0;c<5;c++){
    cin>>arr[r][c];
}
}

solvemaze(arr , 0 , 0 ); //starting coordinates
print(arr);



}