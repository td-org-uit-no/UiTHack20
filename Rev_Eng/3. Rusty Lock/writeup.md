># Rusty Lock
>> Rev_eng - 200pts
>
>As you explore you come upon an old locked door. You see the lock is rusted shut. \
>Can you find a way to break through the door?
> 
> ### Files
> 
> * [rusty-check](./rusty-check)

## Writeup

Reverse engineering this binary will reveal that upon entering the correct password,
the encrypted flag will be decrypted and printed.

After reverse engineering the specific function, we can see that the flag is encrypted
using XOR where both inputs are known, and can be retrieved using the following python
function:

```python
xor = lambda a,b: map(lambda x:x[0]^x[1],zip(a,b))
```

Plugging the two components into the xor function yields the flag: `UiTHack20{binaries_with_secrets}`.
