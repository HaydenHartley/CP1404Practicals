from Prac07.guitar import Guitar

print("My guitars!")

guitars = []


name = input("Name: ")
while name != "":
    guitar = Guitar()
    guitar.name = name
    guitar.year = int(input("Year: "))
    guitar.cost = int(input("Cost: $"))
    print("{} ({}) : ${} added.".format(guitar.name, guitar.year, guitar.cost))
    guitars.append(guitar)
    name = input("Name: ")
print(guitars)