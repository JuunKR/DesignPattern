from abstract import Abstract


class Div(Abstract):

    @staticmethod
    def operate(first_number, second_number):
        result = first_number / second_number
        return result

    @staticmethod
    def is_invalid_number(first_nuber,second_number):
        if second_number == 0:
            return True
        return False