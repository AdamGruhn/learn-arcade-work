"""
Flag of Kiribati ~without the bird~
"""
import arcade

# Opening the window
arcade.open_window(1200, 600, "Flag of Kiribati ~without the bird~")

# Background
arcade.set_background_color((239, 51, 64))

# Get ready to draw
arcade.start_render()

# Sun parts will go here
arcade.draw_circle_filled(600, 250, 100, (255, 209, 0))
arcade.draw_triangle_filled(510, 265, 460, 275, 510, 285, (255, 209, 0))
arcade.draw_triangle_filled(575, 340, 600, 390, 625, 340, (255, 209, 0))
arcade.draw_triangle_filled(690, 265, 740, 275, 690, 285, (255, 209, 0))
arcade.draw_triangle_filled(540, 265, 510, 340, 570, 325, (255, 209, 0))
arcade.draw_triangle_filled(660, 265, 690, 340, 630, 325, (255, 209, 0))

# Top White Wave
arcade.draw_lrtb_rectangle_filled(0, 1200, 240, 180, (255, 255, 255))
arcade.draw_arc_filled(0, 180, 200, 200, (255, 255, 255), 0, 180)
arcade.draw_arc_filled(240, 180, 200, 200, (255, 255, 255), 0, 180)
arcade.draw_arc_filled(480, 180, 200, 200, (255, 255, 255), 0, 180)
arcade.draw_arc_filled(720, 180, 200, 200, (255, 255, 255), 0, 180)
arcade.draw_arc_filled(960, 180, 200, 200, (255, 255, 255), 0, 180)
arcade.draw_arc_filled(1200, 180, 200, 200, (255, 255, 255), 0, 180)
arcade.draw_arc_filled(120, 245, 80, 60, (239, 51, 64), 180, 360)
arcade.draw_arc_filled(360, 245, 80, 60, (239, 51, 64), 180, 360)
arcade.draw_arc_filled(600, 245, 80, 60, (255, 209, 0), 180, 360)
arcade.draw_arc_filled(840, 245, 80, 60, (239, 51, 64), 180, 360)
arcade.draw_arc_filled(1080, 245, 80, 60, (239, 51, 64), 180, 360)

# Top Blue Wave
arcade.draw_lrtb_rectangle_filled(0, 1200, 180, 120, (0, 50, 160))
arcade.draw_arc_filled(0, 120, 200, 200, (0, 50, 160), 0, 180)
arcade.draw_arc_filled(240, 120, 200, 200, (0, 50, 160), 0, 180)
arcade.draw_arc_filled(480, 120, 200, 200, (0, 50, 160), 0, 180)
arcade.draw_arc_filled(720, 120, 200, 200, (0, 50, 160), 0, 180)
arcade.draw_arc_filled(960, 120, 200, 200, (0, 50, 160), 0, 180)
arcade.draw_arc_filled(1200, 120, 200, 200, (0, 50, 160), 0, 180)
arcade.draw_arc_filled(120, 185, 80, 60, (255, 255, 255), 180, 360)
arcade.draw_arc_filled(360, 185, 80, 60, (255, 255, 255), 180, 360)
arcade.draw_arc_filled(600, 185, 80, 60, (255, 255, 255), 180, 360)
arcade.draw_arc_filled(840, 185, 80, 60, (255, 255, 255), 180, 360)
arcade.draw_arc_filled(1080, 185, 80, 60, (255, 255, 255), 180, 360)

# Bottom White Wave
arcade.draw_lrtb_rectangle_filled(0, 1200, 120, 60, (255, 255, 255))
arcade.draw_arc_filled(0, 60, 200, 200, (255, 255, 255), 0, 180)
arcade.draw_arc_filled(240, 60, 200, 200, (255, 255, 255), 0, 180)
arcade.draw_arc_filled(480, 60, 200, 200, (255, 255, 255), 0, 180)
arcade.draw_arc_filled(720, 60, 200, 200, (255, 255, 255), 0, 180)
arcade.draw_arc_filled(960, 60, 200, 200, (255, 255, 255), 0, 180)
arcade.draw_arc_filled(1200, 60, 200, 200, (255, 255, 255), 0, 180)
arcade.draw_arc_filled(120, 125, 80, 60, (0, 50, 160), 180, 360)
arcade.draw_arc_filled(360, 125, 80, 60, (0, 50, 160), 180, 360)
arcade.draw_arc_filled(600, 125, 80, 60, (0, 50, 160), 180, 360)
arcade.draw_arc_filled(840, 125, 80, 60, (0, 50, 160), 180, 360)
arcade.draw_arc_filled(1080, 125, 80, 60, (0, 50, 160), 180, 360)

# Bottom Blue Wave
arcade.draw_lrtb_rectangle_filled(0, 1200, 60, 0, (0, 50, 160))
arcade.draw_arc_filled(0, 0, 200, 200, (0, 50, 160), 0, 180)
arcade.draw_arc_filled(240, 0, 200, 200, (0, 50, 160), 0, 180)
arcade.draw_arc_filled(480, 0, 200, 200, (0, 50, 160), 0, 180)
arcade.draw_arc_filled(720, 0, 200, 200, (0, 50, 160), 0, 180)
arcade.draw_arc_filled(960, 0, 200, 200, (0, 50, 160), 0, 180)
arcade.draw_arc_filled(1200, 0, 200, 200, (0, 50, 160), 0, 180)
arcade.draw_arc_filled(120, 65, 80, 60, (255, 255, 255), 180, 360)
arcade.draw_arc_filled(360, 65, 80, 60, (255, 255, 255), 180, 360)
arcade.draw_arc_filled(600, 65, 80, 60, (255, 255, 255), 180, 360)
arcade.draw_arc_filled(840, 65, 80, 60, (255, 255, 255), 180, 360)
arcade.draw_arc_filled(1080, 65, 80, 60, (255, 255, 255), 180, 360)

# Finish Drawing
arcade.finish_render()

# Put at end to keep window open
arcade.run()
