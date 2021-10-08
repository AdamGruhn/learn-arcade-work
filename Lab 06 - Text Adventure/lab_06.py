class Room:
    def __init__(self, description, north, south, east, west, up, down):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down


def main():
    room_list = []
    # Room 0 Outside
    room = Room("You are outside of a mansion.\nHead North to enter.", 1, None, None, None, None, None)
    room_list.append(room)
    # Room 1
    room = Room("You are in the main hall.\nThere is a door to the North, East, and West.", 6, None, 3, 2, None, None)
    room_list.append(room)
    # Room 2
    room = Room("You are in the dining room.\nThere is a door to the North and to the East.", 4, None, 1, None, None, None)
    room_list.append(room)
    # Room 3
    room = Room("You are in the living room.\nThere is a door to the North and to the West.", 5, None, None, 1, None, None)
    room_list.append(room)
    # Room 4
    room = Room("You are in the kitchen.\nThere is a door to the South and to the East.", None, 2, 6, None, None, None)
    room_list.append(room)
    # Room 5
    room = Room("You are in the spare bedroom.\nThere is a door to the South and to the West.", None, 3, None, 6, None, None)
    room_list.append(room)
    # Room 6
    room = Room("You are in the back hall."
                "\nThere is a door the the South, East, and West."
                "\nThere is also a staircase going down.", None, 1, 5, 4, None, 7)
    room_list.append(room)
    # Room 7
    room = Room("You are in the lobby of the basement."
                "\nThere is a door to the South, East, and West."
                "\nThere is also a staircase going up.", None, 10, 9, 8, 6, None)
    room_list.append(room)
    # Room 8
    room = Room("You are in the master bedroom.\nThere is a door to the East.", None, None, 7, None, None, None)
    room_list.append(room)
    # Room 9
    room = Room("You are in the children's room.\nThere is a door to the West", None, None, None, 7, None, None)
    room_list.append(room)
    # Room 10
    room = Room("You are in the lounge.\nThere is a door to the North.", 7, None, None, None, None, None)
    room_list.append(room)

    current_room = 0
    done = False

    while not done:
        print("")
        print(room_list[current_room].description)
        user_input = input("Which direction do you want to go? ")

        # North
        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # South
        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # East
        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # West
        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # Up
        elif user_input.lower() == "u" or user_input.lower() == "up":
            next_room = room_list[current_room].up
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # Down
        elif user_input.lower() == "d" or user_input.lower() == "down":
            next_room = room_list[current_room].down
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # Quit Command
        elif user_input.lower() == "q" or user_input.lower() == "quit":
            done = True

        # Everything Else
        else:
            print("I don't understand what you want to do.")


main()
