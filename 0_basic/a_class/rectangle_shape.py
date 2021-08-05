class RectangleShape:
    
    # 생성자
    def __init__(self, x, y, width, height):
    
        # 멤버 변수
        self.x = x
        self.y = y
        
        self.width = width
        self.height = height

    # 메서드
    def draw(self):
        return ("draw Rectangle")

    def get_x(self):
        return self.x
    
    def set_x (self, x):
        self.x = x
    
    def get_y(self):
        return self.y
    
    def set_y (self, x):
        self.y = y
    
    def get_width(self):
        return self.width
    
    def set_x (self, width):
        self.width = width
    
    def get_height(self):
        return self.height
    
    def set_x (self, height):
        self.height = height
    