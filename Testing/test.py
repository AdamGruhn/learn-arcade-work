import random

list_1 = []
for i in range(100):
    list_1.append(random.randrange(100))

list_2 = []
for i in range(100):
    list_2.append(random.randrange(100))


def selection_sort(my_list):
    """ Sort a list using the selection sort """
    print(my_list)
    runs_inside = 0
    runs_outside = 0
    # Loop through the entire array
    for cur_pos in range(len(my_list)):

        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos

        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(my_list)):

            # Is this position smallest?
            if my_list[scan_pos] < my_list[min_pos]:

                # It is, mark this position as the smallest
                min_pos = scan_pos
            runs_inside += 1

        # Swap the two values
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp
        runs_outside += 1
    print(runs_outside)
    print(runs_inside)


def insertion_sort(my_list):
    """ Sort a list using the insertion sort """
    print(my_list)
    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    runs_inside = 1
    runs_outside = 0
    for key_pos in range(1, len(my_list)):

        # Get the value of the element to insert
        key_value = my_list[key_pos]

        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1

        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1
            runs_inside += 1

        # Everything's been moved out of the way, insert
        # the key into the correct location
        my_list[scan_pos + 1] = key_value
        runs_outside += 1
    print(runs_outside)
    print(runs_inside)


selection_sort(list_1)
insertion_sort(list_2)
