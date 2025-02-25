# from math import lcm
from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

class phanso:
    def __init__(self, tuso, mauso):
        self.x = tuso
        self.y = mauso

    def rutgon(self):
        ucln = gcd(self.x, self.y)
        self.x //= ucln
        self.y //= ucln

    def add(self, other):
        
        mauchung = lcm(self.y, other.y)
        tuso_tong = self.x * (mauchung // self.y) + other.x * (mauchung // other.y)
        tong = phanso(tuso_tong, mauchung)
        tong.rutgon()
        return tong

    def __str__(self):
        return f"{self.x}/{self.y}"
    
if __name__ == "__main__":
    data = input().split()
    p = phanso(int(data[0]), int(data[1]))
    q = phanso(int(data[2]), int(data[3]))
    print(p.add(q))