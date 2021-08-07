class Calculator(object):

    def __init__(self):
        self.operation = None

    def calculate(self, first_number,second_number):
        self.operation.operate(first_number,second_number)
    
    def set_operation(self, operation):
        self.operation = operation