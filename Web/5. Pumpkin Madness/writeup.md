># Pumpkin Madness
>> Web - 300pts
>
>If you look closely the Pumpkin Madness might consume youuuuuu....
>
>Files:
>[source code](./src/)

## Writeup

When one og the buttons (Click me) get a post request, the flag is added to the headers response request. It is called Pumpkin-flag, and the value
is base64 encoded. It yields:

```
UiTHack20{are_you_a_pumpkin_spice_latte_person?}
```
