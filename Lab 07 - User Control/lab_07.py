""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
MOUSE_CLICK_SOUND_LEFT = arcade.load_sound("arcade_resources_sounds_upgrade1.wav")
MOUSE_CLICK_SOUND_RIGHT = arcade.load_sound("arcade_resources_sounds_upgrade5.wav")
WALL_HIT_SOUND = arcade.load_sound("arcade_resources_sounds_hit1.wav")


class Smile:
    def __init__(self, position_x, position_y, side_length, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = 3 * side_length
        self.width = side_length
        self.height = side_length
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x - self.width,
                                     self.position_y + self.height,
                                     self.width,
                                     self.height,
                                     self.color)
        arcade.draw_rectangle_filled(self.position_x + self.width,
                                     self.position_y + self.height,
                                     self.width,
                                     self.height,
                                     self.color)
        arcade.draw_arc_filled(self.position_x,
                               self.position_y,
                               self.radius,
                               self.radius,
                               (0, 0, 0),
                               180, 360)


class Frown:
    def __init__(self, position_x, position_y, change_x, change_y, side_length, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = 3 * side_length
        self.width = side_length
        self.height = side_length
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x - self.width,
                                     self.position_y + self.height,
                                     self.width,
                                     self.height,
                                     self.color)
        arcade.draw_rectangle_filled(self.position_x + self.width,
                                     self.position_y + self.height,
                                     self.width,
                                     self.height,
                                     self.color)
        arcade.draw_arc_filled(self.position_x,
                               self.position_y - self.radius/2,
                               self.radius,
                               self.radius,
                               (0, 0, 0),
                               0, 180)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x < self.radius/2:
            self.position_x = self.radius/2
            arcade.play_sound(WALL_HIT_SOUND)
        if self.position_x > SCREEN_WIDTH - self.radius/2:
            self.position_x = SCREEN_WIDTH - self.radius/2
            arcade.play_sound(WALL_HIT_SOUND)
        if self.position_y < self.radius/2:
            self.position_y = self.radius/2
            arcade.play_sound(WALL_HIT_SOUND)
        if self.position_y > SCREEN_HEIGHT - self.radius/2:
            self.position_y = SCREEN_HEIGHT - self.radius/2
            arcade.play_sound(WALL_HIT_SOUND)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # Make so you don't see the mouse
        self.set_mouse_visible(False)

        # Making the smile
        self.smile = Smile(400, 300, 20, (0, 0, 0))

        # Making the frown
        self.frown = Frown(200, 300, 0, 0, 20, (0, 0, 0))

    def on_draw(self):
        arcade.start_render()
        # Draw the stripes in the background
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HEIGHT * 2 / 3, (0, 40, 104))
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT * 2 / 3, SCREEN_HEIGHT * 1 / 3,
                                          (255, 255, 255))
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT * 1 / 3, 0, (0, 40, 104))

        # Draw the C shape
        arcade.draw_arc_filled(SCREEN_WIDTH * 4 / 9, SCREEN_HEIGHT / 2, SCREEN_WIDTH * 4 / 9, SCREEN_WIDTH * 4 / 9,
                               (191, 10, 48), 20, 340, 2)

        # Yellow circle on top of the C
        arcade.draw_circle_filled(SCREEN_WIDTH * 4 / 9, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 9, (255, 215, 0))

        self.smile.draw()

        self.frown.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.smile.position_x = x
        self.smile.position_y = y

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(MOUSE_CLICK_SOUND_LEFT)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(MOUSE_CLICK_SOUND_RIGHT)

    def update(self, delta_time):
        self.frown.update()

    def on_key_press(self, key, modifiers):
        # Call when key is pressed, WASD movement
        if key == arcade.key.A:
            self.frown.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.frown.change_x = MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.frown.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.frown.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.frown.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.frown.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()
