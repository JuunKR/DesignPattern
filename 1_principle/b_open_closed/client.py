from calculator import Calculator
from add_operation import AddOperation
from substract_operation import SubstractOperation
from multiply_operation import MultiplyOperation

class Client:
    
    def main(self):
        
        calculator = Calculator()
        
        first_number = 100
        second_number = 20
        
        operation = AddOperation()
        calculator.set_operation(operation)
        
        answer = calculator.calculate(first_number, second_number)
        
        print(str(first_number) + "+" + str(second_number) + " = " + str(answer))
        
        operation = SubstractOperation()
        calculator.set_operation(operation)
        
        answer = calculator.calculate(first_number, second_number)
        
        print(str(first_number) + "-" + str(second_number) + " = " + str(answer))
        
        operation = MultiplyOperation()
        calculator.set_operation(operation)
        
        answer = calculator.calculate(first_number, second_number)
        
        print(str(first_number) + "*" + str(second_number) + " = " + str(answer))
        
client = Client()
client.main()
