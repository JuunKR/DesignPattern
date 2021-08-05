from espresso import Espresso

class Client:

    def main(self):
        
        espresso = Espresso()
        
        print(espresso.get_name())
        
        espresso.display()

client = Client()
client.main()
