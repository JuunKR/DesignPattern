from calculator import Calculator
from add import Add
from substract import Substract
from mul import Mul

class Interface(object):
    @staticmethod
    def main():
        calculator = Calculator()

        calculator.set_add(Add())
        calculator.set_sub(Substract())
        #@ 추가
        calculator.set_mul(Mul())

        first_number = 200
        second_number = 100

        operator = '+'
        result = calculator.calculate(operator, first_number, second_number)
        print(f'{first_number} + {second_number} = {result}')

        operator = '-'
        result = calculator.calculate(operator, first_number, second_number)
        print(f'{first_number} - {second_number} = {result}')

        #@ 추가 
        operator = '*'
        result = calculator.calculate(operator, first_number, second_number)
        print(f'{first_number} * {second_number} = {result}')


if __name__ == '__main__':
    interface = Interface()
    interface.main()