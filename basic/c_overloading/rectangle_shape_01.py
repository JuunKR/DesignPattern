class RectangleShape:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    # 클래스 내에서 같은 이름의 메서드 불가능
    def draw_rectangle(self):
        print("draw Rectangle")
    
    def draw_round_rectangle(self, arc_width, arc_height):
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
