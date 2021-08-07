from calculator import Calculator
from add import Add

class Interface(object):
    @staticmethod
    def main():
        calculator = Calculator()

        first_number = 200
        second_number = 100
        
        operation = Add()
        calculator.set_operation(operation)
        result = calculator.calculate(first_number, second_number)

        print(f'{first_number} + {second_number} = {result}')
