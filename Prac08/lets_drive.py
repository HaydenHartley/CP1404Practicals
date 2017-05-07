"""

"""

from Prac08.taxi import Taxi
from Prac08.taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

print("Let's drive!")
menuChoice = input("q)uit, c)hoice, d)rive\n>>> ").lower()
while menuChoice != 'q':
    if menuChoice == 'c':
        print("Taxis availiable")
        for taxi in taxis:
            print("{} - {}".format(taxis.index(taxi), taxi))
        taxiChoice = int(input("Choose taxi: "))
        taxi = taxis[taxiChoice]
        print("Bill to date: ${:.2f}".format(taxi.get_fare()))
    elif menuChoice == 'd':
        driveDistance = int(input("Drive how far? "))
        taxi.drive(driveDistance)
        print("Your {} trip cost you ${:.2f}".format(taxi.name, taxi.get_fare()))
        print("Bill to date: ${:.2f}".format(taxi.get_fare()))
    else:
        print("invalid choice")
    menuChoice = input("q)uit, c)hoice, d)rive\n>>> ").lower()
print("Taxis are now:")
for taxi in taxis:
    print("{} - {}".format(taxis.index(taxi), taxi))
