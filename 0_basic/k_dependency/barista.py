from coffee_beans import CoffeeBeans
from milk import Milk
from cafe_latte import CafeLatte

class Barista:

    def __init__(self):
        # EspressoMachine 타입의 멤버변수 선언
        self.espresso_machine = None

    def set_espresso_machine(self, espresso_machine):
        self.espresso_machine = espresso_machine
    
    # Espresso 타입의 리턴값에 의존한다.
    def make_espresso(self):
        coffee_beans = CoffeeBeans()

        espresso = self.espresso_machine.make_espresso(coffee_beans)

        return espresso
    
    # Milk 타입의 지역변수값에 의존한다.
    def make_cafe_latte(self):
        coffee_beans = CoffeeBeans()

        espresso = self.espresso_machine.make_espresso(coffee_beans)
        milk = Milk()

        cafeLatte = CafeLatte()

        cafeLatte.set_espresso(espresso)
        cafeLatte.set_milk(milk)

        return cafeLatte
    
    def __str__(self):
        return "Barista"

