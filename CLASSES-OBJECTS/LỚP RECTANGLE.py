class Rectangle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color.capitalize()
    def perimeter(self):
        return (self.x + self.y) * 2
    def area(self):
        return self.x * self.y
    def get_color(self):
        return self.color


if __name__ == '__main__':
    arr = input().split()
    length = int(arr[0])
    width = int(arr[1])
    color = arr[2]

    if length > 0 and width > 0:
        r = Rectangle(length, width, color)
        print(f"{r.perimeter()} {r.area()} {r.get_color()}")
    else:
        print("INVALID")