from abstract_bounding_shape import AbstractBoundingShape


# 추상 클래스를 상속한다.
class RectangleShape(AbstractBoundingShape):

    def __init__(self, *args):
        super().__init__( *args)

    # 추상 메서드를 오버라이딩하여 기능을 확장한다.
    def draw(self):
        print("draw Rectangle")






