from abstract_operation import AbstractOperation

class DivideOperation(AbstractOperation):

    def is_invalid_number(self, first_number, second_number):
        if second_number == 0:
            return True
        
        return False
    
    def operate(self, first_number, second_number):
        answer = first_number / second_number

        return answer
