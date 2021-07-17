from isubject import ISubject


class OperationSubject(ISubject):
    def __init__(self):
        self.first_number = 0
        self.second_number = 0
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def remove_observer(self, observer):
        index = self.observer.index(observer)
        if index >= 0:
            self.observers.remove(index)

    def set_number(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

        self.notify_observers()

    def get_first_number(self):
        return self.first_number

    def get_second_number(self):
        return self.second_number

