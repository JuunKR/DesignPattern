from abc import *

class Abstract(metaclass=ABCMeta):
    @abstractmethod
    def operate(fisrt_number, second_number):
        pass
    
    @abstractmethod
    def get_operator():
        pass
