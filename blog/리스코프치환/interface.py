from calculator import Calculator
from add import Add
from substract import Substract
from mul import Mul
from div import Div

class Interface(object):
    @staticmethod
    def main():
        calculator = Calculator()

        first_number = 200
        second_number = 0

        operation = Add()
        calculator.set_operation(operation)
        result = calculator.calculate(first_number, second_number)
        print(f'{first_number} + {second_number} = {result}')

        operation = Substract()
        calculator.set_operation(operation)
        result = calculator.calculate(first_number, second_number)
        print(f'{first_number} - {second_number} = {result}')

        #@ 추가
        operation = Mul()
        calculator.set_operation(operation)
        result = calculator.calculate(first_number, second_number)
        print(f'{first_number} * {second_number} = {result}')

        operation = Div()
        calculator.set_operation(operation)
        result = calculator.calculate(first_number, second_number)
        print(f'{first_number} / {second_number} = {result}')




if __name__ == '__main__':
    interface = Interface()
    interface.main()




