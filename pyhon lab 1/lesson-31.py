class Laptop:
    def parts(self):
        print("keyboard, display, motherboard")

my_laptop = Laptop()
my_laptop.parts()

class Desktop(Laptop):
    pass

my_desktop = Desktop()
my_desktop.parts()

class Desktop(Laptop):
    def wait(self):
        print("desktops are heavyweight")

my_desktop = Desktop()
my_desktop.parts()
my_desktop.wait()
