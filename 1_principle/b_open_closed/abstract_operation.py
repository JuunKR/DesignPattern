from abc import abstractmethod, ABCMeta

class AbstractOperation(metaclass=ABCMeta):
    
    @abstractmethod
    def operate(self, first_number, second_number):
        pass
    
 