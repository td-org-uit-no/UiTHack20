># room5
>> Noob - 250pts
>
>Oh nooo, it's like all that have been before is now again. And we neeeed to find the flag!
>
>To enter the rooms you will need to connect through `ssh`.
>The username for this first room, is `room5`
>The server name is `sparkly-unicorn.td.org.uit.no`.
>The password for room5 is the flag from the `room4` challenge.
>
>
>
>Tips:
>`ssh room5@sparkly-unicorn.td.org.uit.no`
>
>Tips:
>Perhaps combine what you have learned until now?

## Writeup

Combining the methods from the two last rooms gives you the flag. A one liner command to get the flag is:
`cat $(find -name flag.txt) | grep UiTHack`. The flag yields:

```
UiTHack20{one_liner_commands_are_beautiful_yes?}
```
