#include <stdio.h>
#include <string.h>

void enter_pass(char* qnumber, char* correct)
{
    char guess[31];
    while (1) {
        printf("Enter %s passphrase: \n", qnumber);
        scanf("%30s", guess);
        if (strcmp(correct, guess) == 0) { // equal = 0
            printf("%s is correct!\n", correct);
            break;
        } else {
            printf("not correct \n");
        }
    }
}

int main(int argc, char** argv)
{
    // TODO, maybe use a better flag
    char* pass1 = "skeletons";
    char* pass2 = "party";
    char* pass3 = "forever";

    enter_pass("first", pass1);
    enter_pass("second", pass2);
    enter_pass("third", pass3);

    printf("The flag is UiTHack20{%s_%s_%s}", pass1, pass2, pass3);
}