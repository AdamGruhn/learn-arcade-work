"""
Colorado Flag
"""
import arcade
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# Opening the window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Colorado Flag")

# Get ready to draw
arcade.start_render()

# Draw the stripes in the background
arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HEIGHT * 2/3, (0, 40, 104))
arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT * 2/3, SCREEN_HEIGHT * 1/3, (255, 255, 255))
arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT * 1/3, 0, (0, 40, 104))

# Draw the C shape
arcade.draw_arc_filled(SCREEN_WIDTH*4/9, SCREEN_HEIGHT/2, SCREEN_WIDTH*4/9, SCREEN_WIDTH*4/9, (191, 10, 48), 20, 340, 2)

# Yellow circle on top of the C
arcade.draw_circle_filled(SCREEN_WIDTH*4/9, SCREEN_HEIGHT/2, SCREEN_WIDTH/9, (255, 215, 0))

# Finish Drawing
arcade.finish_render()

# Put at end to keep window open
arcade.run()
