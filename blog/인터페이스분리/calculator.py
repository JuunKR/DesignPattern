from idisplayable import IDisplayable


class Calculator(IDisplayable):

    def __init__(self):
        self.operation = None

    def calculate(self, first_number, second_number):
        result = self.operation.operate(first_number, second_number)

        return result

    def set_operation(self, operation):
        self.operation = operation

    
    def new_display(self,operation,first_number, second_number):
        result = operation.operate(first_number, second_number)

        operator = operation.get_operator()

        print(f'{first_number} {operator} {second_number} = {result}')