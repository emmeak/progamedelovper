#parent class
class person():
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def dis_play(self):
        print(f"Very Human name is {self.name}")
        print(f"Totally Real address is {self.address}")
    
#child class
class employee(person):
    def __init__(self, name, address, salary, position):
        person.__init__(self, name, address) 
        self.salary = salary
        self.position = position
    def dee(self):
        print(f"Yep, this is a Human called {self.name}")
        print(f"This salary is... {self.salary}")
        print(f"Their position is, that -> {self.position}")

eeeeeeee = employee("Gref. J", "123 Ontheplane Of Existence Road", "Five Thousand Annually", "Chicken Noodle Soup Salesman")
eeeeeeeee = person("Dercabaskin hr Goostsengob \nAKA Derick Goodworth", "Street Lane for Humans Who Totally Aren't Aliens Who Eat Human Flesh (HWTAAWEHF)")

eeeeeeee.dee()
print("*"*50)
eeeeeeeee.dis_play()