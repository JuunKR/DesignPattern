class Calculator:
    def __init__(self):
        self.operation = None
    
    def calculate(self, first_number, second_number):
        if self.operation.is_invalid_number(first_number, second_number):
            return -999

        answer = self.operation.operate(first_number, second_number)
        return answer


    def set_operation(self, operation):
        self.operation = operation

        
        
        