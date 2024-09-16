class Keyboard:
    def __init__(self, language, connection):
        self.language = language
        self.connection = connection

my_keyboard = Keyboard(language='English', connection='Wireless')
print(my_keyboard.language)
print(my_keyboard.connection)

class AboutMe:
    def __init__(self, name, address, occupation):
        self.name = name
        self.address = address
        self.occupation = occupation

    def talk(self):
        print(f"My name is {self.name}. I'm from {self.address}. I am a {self.occupation}.")

fairuki = AboutMe(name='Nujamun Faruki', address='Bangladesh', occupation='Teacher')
fairuki.talk()
