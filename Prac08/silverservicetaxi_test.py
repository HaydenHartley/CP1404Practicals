from Prac08.taxi import SilverServiceTaxi

hummer = SilverServiceTaxi("Hummer", 200, 2)
print(hummer)
hummer.start_fare()
hummer.drive(10)
print(hummer.get_fare())
