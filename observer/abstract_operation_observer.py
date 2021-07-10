from abc import ABCMeta, abstractmethod


class AbstractOperationObserver(metaclass=ABCMeta):

    def __init__(self, operation_subject):
        self.operation_subject = operation_subject

    @abstractmethod
    def update(self):
        pass

    def get_first_number(self):
        return self.operation_subject.get_first_number()

    def get_second_number(self):
        return self.operation_subject.get_second_number()
