

budget = int(input("Please enter your budget: "))
price = int(input("Please enter price: "))

if budget >= price:
    print("You have enough money to buy thing")
else:
    print("You need", price - budget)