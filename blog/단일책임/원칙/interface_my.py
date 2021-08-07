from calculator_my import Calculator

class Interface(object):
    
    @staticmethod
    def main():
        calculator = Calculator()

        first_number = 200
        second_number = 100

        sign = "+"
        result = calculator.calculate(sign, first_number, second_number)
        print(f'{first_number} + {second_number} = {result}')

        sign = "-"
        result = calculator.calculate(sign, first_number, second_number)
        print(f'{first_number} - {second_number} = {result}')


if __name__ == '__main__':
    interface = Interface()
    interface.main()
        