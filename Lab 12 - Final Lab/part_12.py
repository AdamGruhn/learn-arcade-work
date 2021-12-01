"""
Final Project
Plan to make a tetris game
"""
"""
Things that need to get done first
- Creating the game screen
    - 10x20 game area
    - Next box
    - Score counter
- All tetrominoes created
    - Made in a list and then randomly select from the list for the piece
- Score calculation
    - Singles score 40 * (current_level + 1)
    - Doubles score 100 * (current_level + 1)
    - Triples score 300 * (current_level + 1)
    - Tetris scores 1200 * (current_level + 1)
- Rotation and movement of pieces
    - Make the pieces fall
    - Keyboard controls
        - Need to decide between 4/5 key controls
            - Maybe make a screen for the player to decide between the two
        - Normal controls with 4 keys
        - Emulate an NES controller for 5 keys
            - Bonus points based on amount of time holding down
    - When piece hits bottom, player had to repress the button to move again
- Speed up as levels progress
    - Strength of the gravity is incremental with levels
    - Max out speed at a certain level
- Game over when pieces reach the top of the screen
    - New screen that shows score
"""
"""
Later additions to not focus on right away
- Piece counter on the side to track how many of each piece has appeared
- Type A and Type B tetris
- Losing screen graphics, particularly something cool
    - Local leaderboard system as well
- Making pieces be different colors on different levels
"""