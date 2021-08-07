from abc import *

class Abstract_operate(metaclass=ABCMeta):
    
    @abstractmethod
    def operate():
        pass
    
    def is_invalid_number(self, first_nubmer, second_number):
        return False
        
