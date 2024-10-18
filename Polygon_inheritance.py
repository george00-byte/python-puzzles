class polygon():
    __width = None
    __length = None

    def set_values(self, length, width):
        self.__length = length
        self.__width = width

    def get__length(self):
        return self.__length

    def get__width(self):
        return self.__width


class Rectangle(polygon):
    def area(self):
        return self.get__length() * self.get__width()


class Triangle(polygon):
    def area(self):
        return self.get__length() * self.get__width()


tri = Triangle()
rec = Rectangle()
rec.set_values(30, 40)
print(rec.area())

