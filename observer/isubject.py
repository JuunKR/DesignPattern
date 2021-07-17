from abc import ABCMeta, abstractmethod


class ISubject(metaclass=ABCMeta):
    
    @abstractmethod
    def notify_observers(self):
        pass

    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

