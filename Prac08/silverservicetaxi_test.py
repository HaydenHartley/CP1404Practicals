from Prac08.taxi import SilverServiceTaxi

Hummer = SilverServiceTaxi("Hummer", 200, 2)
print(Hummer)
Hummer.start_fare()
Hummer.drive(10)
print(Hummer.get_fare())
