class Calculator:

    def __init__(self):
        self.operation = None

    def calculate(self, first_number, second_number):
        result = self.operation.operate(first_number, second_number)

        return result

    def set_operation(self, operation):
        self.operation = operation

    
    def display(self, first_number, second_number):
        result = self.operation.operate(first_number, second_number)

        operator = self.operation.get_operator()

        print(f'{first_number} {operator} {second_number} = {result}')