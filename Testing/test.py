import arcade


# Set how many rows and columns we will have and how big each square will be
ROW_COUNT = 21
COLUMN_COUNT = 10
SIZE = 30
# This sets the margin between each cell and edge of the screen
MARGIN = 5
# How many different levels to choose to start from
START_LEVELS_ROWS = 2
START_LEVELS_COLUMNS = 5
LEVEL_SELECT_SIZE = 2 * (SIZE * 2 + MARGIN)
# Do the math to figure out the play screen dimensions and window dimensions
PLAY_SCREEN_WIDTH = (SIZE + MARGIN) * COLUMN_COUNT + MARGIN
PLAY_SCREEN_HEIGHT = (SIZE + MARGIN) * ROW_COUNT + MARGIN
SCREEN_HEIGHT = (SIZE + MARGIN) * (ROW_COUNT + 3) + MARGIN
SCREEN_WIDTH = 3 * PLAY_SCREEN_WIDTH


class LevelSelect(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        Set up the application.
        """
        super().__init__(width, height)
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(START_LEVELS_ROWS):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(START_LEVELS_COLUMNS):
                self.grid[row].append(0)  # Append a cell

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw TETRIS and ask what level the player wants to start on
        arcade.draw_text("TETRIS",
                         PLAY_SCREEN_WIDTH - LEVEL_SELECT_SIZE / 2,
                         PLAY_SCREEN_HEIGHT - SIZE,
                         arcade.color.WHITE,
                         100)
        arcade.draw_text("Select a level to start on:",
                         2 * MARGIN + LEVEL_SELECT_SIZE,
                         2 * SCREEN_HEIGHT / 3,
                         arcade.color.WHITE,
                         50)

        # Draw the grid
        for row in range(START_LEVELS_ROWS):
            for column in range(START_LEVELS_COLUMNS):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                # Do the math to figure out where the box is
                x = (MARGIN + LEVEL_SELECT_SIZE) * column + MARGIN + LEVEL_SELECT_SIZE // 2 + PLAY_SCREEN_WIDTH / 2
                y = (MARGIN + LEVEL_SELECT_SIZE) * row + MARGIN + LEVEL_SELECT_SIZE // 2 + SCREEN_HEIGHT / 4

                # Draw the box
                arcade.draw_rectangle_filled(x, y, LEVEL_SELECT_SIZE, LEVEL_SELECT_SIZE, color)

                # Draw the number in the boxes
                arcade.draw_text(f"{5 * (-row + 1) + column}",
                                 x - 2 * MARGIN,
                                 y - 2 * MARGIN,
                                 arcade.color.BLACK,
                                 30, bold=True)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = (x - PLAY_SCREEN_WIDTH // 2) // (LEVEL_SELECT_SIZE + MARGIN)
        row = (y - PLAY_SCREEN_HEIGHT // 4) // (LEVEL_SELECT_SIZE + MARGIN)

        if -1 < column < START_LEVELS_COLUMNS and -1 < row < START_LEVELS_ROWS:
            level = 5 * (-row + 1) + column
            print(level)


def main():

    window = LevelSelect(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
