#include<stdio.h>
int main(int argc, char *argv[]){
	execlp("python", "python", "D:/sabreys_cmd/getliste.py", argv[1], (char*) NULL);
	return 0;
}

