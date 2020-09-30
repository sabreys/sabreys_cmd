#include<stdio.h>
#include <sys/stat.h>
#include <stdlib.h>  
#include<string.h>
#include "windows.h"
int is_exist(const char* filename);

int main(int argc, char *argv[]){
	
	
if(argc!=2){
	printf("wrong call. create_file file_name.extention  ");
	return -1;
}

if(is_exist(argv[1])){
	printf("file exist.");
	return -1;
	
}

FILE *fp; 
fp=fopen(argv[1],"w"); 
fclose(fp); 
printf("file created.");


ShellExecute(GetDesktopWindow(), "open", argv[1], NULL, NULL, SW_SHOWNORMAL);

    
	
	
	return 0;
}



int is_exist(const char* filename){
    struct stat buffer;
    int exist = stat(filename,&buffer);
    if(exist == 0)
        return 1;
    else // -1
        return 0;
}
