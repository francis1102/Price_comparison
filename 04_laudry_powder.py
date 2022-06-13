"""

"""

def surf_powder():
    unit = input("Unit to be compared: ")
    cost_price = input("How much for the product? ")
    volume = input("What is the volume of the product? ")
    print(f"The cost price is ${cost_price} with the volume of {volume}kg")


def Earthon_powder():
    product = input("Unit to be compared: ")
    cost_price = input("How much for the product? ")
    volume = input("What is the volume of the product? ")
    print(f"The cost_price ${cost_price} with the volume of {volume}")


def Yours_powder():
    product = input("Please enter the product: ")
    cost_price = input("How much for the product? ")
    volume = input("What is the volume of the product? ")
    print(f"The product is {product} and it is ${cost_price} with the volume of {volume}")


def calc_unit_price():
    calc_price = Yours_powder * surf_powder * Earthon_powder
    print(calc_unit_price)


def quit_programme():
    print("Goodbye")


laundry_powder = []
choice = 0


while choice != 5:
    print()
    print("1 Surf ")
    print("2 Earthon ")
    print("3 Yours ")
    print("4 calc_unit_price ")
    print("5 Exit the system")
    print()
    choice=int(input("Enter your choice (number between 1 and 5): "))
    print()


    if choice == 1:
        surf_powder()
    elif choice == 2:
       Earthon_powder()
    elif choice == 3:
        Yours_powder()
    elif choice == 4:
        calc_unit_price()
    elif choice == 5:
        quit_programme()


    attempt = input("Enter 'x' if you want to compare: ")

def sorting_list():
    coffee = \
    [["Surf", 12],
     ["Earthon", 58.29],
     ["Yours", 19.95]]

coffee.sort()

coffee.sort(key=lambda x: x[1])

for x in coffee:
    print(f"{coffee}")










    








