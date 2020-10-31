># Hall of mirrors
> > Pwn - 150pts
>
>You find yourself in a maze of mirrors, and all you see is the endlessly repeating images of yourself and a terminal. \
>The terminal knows the passphrase to get out, but its not going to give it up willingly. \
>You need to use your LEE7 hacker skills to wrangle the passphrase from it.

>[Terminal](./terminal)

## Writeup

Folder: Hall of Mirrors

The program acts like a simple terminal with limited functionality. 
The terminal echoes any invalid input but if the correct format string is supplied it will output the flag. \
To solve start the terminal with `./terminal` and enter `%s\n` to get the flag.

```
UiTHack20{You_are_lucky_m1rrors_can't_Laugh}
```