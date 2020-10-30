># room4
>> Noob - 200pts
>
>There is too many possibilities.. Where can the next flag be? How can you find it? Can one search for it?... 
>
>To enter the rooms you will need to connect through `ssh`.
>The username for this first room, is `room4`
>The server name is `sparkly-unicorn.td.org.uit.no`.
>The password for room4 is the flag from the `room3` challenge.
>
>
>
>Tips:
>`ssh room4@sparkly-unicorn.td.org.uit.no`
>
>Tips:
>Can you search to find your flag? What do we know of its standard format?

## Writeup

The flag.txt file is hidden in a sea of directories. By searching for it with find `fins -name flag.txt` you will find the path to the flag and it will yield:
```
UiTHack20{can't_believe_you_found_me}
```