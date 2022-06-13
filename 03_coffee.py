"""Component 2 of price comparison -
Price comparing of the cheapest and expensive coffee
Created by Francis Torcuato
"""

name = input("Please enter your name:")
print(f"hello {name}! - Welcome to price comparison ")

# Budget of the user
budget = input("Please enter your budget: ")
print(f"Your budget for coffee is ${budget}")

attempt = ""
while not attempt != "X":
    unit = input("Enter unit to be compared:")
    product = input("Please enter the product name:")
    unit_number = input("Enter the number of units:")
    price = input("Enter price:")

    attempt = input("Enter 'x' if you want to compare: ")

coffee = \
    [["Greggs", 7],
     ["Moconna", 10.49],
     ["Nescafe", 7.79]]

coffee.sort()

coffee.sort(key=lambda x: x[1])

for x in coffee:
    print(f"{coffee}")
