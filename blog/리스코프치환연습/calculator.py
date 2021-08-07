class Calculator(object):

    def __init__(self):
        self.operation = None

    def calculate(self, first_number, second_nubmer):
        if self.operation.is_invalid_number(first_number, second_nubmer):
            return -999

        result = self.operation.operate(first_number, second_nubmer)

        return result


    def set_opertation(self, operation):
        self.operation = operation