#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
    long number = 0;
    char input[200];
    
    printf("\n\nCan you drown in a sink?\n");
    printf("And how do you do it?\n");
    
    gets(input);
    
    if(number != 0)
        system("/bin/sh");
}
