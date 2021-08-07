from add import Add
from div import Div
from calculator import Calculator

class Interface(object):
    
    @staticmethod
    def main():
        calculator = Calculator()

        first_number = 100
        second_number = 0

        operation = Add()
        calculator.set_opertation(operation)
        result = calculator.calculate(first_number, second_number)
        print('정답은 : ', result)

        operation = Div()
        calculator.set_opertation(operation)
        result = calculator.calculate(first_number, second_number)
        print('정답은 : ', result)
            
            
        