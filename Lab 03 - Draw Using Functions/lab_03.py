"""
This is just a sunset
"""

import arcade

# To make things easier later
screen_width = 1200
screen_height = 600
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 50, 160)
red = (239, 51, 64)
yellow = (255, 209, 0)


# To make the blue waves with the white background
def draw_wave_blue(left_x, bottom_y):
    arcade.draw_lrtb_rectangle_filled(left_x, screen_width, (bottom_y + 60), bottom_y, blue)
    arcade.draw_arc_filled(left_x, bottom_y, 200, 200, blue, 0, 180)
    arcade.draw_arc_filled((left_x + 240), bottom_y, 200, 200, blue, 0, 180)
    arcade.draw_arc_filled((left_x + 480), bottom_y, 200, 200, blue, 0, 180)
    arcade.draw_arc_filled((left_x + 720), bottom_y, 200, 200, blue, 0, 180)
    arcade.draw_arc_filled((left_x + 960), bottom_y, 200, 200, blue, 0, 180)
    arcade.draw_arc_filled((left_x + 1200), bottom_y, 200, 200, blue, 0, 180)
    y = bottom_y + 65
    arcade.draw_arc_filled((left_x + 120), y, 80, 60, white, 180, 360)
    arcade.draw_arc_filled((left_x + 360), y, 80, 60, white, 180, 360)
    arcade.draw_arc_filled((left_x + 600), y, 80, 60, white, 180, 360)
    arcade.draw_arc_filled((left_x + 840), y, 80, 60, white, 180, 360)
    arcade.draw_arc_filled((left_x + 1080), y, 80, 60, white, 180, 360)


# To make the white waves with the blue background
def draw_wave_white(left_x, bottom_y):
    arcade.draw_lrtb_rectangle_filled(left_x, screen_width, (bottom_y + 60), bottom_y, white)
    arcade.draw_arc_filled(left_x, bottom_y, 200, 200, white, 0, 180)
    arcade.draw_arc_filled((left_x + 240), bottom_y, 200, 200, white, 0, 180)
    arcade.draw_arc_filled((left_x + 480), bottom_y, 200, 200, white, 0, 180)
    arcade.draw_arc_filled((left_x + 720), bottom_y, 200, 200, white, 0, 180)
    arcade.draw_arc_filled((left_x + 960), bottom_y, 200, 200, white, 0, 180)
    arcade.draw_arc_filled((left_x + 1200), bottom_y, 200, 200, white, 0, 180)
    y = bottom_y + 65
    arcade.draw_arc_filled((left_x + 120), y, 80, 60, blue, 180, 360)
    arcade.draw_arc_filled((left_x + 360), y, 80, 60, blue, 180, 360)
    arcade.draw_arc_filled((left_x + 600), y, 80, 60, blue, 180, 360)
    arcade.draw_arc_filled((left_x + 840), y, 80, 60, blue, 180, 360)
    arcade.draw_arc_filled((left_x + 1080), y, 80, 60, blue, 180, 360)


# This is to make the top wave match the sky in the background
def top_wave_background(left_x, bottom_y):
    y = bottom_y + 65
    arcade.draw_arc_filled((left_x + 120), y, 80, 60, red, 180, 360)
    arcade.draw_arc_filled((left_x + 360), y, 80, 60, red, 180, 360)
    arcade.draw_arc_filled((left_x + 600), y, 80, 60, yellow, 180, 360)
    arcade.draw_arc_filled((left_x + 840), y, 80, 60, red, 180, 360)
    arcade.draw_arc_filled((left_x + 1080), y, 80, 60, red, 180, 360)


def draw_sun_body(center_x, center_y, radius):
    arcade.draw_circle_filled(center_x, center_y, radius, yellow)


def draw_sun_rays(center_x, center_y, width, length, start_angle):
    arcade.draw_rectangle_filled(center_x, center_y, width, length, yellow, start_angle)
    arcade.draw_rectangle_filled(center_x, center_y, width, length, yellow, start_angle + 45)
    arcade.draw_rectangle_filled(center_x, center_y, width, length, yellow, start_angle + 90)
    arcade.draw_rectangle_filled(center_x, center_y, width, length, yellow, start_angle + 135)


def draw_bird(center_x, center_y, color):
    arcade.draw_circle_filled(center_x, center_y, 8, color)
    arcade.draw_arc_filled(center_x + 15, center_y, 30, 20, color, -20, 180)
    arcade.draw_arc_filled(center_x - 15, center_y, 30, 20, color, 0, 200)
    arcade.draw_arc_filled(center_x + 15, center_y, 18, 15, red, -25, 180)
    arcade.draw_arc_filled(center_x - 15, center_y, 18, 15, red, 0, 205)


def main():
    arcade.open_window(screen_width, screen_height, "Sunset")
    arcade.set_background_color(red)
    arcade.start_render()

    # This part is to make the sun
    draw_sun_body(600, 250, 150)
    draw_sun_rays(600, 250, 20, 400, 0)
    draw_sun_rays(600, 250, 10, 350, 15)
    draw_sun_rays(600, 250, 10, 350, 30)

    # Making the waves starting from the top
    draw_wave_white(0, 180)
    top_wave_background(0, 180)
    draw_wave_blue(0, 120)
    draw_wave_white(0, 60)
    draw_wave_blue(0, 0)
    draw_wave_white(0, -60)

    # Adding some birds
    draw_bird(900, 450, black)
    draw_bird(850, 400, black)
    draw_bird(950, 400, white)
    draw_bird(800, 350, white)
    draw_bird(1000, 350, black)

    # Stop drawing and keep the window open
    arcade.finish_render()
    arcade.run()


main()
