#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{
    printf("*=====================================================*\n");
    printf("|                    Login UiTHack20                  |\n");
    printf("*=====================================================*\n");
    
    char username[50];
    char password[100];
    
    printf("Username: ");
    scanf("%s", username);
    printf("Password: ");
    scanf("%s", password);
    
    if (!strcmp(username, "UiTHack20"))
        {
            if (!strcmp(password, "When_the_music_stops"))
            {
                printf("Access Granted\n");
                char s[40] = "_dont_look_in_the_mirror_behind_you";
                printf("UiTHack20{%s%s}\n", password, s);
            }
            else
            {
                printf("Access Denied\n");
                printf("Wrong Password\n");
            }
        }
        else
        {
            printf("Access Denied\n");
            printf("Wrong Username\n");
        }
        
    return 0;
}
