#include<iostream>
using namespace std;

void grid_print(int grid[9][9]){
    for(int r=0;r<9;r++){
        for(int c=0;c<9;c++){
            cout<<grid[r][c]<<" ";

        }cout<<endl;
    }
}

bool issafe(int grid[9][9] , int row , int col , int num){

//check row
for(int c=0; c<9;c++){
if(grid[row][c]==num){
return false;
}
}

//check column
for(int r=0;r<9;r++){
    if(grid[r][col]==num){
        return false;
    }
}

//check the particular grid 
int srow= row-row%3;
int scol = col-col%3;
for(int i=0;i<3;i++){
    for(int j=0;j<3;j++){
       if(grid[srow+i][scol+j]==num){
            return false;
        }
    }
}

return true;

}

bool solvesudoku(int (&grid)[9][9],int row ,int col ){
    if(row>=9){
        return true;
    }

if(col>=9){ 
 solvesudoku(grid,row+1,0);

}
else {

if(grid[row][col]>0){
    solvesudoku(grid , row ,col+1);
    
}
else{
for(int i=1;i<=9;i++){
    if(issafe(grid,row,col,i)){
        
        grid[row][col]=i;
       if(solvesudoku(grid, row,col+1)){/////
        return true;                    /////////good note
       }                                /////
            
        
    }

    grid[row][col]=0;
}

if(grid[row][col]==0){

return false;
}
}

}

}

int main(){

int grid[9][9] = { { 3, 0, 6, 5, 0, 8, 4, 0, 0 },
                       { 5, 2, 0, 0, 0, 0, 0, 0, 0 },
                       { 0, 8, 7, 0, 0, 0, 0, 3, 1 },
                       { 0, 0, 3, 0, 1, 0, 0, 8, 0 },
                       { 9, 0, 0, 8, 6, 3, 0, 0, 5 },
                       { 0, 5, 0, 0, 9, 0, 6, 0, 0 },
                       { 1, 3, 0, 0, 0, 0, 2, 5, 0 },
                       { 0, 0, 0, 0, 0, 0, 0, 7, 4 },
                       { 0, 0, 5, 2, 0, 6, 3, 0, 0 } };


//   for(int r=0;r<9;r++){
//         for(int c=0;c<9;c++){
//             cin>>grid[r][c];

//         }
//     }


solvesudoku(grid , 0,0);
grid_print(grid);



}