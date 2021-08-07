from display_client import DisplayClient
from calculator import Calculator
from add import Add 
from calc_client import CalcClient

class Client():
    @staticmethod
    def main():
        first_number = 100
        second_number = 20

        calculator = Calculator()

        operation = Add()

        calc_client = CalcClient()

        result = calc_client.request(calculator, operation, first_number, second_number)

        print('RESLUT = ', result)

        display_client = DisplayClient()

        display_client.request(calculator, operation, first_number, second_number)
