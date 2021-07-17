from espresso import Espresso

class EspressoMachine:
    
    def __init__(self):
        self.price = 300000
    
    # CoffeBeans 타입의 함수인자값에 의존된다.
    def make_espresso(self, coffee_beans):
        print(coffee_beans)

        return Espresso()
    
    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def __str__(self):
        return "EspressoMachine"
