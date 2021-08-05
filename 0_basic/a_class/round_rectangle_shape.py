class RoundRectangleShape:

    # 클래스 멤버변수
    shape_id_counter = 0 

    def __init__(self, x, y, width, height, arc_width, arc_height):
        self.x = x
        self.y = y
    
        self.width = width
        self.height = height
    
        self.arc_width = arc_width
        self.arc_height = arc_height
    
    def draw(self):
        print("draw RoundRectangle")

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

    def get_arc_width(self):
        return self.arc_width

    def set_arc_width(self, arc_width):
        self.arc_width = arc_width

    def get_arc_height(self):
        return self.arc_height

    def set_arc_height(self, arc_height):
        self.arc_height = arc_height
    
    @classmethod
    def get_shape_id_counter(cls):
        cls.shape_id_counter = cls.shape_id_counter + 1
        return cls.shape_id_counter
    
if __name__ == "__main__": 
    print(RoundRectangleShape.shape_id_counter)
    print(RoundRectangleShape.get_shape_id_counter())
    print(RoundRectangleShape.get_shape_id_counter())

    