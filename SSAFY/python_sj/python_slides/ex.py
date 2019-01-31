# 파일명 변경 금지
# 아래에 클래스 Point와 Circle을 선언하세요.

class Point:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r
    
    def get_area(self):
        return self.r**2*3.14
    
    def get_perimeter(self):
        return 2*self.r*3.14
    
    def get_center(self):
        return (self.center.x, self.center.y)
    
    def print(self):
        print(f'Circle : {self.get_center()}, r: {self.r}')






# 아래의 코드는 수정하지마세요. 
p1 = Point(0, 0)
c1 = Circle(p1, 3)
print(c1.get_area())
print(c1.get_perimeter())
print(c1.get_center())
c1.print()
p2 = Point(4, 5)
c2 = Circle(p2, 1)
print(c2.get_area())
print(c2.get_perimeter())
print(c2.get_center())
c2.print()