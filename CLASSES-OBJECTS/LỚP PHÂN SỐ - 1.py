from math import gcd

class phanso:
    def __init__(self, tuso, mauso):
        self.x = tuso
        self.y = mauso
    def toigian(self):
        gcd_chung = gcd(self.x, self.y)
        self.x = self.x // gcd_chung
        self.y = self.y // gcd_chung
        return f'{self.x}/{self.y}'

if __name__ == "__main__":
    data = input().split()
    p = phanso(int(data[0]), int(data[1]))
    print(p.toigian())
        