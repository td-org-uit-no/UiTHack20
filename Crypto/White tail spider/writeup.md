># White tail spider
>> Crypto - 150pts
>
>We're on the hunt after a serial killer, called White tail spider. We know the most gruesome ways she makes her kills, based on descriptions found in letters sent to us, from her. 
>Still, there is something peculiar with this last one, maybe this might lead us to a clue on how to catch her. We just need to find all the pieces. 
>
>
>[Letter](./letter.txt)

## Writeup

Inside the text, there is pieces of a base64 cipher. It is recognized by the last piece, that end with `==`.
The decoded cipher yields:

```
UiTHack20{I_will_find_you_at_UiTHack_xoxo_WTS}
```