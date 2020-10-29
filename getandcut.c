#include<stdio.h>
int main(int argc, char *argv[]){
	printf("%s ,%s,%s",argv[1],argv[2],argv[3]);
	execlp("python", "python", "D:/sabreys_cmd/getandcut.py", argv[1],argv[2],argv[3], (char*) NULL);
	return 0;
}

