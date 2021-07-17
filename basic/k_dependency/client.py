from barista import Barista
from espresso_machine import EspressoMachine

class Client:

    def main(self):
        barista = Barista()

        espresso_machine = EspressoMachine()

        barista.set_espresso_machine(espresso_machine)
        
        espresso = barista.make_espresso()
        print(((((((((((((espresso)))))))))))))

        cafe_latte = barista.make_cafe_latte()

        cafe_latte.display()
        
client = Client()
client.main()
