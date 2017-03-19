"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]\<>?{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(len(password)) + " character password is valid: " + password)


def is_valid_password(password):
    while len(password) > MAX_LENGTH or len(password) < MIN_LENGTH:
        print("Invalid Length")
        password = input("> ")


    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if str.islower(char):
            count_lower += 1
        elif str.isupper(char):
            count_upper += 1
        elif str.isdigit(char):
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1
        pass

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    if SPECIAL_CHARS_REQUIRED == True:
        if count_special == 0:
            return False

    # if we get here (without having returned False), then the password must be valid
    return True

main()