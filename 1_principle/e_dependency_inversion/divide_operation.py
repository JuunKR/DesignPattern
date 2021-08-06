from abstract_operation import AbstractOperation

class DivideOperation(AbstractOperation):
    
    def operate(self, first_number, second_number):
        answer = first_number / second_number
        
        return answer
