from add import Add
from substract import Substract

class Calculator(object):
    add = Add()
    sub = Substract()

   
    def calculate(self, sign, first_number, second_number):
        result = 0
        if sign == '+':
            result = self.add.operate(first_number, second_number)
        
        elif sign == '-':
            result = self.sub.operate(first_number, second_number)


        return result