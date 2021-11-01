import random
import arcade

MOVEMENT_SPEED = 4
SPRITE_SCALING_FROG = 0.6
SPRITE_SCALING_FLY = 0.3
SPRITE_SCALING_BEE = 0.35
FLY_COUNT = random.randrange(20, 30)
BEE_COUNT = FLY_COUNT // 2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

class Frog(arcade.Sprite):
    def __init__(self, filename, sprite_scaling, position_x, position_y, change_x, change_y):
        super().__init__(filename, sprite_scaling)
        print("yes")
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        

    def update(self):
        print("hi")
        self.position_x += self.change_x
        self.position_y += self.change_y

class Bug(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.change_x = 0
        self.change_y = 0

    def update(self):
        # Moving bugs
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Reflect off walls
        if self.left <= 0:
            self.left = 0
            self.change_x *= -1
        elif self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
            self.change_x *= -1
        elif self.bottom <= 0:
            self.bottom = 0
            self.change_y *= -1
        elif self.top >= SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT
            self.change_y *= -1


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Hungry Frog")

        self.frog_list = None
        self.fly_list = None
        self.bee_list = None

        self.frog_sprite = None
        self.score = 0

        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.CELADON_GREEN)

    def setup(self):
        self.frog_list = arcade.SpriteList()
        self.fly_list = arcade.SpriteList()
        self.bee_list = arcade.SpriteList()

        self.score = 0

        # Create the frog
        self.frog_sprite = Frog("frog.png", SPRITE_SCALING_FROG, SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 0, 0)

        for i in range(FLY_COUNT):
            fly = Bug("fly.png", SPRITE_SCALING_FLY)

            fly.center_x = random.randrange(SCREEN_WIDTH)
            fly.center_y = random.randrange(SCREEN_HEIGHT)

            fly.change_x = random.randrange(-5, 6, 2)
            fly.change_y = random.randrange(-5, 6, 2)

            self.fly_list.append(fly)

        for j in range(BEE_COUNT):
            bee = Bug("bee.png", SPRITE_SCALING_BEE)

            bee.center_x = random.randrange(SCREEN_WIDTH)
            bee.center_y = random.randrange(SCREEN_HEIGHT)

            bee.change_x = random.randrange(-1, 2, 2)
            bee.change_y = random.randrange(-1, 2, 2)

            self.bee_list.append(bee)

    def on_draw(self):
        arcade.start_render()
        self.fly_list.draw()
        self.bee_list.draw()

        score = f"Score = {self.score}"
        arcade.draw_text(score, 10, 10, arcade.color.WHITE, 12)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.frog_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.frog_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.frog_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.frog_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.frog_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.frog_sprite.change_x = 0

    def update(self, delta_time):
        self.fly_list.update()
        self.bee_list.update()

        fly_hit_list = arcade.check_for_collision_with_list(self.frog_sprite, self.fly_list)
        bee_hit_list = arcade.check_for_collision_with_list(self.frog_sprite, self.bee_list)

        for fly in fly_hit_list:
            fly.remove_from_sprite_lists()
            self.score += 1

        for bee in bee_hit_list:
            bee.remove_from_sprite_lists()
            self.score -= 1


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
