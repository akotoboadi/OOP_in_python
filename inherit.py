from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Triangle(Shape):
    def calculate_area(self,base,height):
        self.base = base
        self.height = height
        return (0.5*base*height)


class Rectangle(Shape):
    def calculate_area(self,length,width):
        self.length = length
        self.width  = width
        return(length*width)


triangle1 = Triangle()
print(triangle1.calculate_area(20,100))
rectangle1 = Rectangle()
print(rectangle1.calculate_area(2,8))
