from rectangle_shape import RectangleShape

class RoundRectangleShape(RectangleShape):

    def __init__(self):
        RectangleShape.__init__(self)
        self.arc_width = 0
        self.arc_height = 0
    
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
  
if __name__ == "__main__":      
    rectangle_shape = RectangleShape()
    rectangle_shape.draw()
    
    round_rectangle_shape = RoundRectangleShape()
    round_rectangle_shape.draw()

    
