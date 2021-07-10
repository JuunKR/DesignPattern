from abstract_operation_observer import AbstractOperationObserver


class DivideOperationObserver(AbstractOperationObserver):
    def __init__(self, operation_subject):
        AbstractOperationObserver.__init__(self, operation_subject)

    def update(self):
        first_number = self.get_first_number()
        second_number = self.get_second_number()

        answer = first_number / second_number

        print(first_number, " / ", second_number, ' = ', answer)