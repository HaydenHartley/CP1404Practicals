"""
test taxi
CP1404 Practical
"""

from Prac08.taxi import Taxi

Prius = Taxi("Prius 1", 100, 1.20)
Prius.drive(40)
Prius.start_fare()
Prius.drive(100)
print(Prius.get_fare())
