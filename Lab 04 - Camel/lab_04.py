"""
Camel Game
"""

import random


def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make you way across the great Mobi Desert.")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and out run the natives across the desert.")
    player_miles_traveled = 0
    natives_miles_traveled = -20
    player_thirst = 0
    camel_tiredness = 0
    canteen_drinks_left = 3

    done = False
    while not done:
        print("")
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit")
        print("")
        user_input = input("What is your choice? ")
        print("")

        if user_input.lower() == "q":
            print("You have quit the game. :(")
            break

        elif user_input.lower() == "e":
            print(f"Miles traveled: {player_miles_traveled}")
            print(f"Drinks in Canteen: {canteen_drinks_left}")
            print(f"The natives are {player_miles_traveled - natives_miles_traveled} miles behind you.")

        elif user_input.lower() == "d":
            camel_tiredness = 0
            print("Your camel is well rested.")
            natives_miles_traveled += random.randrange(7, 15)

        elif user_input.lower() == "c":
            player_thirst += 1
            camel_tiredness += random.randrange(1, 4)
            turn_distance = random.randrange(10, 21)
            print(f"You traveled {turn_distance} miles.")
            player_miles_traveled += turn_distance
            natives_miles_traveled += random.randrange(7, 15)
            if random.randrange(20) == 0:
                canteen_drinks_left = 3
                camel_tiredness = 0
                player_thirst = 0
                print("You found an oasis!")

        elif user_input.lower() == "b":
            player_thirst += 1
            camel_tiredness += 1
            turn_distance = random.randrange(5, 13)
            print(f"You traveled {turn_distance} miles.")
            player_miles_traveled += turn_distance
            natives_miles_traveled += random. randrange(7, 15)
            if random.randrange(20) == 0:
                canteen_drinks_left = 3
                camel_tiredness = 0
                player_thirst = 0
                print("You found an oasis!")

        elif user_input.lower() == "a":
            if canteen_drinks_left > 0:
                print("You are no longer thirsty.")
                canteen_drinks_left -= 1
                player_thirst = 0
            else:
                print("You have no drinks left in your canteen.")

        if player_thirst > 4:
            if player_thirst > 6:
                print("You died of thirst. :(")
                break
            else:
                print("You are thirsty.")

        if camel_tiredness > 5:
            if camel_tiredness > 8:
                print("Your camel died of exhaustion. :(")
                break
            else:
                print("Your camel is getting tired.")

        if natives_miles_traveled >= player_miles_traveled:
            print("The natives caught you. :(")
            break

        elif player_miles_traveled - natives_miles_traveled < 15:
            print("The natives are getting close!")

        if player_miles_traveled >= 200:
            print("You made it across the desert and escaped the natives.")
            break


main()
