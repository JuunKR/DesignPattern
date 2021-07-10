from divide_operation_observer import DivideOperationObserver
from multiply_operation_observer import MultiplyOperationObserver
from substratct_operation_observer import SubstractOperationObserver
from add_operation_observer import AddOperationObserver
from operation_subject import OperationSubject


class Client:

    def main(self, a, b):
        operation_subject = OperationSubject()

        add_observer = AddOperationObserver(operation_subject)
        substract_observer = SubstractOperationObserver(operation_subject)
        multiply_observer = MultiplyOperationObserver(operation_subject)
        divide_observer = DivideOperationObserver(operation_subject)

        operation_subject.register_observer(add_observer)
        operation_subject.register_observer(substract_observer)
        operation_subject.register_observer(multiply_observer)
        operation_subject.register_observer(divide_observer)

        first_number = a
        second_number = b

        operation_subject.set_number(first_number, second_number)

client = Client()
client.main(100, 20)
