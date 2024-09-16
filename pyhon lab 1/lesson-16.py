grocery_list = ["egg", "rice", "bread", "sugar"]
print(grocery_list)

print(grocery_list[0])
print(grocery_list[1])
print(grocery_list[-1])
print(grocery_list[-2])

print(grocery_list[2:])
print(grocery_list[:2])
print(grocery_list[1:2])

grocery_list[1] = "oil"
print(grocery_list)

price = [10, 20, 15, 30]
max_price = price[0]

for value in price:
    if value > max_price:
        max_price = value

print(max_price)
