># Haunted house
>> Rev_eng - 50 pts
>
>You find yourself in an old haunted house. To advance to the next room you need to enter a passphrase based on a challenge infront of you. <br>
>There are 3 steps, each with a unique passphrase.
>
>Good luck.

## Writeup 

folder -> Haunted_house \
The program prompts the user for a series of answers, which combine into the flag. <br>
Instead the flag can be found by reading the binary with xxd or strings, and looking for strings related to the theme. <br>
FLAG: `UiTHack20{skeletons_party_forever}`