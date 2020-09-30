
#include<stdio.h>
#include<string.h>
#define LENGTH 256

int main(int argc, char *argv[]){
 printf("write key:");
 char pass[LENGTH];
 scanf("%s",pass);
 printf("write key file name:");
 char* c[LENGTH];
 scanf("%s",c);
 execlp("python", "python", "D:/sabreys_cmd/deaes.py", argv[1],pass,c, (char*) NULL);
 return 0;
}

