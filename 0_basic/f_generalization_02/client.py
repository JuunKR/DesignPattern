from coffee import Coffee
from espresso import Espresso

class Client:

    def main(self):
        
        coffee = Coffee()

        print(coffee.get_name())
        
        coffee.display()

        espresso = Espresso()
        espresso.set_name("Espresso")

        print(espresso.get_name())
        
        espresso.display()
        
client = Client()
client.main()
