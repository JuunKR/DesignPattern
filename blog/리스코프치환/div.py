from abc import *


class Div(metaclass=ABCMeta):
    @staticmethod
    def operate(first_number, second_number):
        return first_number / second_number

    @staticmethod
    def is_invalid_number(first_number, second_number):
        if second_number == 0:
            return True
        return False
        