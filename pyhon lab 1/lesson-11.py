good_condition = True
reasonable_price = True

if good_condition and reasonable_price:
    print("We will buy the house")

good_condition = True
reasonable_price = False

if good_condition or reasonable_price:
    print("We are interested")

good_condition = True
poor_foundation = False

if good_condition and not poor_foundation:
    print("It is a good deal")
