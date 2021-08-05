from calculator import Calculator
from add_operation import AddOperation
from substract_operation import SubstractOperation
from multiply_operation import MultiplyOperation

class Client:
    
    def main(self):
        calculator = Calculator()
        
        calculator.set_add_operation(AddOperation())
        calculator.set_substract_operation(SubstractOperation())
        calculator.set_multiply_operation(MultiplyOperation())
        
        first_number = 100
        second_number = 20
        
        operator = "+"
        answer = calculator.calculate(operator, first_number, second_number)
        
        print(str(first_number) + operator + str(second_number) + " = " + str(answer))
        
        operator = "-"
        answer = calculator.calculate(operator, first_number, second_number)
        
        print(str(first_number) + operator + str(second_number) + " = " + str(answer))
        
        operator = "*"
        answer = calculator.calculate(operator, first_number, second_number)
        
        print(str(first_number) + operator + str(second_number) + " = " + str(answer))
        
client = Client()
client.main()
