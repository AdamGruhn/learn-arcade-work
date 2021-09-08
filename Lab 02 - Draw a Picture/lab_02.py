"""
Colorado Flag
"""
import arcade

# Opening the window
arcade.open_window(900, 600, "Colorado Flag")

# Get ready to draw
arcade.start_render()

# Draw the stripes in the background
arcade.draw_lrtb_rectangle_filled(0, 900, 600, 400, (0, 40, 104))
arcade.draw_lrtb_rectangle_filled(0, 900, 400, 200, (255, 255, 255))
arcade.draw_lrtb_rectangle_filled(0, 900, 200, 0, (0, 40, 104))

# Draw the C shape
arcade.draw_arc_filled(400, 300, 400, 400, (191, 10, 48), 20, 340, 2)

# Yellow circle on top of the C
arcade.draw_circle_filled(400, 300, 100, (255, 215, 0))

# Finish Drawing
arcade.finish_render()

# Put at end to keep window open
arcade.run()
