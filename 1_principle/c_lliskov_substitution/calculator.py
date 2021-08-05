class Calculator:
    
    def calculate(self, operation, first_number, second_number):
        if operation.is_invalid_number(first_number, second_number):
            return -999
        
        answer = operation.operate(first_number, second_number)
        
        return answer
