class Calculator:
     
    def __init__(self):
        self.add_operation = None
        self.substract_operation = None
        self.multiply_operation = None
    
    def calculate(self, operator, first_number, second_number):
        answer = 0
        
        if operator == "+":
            answer = self.add_operation.operate(first_number, second_number)
        elif operator == "-":
            answer = self.substract_operation.operate(first_number, second_number)
        elif operator == "*":
            answer = self.multiply_operation.operate(first_number, second_number)
        
        return answer

    def set_add_operation(self, operation):
        self.add_operation = operation

    def set_substract_operation(self, substract_operation):
        self.substract_operation = substract_operation

    def set_multiply_operation(self, multiply_operation):
        self.multiply_operation = multiply_operation
