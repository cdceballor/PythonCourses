import random

class Box():

    def select(self, value):
        if value == 0:
            draw(value)
        elif value == 1:
            draw(value)
        elif value == 2:
            draw(value)
        elif value == 3:
            draw(value)
        elif value == 4:
            draw(value)
        elif value == 5:
            draw(value)
        elif value == 6:
            draw(value)
        elif value > 6:
            print("Error, valor muy grande")
    
    def draw(self, value):
        if value == 0:
            print("""
            ___________________
            |    _________    |
            |   |    _    |   |
            |   |   | |   |   |
            |   |   | |   |   |
            |   |   |_|   |   |
            |   |_________|   |
            |_________________|
            """)
        elif value == 1:
            print("""
            ___________________
            |      ____       |
            |     /    |      |
            |    /_/|  |      |
            |       |  |      |
            |       |  |      |
            |       |__|      |
            |_________________|
            """)
        elif value == 2:
            print("""
            ___________________
            |      ____       |
            |     /    |      |
            |    /_/|  |      |
            |      /  /       |
            |     |  |___     |
            |     |______|    |
            |_________________|
            """)
        elif value == 3:
            print("""
            ___________________
            |      ____       |
            |     |__  |      |
            |      _|  |      |
            |     |_   |      |
            |      _|  |      |
            |     |____|      |
            |_________________|
            """)
        else:
            print("valor mayor a 3")
            print("""
            ___________________
            |                  |
            |    (ง ͠° ͟ل͜ ͡°)ง    | ERROR - VALOR MAYOR A 3
            |                  |
            |__________________|
            """)


def executor():
    n = random.randint(0,4)
    dice = Box().draw(n)

executor()