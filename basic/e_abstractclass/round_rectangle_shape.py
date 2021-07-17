from abstract_bounding_shape import AbstractBoundingShape


# 추상클래스를 상속한다.
class RoundRectangleShape(AbstractBoundingShape):

    def __init__(self, *args):
        super().__init__(*args)
        self.arc_width = 0
        self.arc_height = 0
    
    # 추상메서드를 오버라이딩하여 기능을 확장
    def draw(self):
        print("draw RoundRectangle")

    def get_arc_width(self):
        return self.arc_width

    def set_arc_width(self, arc_width):
        self.arc_width = arc_width

    def get_arc_height(self):
        return self.arc_height

    def set_arc_height(self, arc_height):
        self.arc_height = arc_height

