from abc import abstractmethod, ABCMeta


# 추상 클래스를 정의한다. abc == abstract base class
class AbstractBoundingShape(metaclass=ABCMeta):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        
        self.width = width
        self.height = height
    
    # 추상 메서드를 선언한다.
    @abstractmethod
    def draw(self):
        pass

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height


