name_input = input("enter your name: ")
while len(name_input) < 1:
    name_input = input("enter your name: ")
name_length = len(name_input)
print (name_input[1:name_length:2])
