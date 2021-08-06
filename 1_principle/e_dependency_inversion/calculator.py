class Calculator:

    def __init__(self):
        self.operation = None    

    def calculate(self, first_number, second_number):
        answer = self.operation.operate(first_number, second_number)
        
        return answer

    def set_operation(self, operation):
        self.operation = operation
