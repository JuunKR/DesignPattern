from abstract import Abstract


class Add(Abstract):

    @staticmethod
    def operate(first_number, second_number):
        result = first_number + second_number
        return result


        