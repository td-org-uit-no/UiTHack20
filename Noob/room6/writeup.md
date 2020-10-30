># room6
>> Noob - 300pts
>
>I have a gift for you which is wrapped extra super good for you. And a secret is inside. It's not a baseball.  
>
>To enter the rooms you will need to connect through `ssh`.
>The username for this first room, is `room6`
>The server name is `sparkly-unicorn.td.org.uit.no`.
>The password for room6 is the flag from the `room5` challenge.
>
>
>
>Tips:
>`ssh room6@sparkly-unicorn.td.org.uit.no`
>
>Tips:
>Is something done with this file? How can you undo it? 

## Writeup

This is a folder with the flag that is compressed three times with different algorithms. The flag is also base64 encoded. 
a method for solving this, is copying the flag to the /tmp folder, where the user have write rights, then start to decompress the file.
All of this can be done with these commands:

>cp flag.tar.bz2 /tmp/flag.tar.bz2
>cd /tmp
>bzip2 -d flag.tar.bz2
>tar -xf flag.tar
>tar -xf flag.tar.gx
>cat flag/flag.txt | base64 -d

flag yields:
```
UiTHack20{how_many_layers_is_there?Spicy}
```