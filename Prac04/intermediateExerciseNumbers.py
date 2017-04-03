NUMBER_OF_INPUTS = 5

numbers = []

for input_number in NUMBER_OF_INPUTS:
    number = int(input("enter number {} of {}:".format(input_number,NUMBER_OF_INPUTS)))
    numbers.append(number)

print("The first number is", (numbers[0]))
print("The last number is", format(numbers[-1]))
print("The smallest number is",(min(numbers)))
print("The largest number is", (max(numbers)))
print("The average of the numbers is", (sum(numbers)/len(numbers)))