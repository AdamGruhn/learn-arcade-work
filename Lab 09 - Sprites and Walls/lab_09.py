"""

Sprites all from https://kenney.nl/assets/sokoban
"""

import random
import arcade

SPRITE_SCALING = 1
STEP = 64 * SPRITE_SCALING
PLAYER_SCALING = .75
COIN_SCALING = .5

NUMBER_OF_COINS = random.randrange(15, 25)
# Sound taken from https://api.arcade.academy/en/latest/resources.html
COIN_COLLECT_SOUND = arcade.load_sound("arcade_resources_sounds_coin2.wav")

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("player_23.png",
                                           scale=PLAYER_SCALING)
        self.player_sprite.center_x = -640 + 64 * SPRITE_SCALING
        self.player_sprite.center_y = -640 + 64 * SPRITE_SCALING
        self.player_list.append(self.player_sprite)

        # Border walls made with for loops, specifically placed
        for x in range(-640, 641, STEP):
            for y in range(-640, 641, 1280):
                if x % 128 == 0:
                    wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)
                else:
                    wall = arcade.Sprite("crate_11.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)
        for y in range(-640, 641, STEP):
            for x in range(-640, 641, 1280):
                if y % 128 == 0:
                    wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)
                else:
                    wall = arcade.Sprite("crate_11.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        # Create walls specifically placed
        eyes_coordinates = [[-128, 64], [-64, 128], [-128, 128], [-64, 64],
                            [128, 64], [64, 128], [128, 128], [64, 64]]
        mouth_coordinates = [[-128, -64], [-64, -128], [0, -128], [64, -128], [128, -64]]
        for coordinate in eyes_coordinates:
            wall = arcade.Sprite("crate_44.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)
        for coordinate in mouth_coordinates:
            wall = arcade.Sprite("crate_43.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Create central walls randomly
        # 1 in 5 spaces are walls
        for x in range(-640 + 2*STEP, 640 - 2 * STEP + 1, STEP):
            for y in range(-640 + 2*STEP, 640 - 2 * STEP + 1, STEP):
                if -192 <= x <= 192 and -192 <= y <= 192:
                    pass
                elif random.randrange(5) == 0:
                    wall = arcade.Sprite("crate_42.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        # Making the coins
        for i in range(NUMBER_OF_COINS):
            coin = arcade.Sprite("environment_12.png", COIN_SCALING)

            coin_placed_successfully = False

            while not coin_placed_successfully:
                coin.center_x = random.randrange(-640, 640)
                coin.center_y = random.randrange(-640, 640)

                # Check if coin is on wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)
                # Check if coin is on another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True

            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        self.score = 0

    def on_draw(self):
        arcade.start_render()

        # Select the camera to draw all sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Score = {self.score}"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)
        if len(self.coin_list) <= 0:
            arcade.draw_text("GAME OVER", 20, 350, arcade.color.BLACK, 90)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        if len(self.coin_list) > 0:

            self.physics_engine.update()

            # Scroll the screen to the player
            self.scroll_to_player()

            coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

            for coin in coin_hit_list:
                coin.remove_from_sprite_lists()
                arcade.play_sound(COIN_COLLECT_SOUND)
                self.score += 1
        else:
            pass


    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = self.player_sprite.center_x - self.width / 2, \
            self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()