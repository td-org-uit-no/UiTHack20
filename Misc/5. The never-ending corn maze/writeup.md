> # The never-ending corn maze
> > Misc - 300pts
> 
> Can you find your way out of the maze? 
> 
> Files: 
> [source code](./src/)

## Writeup

To solve the maze you need to write a program that reads the maze and finds the solution, the easiest is probably using python and the pathfinding module. \
You need to parse the solution to the equivalent input string and send it to the server. \
If the maze hash matches the input string the flag should be returned:

```
UiTHack20{If_a_man_does_not_have_the_sauce,_then_he_is_lost._But_the_same_man_can_be_lost_in_the_sauce}
```
