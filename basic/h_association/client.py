from barista import Barista
from espresso_machine import EspressoMachine

class Client:

    def main(self):
        barista = Barista()

        espresso_machine = EspressoMachine()

        barista.set_espresso_machine(espresso_machine)

        espresso = barista.make_espresso()

        espresso.display()
        
client = Client()
client.main()
