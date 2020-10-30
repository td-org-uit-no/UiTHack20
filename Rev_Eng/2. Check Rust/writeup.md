# Rusty Check

> Ikke sikker på poengene, men ikke altfor vanskelig.
> Utfordringen/det interessante her er at det ikke er C/CPP,
> men heller Rust som binaryen er skrevet i.
> 
> (Kan du finne på noe spennende her?)
> 
> Can you determine the password and retrieve the flag?
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

Plugging the two components into the xor function yields the flag: `UiTHack20{another_flag_bite_the}`.
