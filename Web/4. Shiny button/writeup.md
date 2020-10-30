># Shiny button
>
>Walking around some dark halls you find youself in a larger room. 
>The room is barren with intricate carved store walls and a pedestal in the centre.
>Upon the pedestal is a large red button. \
>Although this very much looks like a trap, what else can you do but press it and find out.
>
>`link to website`

After 50k presses of the button it returns the flag. Instead of actually pressing it this many times a simple script like the one below is sufficient. Using sessions here is important as the backend matches your counter to your session user_id.

```py
import requests

s = requests.Session()
url = "link to website"

while 1:
    r = s.post(url)
    if b'UiTHack20{' in r.content:
        print(r.content)
        break

```