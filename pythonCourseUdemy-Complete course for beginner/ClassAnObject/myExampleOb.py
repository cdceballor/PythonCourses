class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def displayNameAge(self):
        print("The pet with name {0} and age {1} could be yours ".format(self.name, self.age))
    
    
def giveNameAge():
    name = input("Write a name: ")
    age = input("Write a age: ")
    dog = Pet(name, age)
    dog.displayNameAge()

giveNameAge()