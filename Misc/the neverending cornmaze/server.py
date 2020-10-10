# import flask
from flask import Flask, render_template, redirect, url_for, request, g, session, abort, send_file
import os
import maze
import pathfind
import random
import hashlib
from threading import Thread

app = Flask(__name__)
app.config.update(dict(SECRET_KEY=os.urandom(16)))

hash_to_solution = {}

def get_maze_hash(m):
    
    accumulated = '';
    for i in range(0, min(200, len(m))):
        for s in m[i]:
            if s == '#':
                accumulated += s
    sha = hashlib.sha256(accumulated.encode('utf-8')).hexdigest()
    return sha;

def get_and_store_hash(maze, solution):
    hashed_maze = get_maze_hash(maze)
    print(hashed_maze)

    hash_to_solution[hashed_maze] = solution

@app.route('/submit', methods=['POST'])
def verify_input():
    input_path = request.form['input']
    input_mazehash = request.form['maze_hash']

    if input_path == hash_to_solution[input_mazehash]:
        return "UiTHack20{If_a_man_does_not_have_the_sauce,_then_he_is_lost._But_the_same_man_can_be_lost_in_the_sauce}"
    else:
        return "wrong path try again :)"


@app.route("/", methods=['GET'])
def index():
    seed = random.randint(0, 100000)
    large_maze = maze.get_maze(800, 800, seed)
    solution = pathfind.solve_maze(large_maze)

    hasher_thread = Thread(target=get_and_store_hash, kwargs={'maze': large_maze, 'solution': solution})
    hasher_thread.start()

    return render_template('index.html', maze_string=large_maze, start_x=1, start_y=1)

if __name__ == "__main__":
    app.run()
