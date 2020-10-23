from flask import Flask, render_template, redirect, url_for, request, g, session, abort, send_file
import os
app = Flask(__name__)
app.config.update(dict(SECRET_KEY=os.urandom(16)))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/casper")
def flag():
    return render_template('casper.html')