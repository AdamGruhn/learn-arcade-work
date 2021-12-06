import arcade
import random
import PIL
"""
Final Project
Plan to make a tetris game
Matrix work from
https://api.arcade.academy/en/latest/examples/tetris.html#tetris
"""
"""
To Do

Figure out why the pieces appear at the top of the screen
Make the screen larger than just the play area
Make the bottom layer of 1's below the screen

Game Over Screen
Add a scoring system
Add a level system
Add a next box

Made the speed scale with level
https://harddrop.com/wiki/Tetris_(NES,_Nintendo)

"""
# Set how many rows and columns we will have
ROW_COUNT = 20
COLUMN_COUNT = 10
# This sets the WIDTH and HEIGHT of each grid location
# Only one variable because they are squares
SIZE = 30
# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5
# Do the math to figure out the play screen dimensions
SCREEN_WIDTH = (SIZE + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (SIZE + MARGIN) * ROW_COUNT + MARGIN

# Colors in order L, I, T, S, Z, O, J
colors = [arcade.color.BLACK,
          arcade.color.PURPLE,
          arcade.color.RED,
          arcade.color.YELLOW,
          arcade.color.GREEN,
          arcade.color.CYAN,
          arcade.color.BLUE,
          arcade.color.WHITE]

# Making the shapes in their own matrices
# Same order, L, I, T, S, Z, O, J
TETROMINOES = [
    [[1, 1, 1],
     [1, 0, 0]],
    [[2, 2, 2, 2]],
    [[3, 3, 3],
     [0, 3, 0]],
    [[0, 4, 4],
     [4, 4, 0]],
    [[5, 5, 0],
     [0, 5, 5]],
    [[6, 6],
     [6, 6]],
    [[7, 7, 7],
     [0, 0, 7]]
]


def create_textures():
    # Makes a list of pictures for sprites
    new_textures = []
    for color in colors:
        image = PIL.Image.new('RGBA', (SIZE, SIZE), color)
        new_textures.append(arcade.Texture(str(color), image=image))
    return new_textures


texture_list = create_textures()


def rotate_counterclockwise(shape):
    # Rotates the matrices counterclockwise
    """
    3 3 3               3 0
    0 3 0   Goes to     3 3
                        3 0
    """
    return [[shape[y][x] for y in range(len(shape))]
            for x in range(len(shape[0]) - 1, -1, -1)]


def rotate_clockwise(shape):
    # Rotates the matrices clockwise
    """
    3 3 3               0 3
    0 3 0   Goes to     3 3
                        0 3
    """
    return [[shape[y][x] for y in range(len(shape) - 1, -1, -1)]
            for x in range(len(shape[0]))]


def check_collision(board, shape, offset):
    # Checks for collisions on the board
    # Offset is an (x, y) coordinate
    off_x, off_y = offset
    for cy, row in enumerate(shape):
        for cx, cell in enumerate(row):
            if cell and board[cy + off_y][cx + off_x]:
                return True
    return False


def remove_row(board, row):
    # Clears the row when there is a line clear
    del board[row]
    return [[0 for _ in range(COLUMN_COUNT)]] + board


def join_matrices(matrix1, matrix2, matrix2offset):
    # Copies matrix 2 into matrix 1 based on the passed in x, y offset
    off_x, off_y = matrix2offset
    for cy, row in enumerate(matrix2):
        for cx, val in enumerate(row):
            matrix1[cy + off_y - 1][cx + off_x] += val
    return matrix1


def new_board():
    # Creates grid of 0's
    board = [[0 for _x in range(COLUMN_COUNT)] for _y in range(ROW_COUNT)]
    # Creates row of 1's at the bottom
    board += [[1 for _x in range(COLUMN_COUNT)]]
    return board


class MyGame(arcade.Window):
    """Main application"""
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.DARK_GRAY)

        self.board = None
        self.frame_count = 0
        self.game_over = False
        self.paused = False
        self.board_sprite_list = None

        self.tile = None
        self.tile_x = 0
        self.tile_y = 0

    def new_tile(self):
        # Randomly picks new tile and set location to top. Game over if
        # immediately collides
        self.tile = random.choice(TETROMINOES)
        self.tile_x = int(COLUMN_COUNT / 2 - len(self.tile[0]) / 2)
        self.tile_y = 0

        if check_collision(self.board, self.tile, (self.tile_x, self.tile_y)):
            self.game_over = True

    def setup(self):
        self.board = new_board()

        self.board_sprite_list = arcade.SpriteList()
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                sprite = arcade.Sprite()
                for texture in texture_list:
                    sprite.append_texture(texture)
                sprite.set_texture(0)
                sprite.center_x = (MARGIN + SIZE) * column + MARGIN + SIZE // 2
                sprite.center_y = SCREEN_HEIGHT - (MARGIN + SIZE) * row + MARGIN + SIZE // 2

                self.board_sprite_list.append(sprite)
        self.new_tile()
        self.update_board()

    def fall(self):
        """
        Pieces fall
        If collision, join matrices
        """
        if not self.game_over and not self.paused:
            self.tile_y += 1
            if check_collision(self.board, self.tile, (self.tile_x,
                                                       self.tile_y)):
                self.board = join_matrices(self.board, self.tile,
                                           (self.tile_x, self.tile_y))
                while True:
                    # Line clear code
                    for i, row in enumerate(self.board[:-1]):
                        if 0 not in row:
                            self.board = remove_row(self.board, i)
                            break
                    else:
                        break
                self.update_board()
                self.new_tile()

    def rotate_tile_clockwise(self):
        """
        Rotate tile clockwise and check for collision
        """
        if not self.game_over and not self.paused:
            new_tile = rotate_clockwise(self.tile)
            if self.tile_x + len(new_tile[0]) >= COLUMN_COUNT:
                self.tile_x = COLUMN_COUNT - len(new_tile[0])
            if not check_collision(self.board, new_tile, (self.tile_x,
                                                          self.tile_y)):
                self.tile = new_tile

    def rotate_tile_counterclockwise(self):
        """
        Rotate tile counterclockwise and check for collision
        """
        if not self.game_over and not self.paused:
            new_tile = rotate_counterclockwise(self.tile)
            if self.tile_x + len(new_tile[0]) >= COLUMN_COUNT:
                self.tile_x = COLUMN_COUNT - len(new_tile[0])
            if not check_collision(self.board, new_tile, (self.tile_x,
                                                          self.tile_y)):
                self.tile = new_tile

    def on_update(self, dt):
        """Piece moves every 1/6 of a second"""
        self.frame_count += 1
        if self.frame_count % 10 == 0:
            self.fall()

    def move_x(self, delta_x):
        """Move tile left or right"""
        if not self.game_over and not self.paused:
            new_x = self.tile_x + delta_x
            if new_x < 0:
                new_x = 0
            if new_x > COLUMN_COUNT - len(self.tile[0]):
                new_x = COLUMN_COUNT - len(self.tile[0])
            if not check_collision(self.board, self.tile, (new_x,
                                                           self.tile_y)):
                self.tile_x = new_x

    def on_key_press(self, key, modifiers):
        """
        Left and Right movement
        Clockwise and counter rotation
        Drop down
        """
        if key == arcade.key.NUM_4:
            self.move_x(-1)
        elif key == arcade.key.NUM_6:
            self.move_x(1)
        elif key == arcade.key.NUM_8:
            self.rotate_tile_counterclockwise()
        elif key == arcade.key.NUM_2:
            self.rotate_tile_clockwise()
        elif key == arcade.key.NUM_5:
            self.fall()

    def draw_grid(self, grid, offset_x, offset_y):
        """
        Draws the tetrominoes
        """
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                # Assigns colors
                if grid[row][column]:
                    color = colors[grid[row][column]]
                    x = (MARGIN + SIZE) * (column + offset_x) + MARGIN + SIZE // 2
                    y = SCREEN_HEIGHT - (MARGIN + SIZE) * (row + offset_y) + MARGIN + SIZE // 2

                    arcade.draw_rectangle_filled(x, y, SIZE, SIZE, color)

    def update_board(self):
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                v = self.board[row][column]
                i = row * COLUMN_COUNT + column
                self.board_sprite_list[i].set_texture(v)

    def on_draw(self):
        arcade.start_render()
        self.board_sprite_list.draw()
        self.draw_grid(self.tile, self.tile_x, self.tile_y)


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Tetris")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
