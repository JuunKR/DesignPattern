from espresso import Espresso
from milk import Milk

class CafeLatte:

    def __init__(self):
        self.name = "CafeLatte"
        
        # CafeLatte의 멤버변수로 선언하고 객체를 생성
        self.espresso = Espresso()
        self.milk = Milk()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def display(self):
        print(self.name + " (" + str(self.espresso) + " + " + str(self.milk) + ")")
    
    def __str__(self):
        return "CafeLatte"
