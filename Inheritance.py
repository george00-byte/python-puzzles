class polygon():
    __width = None
    __length = None

    def set_values(self, length, witdh):
        self.__length = length
        self.__width = witdh

    def get__length(self):
        return self.__length

    def get__width(self):
        return self.__width


class Rectangle(polygon):
    def area(self):
        return self.get__length() * self.get__width()


class Triangle(polygon):
    def area(self):
        return 0.5*(self.get__length() * self.get__width())





rect=Rectangle()
tri=Triangle()
tri.set_values(40,50)
rect.set_values(40,50)
print("Area of Rectangle is ",rect.area())
print("Area of Triangle is ",tri.area())