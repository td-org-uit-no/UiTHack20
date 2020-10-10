
function update_player_pos() {
  let canvas = document.getElementById('maze');
  if (canvas.getContext) {
    ctx.fillRect(
        player_y * draw_size, player_x * draw_size, draw_size, draw_size);
  }
  input_field.value = accumulated_input;
}


function move_left() {
  if (maze_array[player_y - 1][player_x] == ' ') {
    player_y -= 1;
    maze_array[player_y][player_x] = 'P';
    accumulated_input += 'a';
    update_player_pos();
  }
}

function move_right() {
  if (maze_array[player_y + 1][player_x] == ' ') {
    player_y += 1;
    maze_array[player_y][player_x] = 'P';
    accumulated_input += 'd';
    update_player_pos();
  }
}

function move_up() {
  if (maze_array[player_y][player_x - 1] == ' ') {
    player_x -= 1;
    maze_array[player_y][player_x] = 'P';
    accumulated_input += 'w';
    update_player_pos();
  }
}

function move_down() {
  if (maze_array[player_y][player_x + 1] == ' ') {
    player_x += 1;
    maze_array[player_y][player_x] = 'P';
    accumulated_input += 's';
    update_player_pos();
  }
}

function draw_maze() {
  if (canvas.getContext) {
    // draw walls, player and goal
    for (let i = 0; i < maze_array.length; i++) {
      let row = maze_array[i];
      for (let j = 0; j < row.length; j++) {
        let curr_element = row[j];
        if (curr_element.localeCompare('#') == 0) {
          ctx.fillStyle = '#FBEC5D';
          ctx.fillRect(i * draw_size, j * draw_size, draw_size, draw_size);
        } else if (curr_element.localeCompare('P') == 0) {
          ctx.fillStyle = 'green';
          ctx.fillRect(i * draw_size, j * draw_size, draw_size, draw_size);
        } else if (curr_element.localeCompare('G') == 0) {
          ctx.fillStyle = 'red';
          ctx.fillRect(i * draw_size, j * draw_size, draw_size, draw_size);
        }
      }
    }
    ctx.fillStyle = 'green';
  }
}

function handle_keydown(event) {
  let pressed_char = String.fromCharCode(event.charCode || event.keyCode);
  if (pressed_char == 'w' || pressed_char == 'W') {
    move_up();
  } else if (pressed_char == 'd' || pressed_char == 'D') {
    move_right();
  } else if (pressed_char == 's' || pressed_char == 'S') {
    move_down();
  } else if (pressed_char == 'a' || pressed_char == 'A') {
    move_left();
  }
}


function hash_maze() {
  let hashstring = '';
  for (let i = 0; i < maze_array.length && i < 200; i++) {
    let row = maze_array[i];
    for (let j = 0; j < row.length; j++) {
      let curr_element = row[j];
      if (curr_element == '#') {
        hashstring = hashstring.concat(curr_element);
      }
    }
  }

  return CryptoJS.SHA256(hashstring).toString();
}
