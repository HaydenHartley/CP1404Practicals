__author__ = 'hayden'

total_price = 0

number_of_items = int(input("Enter number of items: "))
while number_of_items <= 0:
    print("Invalid number of items")
    number_of_items = float(input("Enter number of items: "))

for i in range(number_of_items):
    total_price = total_price + float(input("Price of item: "))

if total_price > 100:
    total_price = total_price - total_price / 10
print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))
