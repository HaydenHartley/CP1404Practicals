from Prac07.guitar import Guitar

print("My guitars!")

myGuitars = []

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = int(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    myGuitars.append(guitar)
    print("{} ({}) : ${} added.".format(guitar.name, guitar.year, guitar.cost))
    name = input("Name: ")

myGuitars.append(Guitar("Gibson L-5 CES", 1992, 16035.40))
myGuitars.append(Guitar("Line 6 JTV", 2010, 1512.9))

i = 0
for guitar in myGuitars:
    if guitar.is_vintage():
        vintage_string = "(Vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>15} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                               vintage_string))
    i += 1
