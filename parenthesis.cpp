#include<iostream>
using namespace std;

struct stack {
   int top;
   char * arr;
   int size;
};

bool is_matching(struct stack *ptr  , char b){
    if(ptr->arr[ptr->top]=='{' && b=='}'){ return 1;}
       
    if(ptr->arr[ptr->top]=='(' && b==')'){ return 1; }
       
    if(ptr->arr[ptr->top]=='[' && b==']'){ return 1;}
     
    return 0;

}




bool isfull(struct stack * ptr){
    if(ptr->top==ptr->size){
        cout<<ptr->arr[ptr->top]<<endl;
        return 1;
    }
    return 0;
}

bool isempty(struct stack * ptr){
    if(ptr->top==-1){
        return 1;
    }
    return 0;
}

bool pop(struct stack * ptr)
 {  if(isempty(ptr)){
    cout<<"stack underflow"<<endl;
    return 0;
}
   
    ptr->top--;
    
    return 1;
}

bool push(char a,struct stack * ptr){
if(isfull(ptr)){
    cout<<"stack overflowed"<<endl;
    return 0;
}
ptr->top++;
ptr->arr[ptr->top]= a;
      
return 1;
}

bool parethesismatching(char* exp)
{
 struct stack *s=new stack();
 s->size =100;
 s->top=-1;
 s->arr=new char[s->size];

for(int i=0;exp[i]!='\0';i++){
    if(exp[i]=='{' || exp[i]=='(' || exp[i]=='['){
        push(exp[i],s);

    }

else if(exp[i]=='}' || exp[i]==')' || exp[i]==']')
 {   if(isempty(s)){
        return 0;
    }

    if(is_matching(s, exp[i] )){
        pop(s);
     
      
    }
    else {return 0;}

}
}

if(isempty){
    return 1;
}
else{ return 0;}



}


int main(){

char* exp = (char*)"{}}";


if(parethesismatching(exp)){
    cout<<"yes"<<endl;
}

else {
    cout<<"no"<<endl;
}

}