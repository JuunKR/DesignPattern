from calculator import Calculator
from add_operation import AddOperation
from substract_operation import SubstractOperation
from multiply_operation import MultiplyOperation
from divide_operation import DivideOperation

class Client:
    
    def main(self):
        
        calculator = Calculator()
        
        first_number = 100
        second_number = 20
        
        operation = AddOperation()
        answer = calculator.calculate(operation, first_number, second_number)
        
        print(str(first_number) + "+" + str(second_number) + " = " + str(answer))
        
        operation = SubstractOperation()
        answer = calculator.calculate(operation, first_number, second_number)
        
        print(str(first_number) + "-" + str(second_number) + " = " + str(answer))
        
        operation = MultiplyOperation()
        answer = calculator.calculate(operation, first_number, second_number)
        
        print(str(first_number) + "*" + str(second_number) + " = " + str(answer))
        
        second_number = 0
        operation = DivideOperation()
        
        answer = calculator.calculate(operation, first_number, second_number)
        
        print(str(first_number) + "/" + str(second_number) + " = " + str(answer))
        
client = Client()
client.main()
