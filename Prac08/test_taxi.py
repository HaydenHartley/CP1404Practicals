"""
test taxi
CP1404 Practical
"""

from Prac08.taxi import Taxi

prius = Taxi("Prius 1", 100)
prius.drive(40)
prius.start_fare()
prius.drive(100)
print(prius.get_fare())
