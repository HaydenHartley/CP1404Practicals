def main():
    name_input, name_length = get_name()
    print (name_input[1:name_length:2])


def get_name():
    name_input = input("enter your name: ")
    while len(name_input) < 1:
        name_input = input("enter your name: ")
    name_length = len(name_input)
    return name_input, name_length


main()