"""Component 3 of price comparison
comparing the price of soft drinks
"""

budget = input("Please enter your budget: ")
print(f"Your budget is ${budget}")

attempt = ""
while attempt != "X":
    attempt = input("Please enter the product you want?")
    cost_price = input("How much for the product? ")
    print(f"The cost of the product is ${cost_price}")
    mass = input("What is the volume?")
    print(f"The mass volume is {mass}L")
    print(f"The product that you want is {attempt} for {mass}L and cost ${cost_price}")
    compare_price = input("Press 'X' if you want to compare the  prices:")


    quality = float(input(f"How many {mass}L"))
    cost_price = float(input(f"How many ${cost_price}"))
    calculate_price = cost_price * quality
















    








