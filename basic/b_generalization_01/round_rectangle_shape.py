from rectangle_shape import RectangleShape

class RoundRectangleShape(RectangleShape):
 
    def __init__(self, arc_width, arc_height):
        self.arc_width = arc_width
        self.arc_height = arc_height
    
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



if __name__ == '__main__':
    shape = RoundRectangleShape(1,2)
    # 오버라이딩
    shape.draw()
    