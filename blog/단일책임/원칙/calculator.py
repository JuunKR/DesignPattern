class Calculator:
    def __init__(self):
        self.add = None
        self.sub = None
        self.mul = None
    
    def calculate(self, sign, first_number, second_number):
        answer = 0
        if sign == '+':
            answer = self.add.operate(first_number, second_number)
        elif sign == '-':
            answer = self.sub.operate(first_number, second_number)
        
        #@추가
        elif sign == '*':
            answer = self.mul.operate(first_number, second_number)

        return answer

    def set_add(self, operation):
        self.add = operation
    
    def set_sub(self, operation):
        self.sub = operation
    
        
    def set_mul(self, operation):
        self.mul = operation
        
        
        