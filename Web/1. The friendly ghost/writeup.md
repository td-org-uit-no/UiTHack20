> # The friendly ghost
> > Web - 100pts
> 
> Not all ghosts are scary! We have a friendly ghost here, and he's the most famous one as well!
> If you know his name, write it in the input and see his website!
> 
> Files: 
> [source code](./scr/)

## Writeup

The input field is a dummy field, and the most famous friendly ghost is casper. To get the flag, enter `/casper` at the end of the url, and you will be redirected to the flag, yielding:

``` 
UiTHack20{casper_is_the_c0olest_of_Gh0st}
```
If you inspect the source code of the html in the `/casper` site, you will find a picture that is hidden. Remove this hidden tag, and inverse the QR code to get a second flag, yielding:

```
UiTHack20{can_you_inverse_casper_to_a_human?}
```
