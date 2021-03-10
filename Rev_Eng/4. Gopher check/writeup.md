># Gopher Check
>> Rev_Eng - 250pts
>While exploring you hear a faint noise from the walls. <br>
>Invesigating this you find a tiny hole. Within the small dark hole lies a >tiny keyhole. <br>
>You have found keys previously but none like this. <br>
>Can you find the correct key?
> 
> 
> * [gopher-check](./gopher-check)

## Writeup

Reverse engineering this binary will reveal that upon entering the correct password,
the encrypted flag will be decrypted and printed.

After reverse engineering the specific function, we can see that the flag is encrypted
using XOR where both inputs are known, and can be retrieved using the following python
function:

```python
xor = lambda a,b: map(lambda x:x[0]^x[1],zip(a,b))
```

Plugging the two components into the xor function yields the flag: `UiTHack20{gophers_are_secretive}`.
