"""Component 5 of price comparison
The program should give the user the best price recommended
Created by francis
"""

price_per_unit = input(f"The cost price of the product is ${price} and the unit price is {unit_number}{unit}")
print(price_per_unit)


coffee = \
    [["Greggs",7],
     ["Moconna",10.49],
     ["Nescafe",7.79]]

coffee.sort()

coffee.sort(key=lambda x: x[1])

for x in coffee:
    print("coffee")











    








