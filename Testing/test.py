def main():
    my_file = open("super_villains.txt")

    for line in my_file:
        line = line.strip()
        print(line)

    my_file.close()

main()