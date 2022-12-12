class Rectangle:
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height

    def getArea(self):
        return(self.width * self.height)
    def getPerimeter(self):
        return(2*(self.width+self.height))

def main():
    r1 = Rectangle(4,40)
    print("The width of the rectangle is {}".format(r1.width))
    print("The height of the rectangel is {}".format(r1.height))
    print("The area of the rectangle is {}".format(r1.getArea()))
    print("The perimeter of the rectangle is {}".format(r1.getPerimeter()))
    print("\n")
    r2 = Rectangle(3.5,35.7)
    print("The width of the rectangle is {}".format(r2.width))
    print("The height of the rectangel is {}".format(r2.height))
    print("The area of the rectangle is {}".format(r2.getArea()))
    print("The perimeter of the rectangle is {}".format(r2.getPerimeter()))
main()


