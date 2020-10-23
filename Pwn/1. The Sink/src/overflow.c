#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
    long number = 0;
    char input[16];
    
    printf("Welcome to UiTHack2020, the sink is overflowing\n");
    printf("What do you want to do?\n");
    
    gets(input);
    
    if(number != 0)
        system("/bin/sh");
}
