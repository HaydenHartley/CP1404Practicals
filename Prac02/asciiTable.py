LOWER_VALUE = 33
UPPER_VALUE = 127

def main():

    character_input = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(character_input, ord(character_input)))

    number_input = int(input("Enter a between 33 and 127: "))
    while LOWER_VALUE > number_input & number_input > UPPER_VALUE:
        number_input = int(input("Invalid number. Enter a between {} and {}: ".format(LOWER_VALUE, UPPER_VALUE)))
    else:
        print("The character for {} is {}".format(str(character_input), chr(character_input)))

def get_number():


main()