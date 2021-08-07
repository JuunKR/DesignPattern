'''
클래스는 하나의 책임만 가진다.
하나의 클래스가 하는 일을 하나의 일을 담당하고 있다.
클래스를 변경해야 할 이유는 오직 한가지만이 존재한다.
'''

class Calculator(object):

    def calculate(self, sign, first_number, second_number):
        result = 0
        if sign == '+':
            result = first_number + second_number
            
        elif sign == '-':
            result = first_number - second_number

        #@ 새로 추가 
        elif sign == '*':
            result = first_number * second_number

        return result


        

        

    
 

