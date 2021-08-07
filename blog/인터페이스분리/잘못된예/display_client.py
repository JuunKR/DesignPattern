class DisplayClient():
    def request(self, calculator, operation, first_number, second_number):
        calculator.set_operation(operation)

        calculator.display(first_number, second_number)