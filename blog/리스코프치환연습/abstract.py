from abc import *
from typing import AbstractSet

class Abstract(metaclass=ABCMeta):

    @abstractmethod
    def operate(first_number, second_number):
        pass

    @staticmethod
    def is_invalid_number(first_number, second_number):
        return False