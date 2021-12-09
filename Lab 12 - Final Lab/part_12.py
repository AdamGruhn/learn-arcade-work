import arcade
import random
import PIL
"""
Final Project
Tetris game
Matrix work from
https://api.arcade.academy/en/latest/examples/tetris.html#tetris

For scoring calculations I used 
https://tetris.fandom.com/wiki/Scoring
"""
"""
To Do

DONE DONE Figure out why the pieces appear at the top of the screen
DONE DONE Make the screen larger than just the play area
DONE DONE Make the bottom layer of 1's below the screen
DONE DONE Make the bottom layer of 1's be DARK_GRAY without changing the colors of the tiles

DONE DONE Game Over Screen
DONE DONE Add a scoring system
DONE DONE Add a level system
DONE DONE Able to pause
DONE DONE Able to unpause
DONE DONE Line Clear Counter
Start screen with level selects - Sprites to click to select start level instead of typing
Add a next box
Counter for number of times each piece appeared
Sound effects on line clears
Create a leaderboard system at some point?

DONE DONE Made the speed scale with level

"""
# Set how many rows and columns we will have
ROW_COUNT = 21
COLUMN_COUNT = 10
# This sets the WIDTH and HEIGHT of each grid location
# Only one variable because they are squares
SIZE = 30
# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5
# Do the math to figure out the play screen dimensions
PLAY_SCREEN_WIDTH = (SIZE + MARGIN) * COLUMN_COUNT + MARGIN
PLAY_SCREEN_HEIGHT = (SIZE + MARGIN) * ROW_COUNT + MARGIN
SCREEN_HEIGHT = (SIZE + MARGIN) * (ROW_COUNT + 3) + MARGIN
SCREEN_WIDTH = 3 * PLAY_SCREEN_WIDTH


# Colors in order L, I, T, S, Z, O, J
colors = [arcade.color.DARK_GRAY,
          arcade.color.PURPLE,
          arcade.color.DARK_RED,
          arcade.color.YELLOW,
          arcade.color.GREEN,
          arcade.color.CYAN,
          arcade.color.BLUE,
          arcade.color.WHITE,
          arcade.color.BLACK]

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
    board += [[8 for _x in range(COLUMN_COUNT)]]
    return board


class MyGame(arcade.Window):
    """Main application"""
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.board = None
        self.frame_count = 0
        self.game_over = False
        self.paused = 1
        self.board_sprite_list = None

        self.tile = None
        self.tile_x = 0
        self.tile_y = 0

        self.next_tile = random.choice(TETROMINOES)
        self.next_tile_x = 0
        self.next_tile_y = 0

        self.line_clears = 0
        # Player can select the level they start on
        self.start_level = int(input("What level do you want to start on? "))
        self.current_level = self.start_level

        self.score = 0
        self.piece_clear = 0

    def new_tile(self):
        # Randomly picks new tile and set location to top. Game over if
        # immediately collides
        self.tile = self.next_tile
        self.tile_x = int(COLUMN_COUNT / 2 - len(self.tile[0]) / 2)
        self.tile_y = 0
        # Makes a tile that I can display in the "Next Box"
        self.next_tile = random.choice(TETROMINOES)
        print(self.next_tile)

        if check_collision(self.board, self.tile, (self.tile_x, self.tile_y)):
            self.game_over = True

    def setup(self):
        """
        Draws the grid in the background
        """
        self.board = new_board()
        self.board_sprite_list = arcade.SpriteList()
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                sprite = arcade.Sprite()
                for texture in texture_list:
                    sprite.append_texture(texture)
                sprite.set_texture(0)
                sprite.center_x = PLAY_SCREEN_WIDTH + (MARGIN + SIZE) * column + MARGIN + SIZE // 2
                sprite.center_y = PLAY_SCREEN_HEIGHT - (MARGIN + SIZE) * (row + 1) + MARGIN + SIZE // 2

                self.board_sprite_list.append(sprite)

        self.new_tile()
        self.update_board()

    def fall(self):
        """
        Pieces fall
        If collision, join matrices
        """
        if not self.game_over and self.paused != -1:
            self.tile_y += 1
            self.piece_clear = 0
            if check_collision(self.board, self.tile, (self.tile_x,
                                                       self.tile_y)):
                self.board = join_matrices(self.board, self.tile,
                                           (self.tile_x, self.tile_y))
                while True:
                    # Line clear code
                    for i, row in enumerate(self.board[:-1]):
                        if 0 not in row:
                            self.board = remove_row(self.board, i)
                            self.line_clears += 1
                            self.piece_clear += 1

                            break
                    else:
                        break
                if self.piece_clear == 4:
                    self.score += (self.current_level + 1) * 1200
                    # Each of these if statements makes it so that you
                    # Don't reach a new level until your line count is high enough
                    if self.line_clears >= self.start_level:
                        self.current_level = self.start_level + self.line_clears // 10
                if self.piece_clear == 3:
                    self.score += (self.current_level + 1) * 300
                    if self.line_clears >= self.start_level:
                        self.current_level = self.start_level + self.line_clears // 10
                if self.piece_clear == 2:
                    self.score += (self.current_level + 1) * 100
                    if self.line_clears >= self.start_level:
                        self.current_level = self.start_level + self.line_clears // 10
                if self.piece_clear == 1:
                    self.score += (self.current_level + 1) * 40
                    if self.line_clears >= self.start_level:
                        self.current_level = self.start_level + self.line_clears // 10

                self.update_board()
                self.new_tile()

    def rotate_tile_clockwise(self):
        """
        Rotate tile clockwise and check for collision
        """
        if not self.game_over and self.paused != -1:
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
        if not self.game_over and self.paused != -1:
            new_tile = rotate_counterclockwise(self.tile)
            if self.tile_x + len(new_tile[0]) >= COLUMN_COUNT:
                self.tile_x = COLUMN_COUNT - len(new_tile[0])
            if not check_collision(self.board, new_tile, (self.tile_x,
                                                          self.tile_y)):
                self.tile = new_tile

    def on_update(self, dt):
        """Basically the game speed"""
        self.frame_count += 1
        # Speed scales with each level that you are on
        if self.current_level <= 58:
            if self.frame_count % (59 // (self.current_level + 1)) == 0:
                self.fall()
        # When current level is larger than 58 it divides by 0 and breaks
        elif self.current_level > 58:
            if self.frame_count % 1 == 0:
                self.fall()

    def move_x(self, delta_x):
        """Move tile left or right"""
        if not self.game_over and self.paused != -1:
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
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.move_x(-1)
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.move_x(1)
        elif key == arcade.key.J:
            self.rotate_tile_counterclockwise()
        elif key == arcade.key.UP or key == arcade.key.L:
            self.rotate_tile_clockwise()
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.fall()
        elif key == arcade.key.P:
            self.paused *= -1

    def draw_grid(self, grid, offset_x, offset_y):
        """
        Draws the tetrominoes
        """
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                # Assigns colors
                if grid[row][column]:
                    color = colors[grid[row][column]]
                    x = PLAY_SCREEN_WIDTH + (MARGIN + SIZE) * (column + offset_x) + MARGIN +\
                        SIZE // 2
                    y = PLAY_SCREEN_HEIGHT - (MARGIN + SIZE) * (row + offset_y + 1) +\
                        MARGIN + SIZE // 2

                    arcade.draw_rectangle_filled(x, y, SIZE, SIZE, color)

    # def draw_next(self, grid, offset_x, offset_y):
    #     for row in range(len(grid)):
    #         for column in range(len(grid[0])):
    #             if grid[row][column]:
    #                 color = colors[grid[row][column]]
    #                 x =

    def update_board(self):
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                v = self.board[row][column]
                i = row * COLUMN_COUNT + column
                self.board_sprite_list[i].set_texture(v)

    def on_draw(self):
        arcade.start_render()
        self.board_sprite_list.draw()
        # Draws the falling tiles
        self.draw_grid(self.tile, self.tile_x, self.tile_y)
        # Draws the tiles in the next box
        # self.draw_next(self.next_tile, self.next_tile_x, self.next_tile_y)
        self.draw_counters()

    def draw_counters(self):
        """
        Boxes with different stats
        """
        # Line clear counter
        arcade.draw_text(f"Lines: {self.line_clears}",
                         2 * SCREEN_WIDTH / 5,
                         PLAY_SCREEN_HEIGHT - 3 * MARGIN + 2 * SIZE,
                         arcade.color.WHITE,
                         30, bold=True)

        # Level counter
        arcade.draw_text("Level:",
                         2 * PLAY_SCREEN_WIDTH + SIZE,
                         PLAY_SCREEN_HEIGHT - 6 * SIZE - 5 * MARGIN,
                         arcade.color.WHITE,
                         30, bold=True)
        arcade.draw_text(f"{self.current_level}",
                         2 * PLAY_SCREEN_WIDTH + SIZE,
                         PLAY_SCREEN_HEIGHT - 7 * SIZE - 7 * MARGIN,
                         arcade.color.WHITE,
                         30, bold=True)

        # Scoreboard
        arcade.draw_text("Score:",
                         2 * PLAY_SCREEN_WIDTH + SIZE,
                         PLAY_SCREEN_HEIGHT - 3 * SIZE - 2 * MARGIN,
                         arcade.color.WHITE,
                         30, bold=True)
        arcade.draw_text(f"{self.score}",
                         2 * PLAY_SCREEN_WIDTH + SIZE,
                         PLAY_SCREEN_HEIGHT - 4 * SIZE - 4 * MARGIN,
                         arcade.color.WHITE,
                         30, bold=True)

        if self.game_over:
            arcade.draw_text("GAME",
                             PLAY_SCREEN_WIDTH - SIZE - MARGIN,
                             SCREEN_HEIGHT / 2,
                             arcade.color.RED,
                             100, bold=True)
            arcade.draw_text("OVER",
                             PLAY_SCREEN_WIDTH - SIZE - MARGIN,
                             SCREEN_HEIGHT / 2 - 150,
                             arcade.color.RED,
                             100, bold=True)


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Tetris")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
