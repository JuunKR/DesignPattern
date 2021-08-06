class DisplayClient:
    
    def request(self, calculator, operation, first_number, second_number):
        
        calculator.new_display(operation, first_number, second_number)
