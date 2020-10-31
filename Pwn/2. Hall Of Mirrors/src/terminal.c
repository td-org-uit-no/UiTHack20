#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    char buffer[256] = { 0 };

    //flag obfuscation
    char flag[] = {
        'N',
        'b',
        'M',
        'A',
        'Z',
        '\\',
        'd',
        '+',
        ')',
        't',
        'R',
        'h',
        'n',
        'X',
        'Z',
        'k',
        '^',
        'X',
        'e',
        'n',
        '\\',
        'd',
        'r',
        'X',
        'f',
        '*',
        'k',
        'k',
        'h',
        'k',
        'l',
        'X',
        '\\',
        'Z',
        'g',
        ' ',
        'm',
        'X',
        'E',
        'Z',
        'n',
        '`',
        'a',
        'v',
    };

    for (int i = 0; i < strlen(flag); i++) {
        flag[i] = flag[i] + 7;
    }

    
    while (1) {

        printf("> ");
        if (!fgets(buffer, sizeof(buffer), stdin)) {
            perror("fgets failure\n");
            exit(EXIT_FAILURE);
        }

        //terminal simulation for misdirection
        if (strcmp(buffer, "ls\n") == 0) {
            printf("  dispair.txt  flag.txt\n");
        } else if (strcmp(buffer, "ls -a\n") == 0) {
            printf("  ./  ../  dispair.txt  flag.txt\n");
        } else if (strcmp(buffer, "ls -la\n") == 0) {
            printf("  ./\n  ../\n  dispair.txt\n  flag.txt\n");
        } else if (strcmp(buffer, "cat dispair.txt\n") == 0) {
            printf("  There is no way out, send help. Please... \n");
        } else if (strcmp(buffer, "cat flag.txt\n") == 0) {
            printf("  Sooner or later you’re going to realize, just as I did, there’s a difference between knowing the path and walking the path. \n");
        } else if (strcmp(buffer, "exit\n") == 0 || strcmp(buffer, "q\n") == 0) {
            exit(0);
        } else {
            printf(buffer, flag);
        }
    }
}