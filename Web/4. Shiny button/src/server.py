from flask import Flask, render_template, redirect, url_for, request, g, session, abort, send_file
import os

app = Flask(__name__)
app.config.update(dict(SECRET_KEY=os.urandom(16)))


max_presses = 50000
flag = "UiTHack20{The_definition_0f_insan1ty_1s_d0ing_the_same_thing_over_and_0ver_again_and_expecting_d1fferent_results}"
counter_storage = {}


mockeries = [
    "how many do you think there are?", 
    "you are definetly getting closer", 
    "this would go faster if you had more ram: https://downloadmoreram.com/",
    "wow this is many presses", 
    "very tanacious of you inDeeD", 
    "imagine if it never ends",
    "you are getting closer, promise",
    "imagine giving up now",
    "you are actually very close now",
    "or are you?",
    "maybe you are, maybe not",
    "what do I know, I only made it to 50",
    "should have continued to 50k",
    "wow you are actually kinda close now",
    "last one, been nice speaking to you"
]

def pick_mockery(count):
    idx = int(count // (max_presses/(len(mockeries) + 1)))
    if idx == 0:
        return ""
    elif  idx-1 <= 0:
        return mockeries[0]
    elif idx-1 >= len(mockeries):
        return mockeries[-1]
    else:
        return mockeries[idx-1]

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        if 'user_id' not in session:
            session['user_id'] = os.urandom(64)
            return render_template('index.html', count='0')

        else:
            return render_template('index.html', count=session['user_id'])

    if request.method == 'POST':
        if 'user_id' not in session:
            session['user_id'] = os.urandom(64)

        user_id = session.get('user_id')
        if user_id:
            if user_id not in counter_storage:
                counter_storage[user_id] = 0
            
            counter_storage[user_id] += 1
            count = counter_storage[user_id]
            
            if count > max_presses:
                return render_template('index.html', count=count, flag=flag)
            else:
                return render_template('index.html', count=count, mockery=pick_mockery(count))
    
    
    return render_template('index.html', count='0')

if __name__ == "__main__":
    app.run()