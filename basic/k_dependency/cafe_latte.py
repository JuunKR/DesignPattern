class CafeLatte:

    def __init__(self):
        self.name = "CafeLatte"
        
        # CafeLatte의 멤버변수로 선언
        self.espresso = None
        self.milk = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # CafeLatte의 멤버변수를 외부에서 설정하는 메서드
    def set_espresso(self, espresso):
        self.espresso = espresso

    def set_milk(self, milk):
        self.milk = milk
    
    def display(self):
        print(self.name + " (" + str(self.espresso) + " + " + str(self.milk) + ")")
    
    def __str__(self):
        return "CafeLatte"

    