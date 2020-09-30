#include<stdio.h>
int main(int argc, char *argv[]){
	execlp("python", "python", "deaes.py", argv[1],argv[2],argv[3], (char*) NULL);
	return 0;
}


