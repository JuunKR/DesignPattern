from test import AbstractOperation

class AddOperation(AbstractOperation):
    
    def operate(self, first_number, second_number):
        answer = first_number + second_number
        
        return answer
    

class DivideOperation(AbstractOperation):
    
    def is_invalid_number(self, first_number, second_number):
        if second_number == 0:
            return True
        
        return False
    
    def operate(self, first_number, second_number):
        answer = first_number / second_number

        return answer

class Calculator:
    
    def calculate(self, operation, first_number, second_number):
        if operation.is_invalid_number(first_number, second_number):
            return -999
        
        answer = operation.operate(first_number, second_number)
        
        return answer

if __name__ == '__main__':
     a = AddOperation()
     d = DivideOperation()
     c = Calculator()

     operation1 = a
     operation2 = d
    
    
     print(c.calculate(operation1,100,0))


         
    