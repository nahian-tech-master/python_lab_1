class Keyboard:
    def definition(self):
        print("Keyboard is an input device")

    def number_of_keys(self):
        print("There are 101 keys")

my_keyboard = Keyboard()
my_keyboard.definition()
my_keyboard.number_of_keys()

my_keyboard.brand = "Logitech"
print(my_keyboard.brand)

new_keyboard = Keyboard()
new_keyboard.definition()

new_keyboard.brand = "Dell"
print(new_keyboard.brand)
