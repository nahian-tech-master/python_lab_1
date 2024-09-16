def total_cost(price, shipping, discount):
    total = price + shipping - discount
    print(f"Total cost: {total}")

total_cost(10, 5, 1)
total_cost(20, 5, 5)
total_cost(30, 5, 10)

def welcome(name):
    print(f"Hi {name}")

welcome("nurgeomon varikey")

def welcome(first_name, last_name):
    print(f"Hi {first_name} {last_name}")

welcome("nurgeomon", "faraki")
