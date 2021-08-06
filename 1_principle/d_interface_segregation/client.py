from calculator import Calculator
from add_operation import AddOperation
from calc_client import CalcClient
from display_client import DisplayClient

class Client:
    
    def main(self):
        
        first_number = 100
        second_number = 20
        
        calculator = Calculator()
        
        operation = AddOperation()
        
        calc_client = CalcClient()
        
        answer = calc_client.request(calculator, operation, first_number, second_number)
        
        print("answer = " + str(answer))
        
        display_client = DisplayClient()
        
        display_client.request(calculator, operation, first_number, second_number)
       
client = Client()
client.main() 
