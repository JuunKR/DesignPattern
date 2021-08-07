class CalcClient:

    def request(self, calculator, operation, first_number, second_number):
        
        calculator.set_operation(operation)

        result = calculator.calculate(first_number, second_number)

        return result



