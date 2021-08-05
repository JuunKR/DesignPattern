class Barista:

    def __init__(self):
        # Barista의 멤버변수로 선언
        self.espresso_machine = None
    
    def set_espresso_machine(self, espresso_machine):
        self.espresso_machine = espresso_machine
    
    def make_espresso(self):
        return self.espresso_machine.make_espresso()




