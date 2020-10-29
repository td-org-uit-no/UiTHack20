from flask import Flask, render_template, redirect, url_for, request, g, session, abort, send_file
import os
app = Flask(__name__)
app.config.update(dict(SECRET_KEY=os.urandom(16)))

uname =  "skeleton"
pwrd = "Spooky and scary password"
flag = "UiTHack20{We_aLL_look_the_same_when_we_d1e}"

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        form_uname = request.form['username']
        form_password = request.form['password']

        if form_uname == uname and form_password == pwrd:
            return render_template('index.html', flag=flag)

    return render_template('index.html')

if __name__ == "__main__":
    app.run()