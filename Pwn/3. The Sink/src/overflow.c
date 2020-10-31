#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    
    long number = 0;
    char input[200];
    
    printf("\n\nCan you drown in a sink?\n");
    printf("And how do you do it?\n");
    
    gets(input);
    
    if(number != 0)
        system("/bin/sh");
}
