from itertools import combinations
from math import sqrt

EPSILON = 1e-9  # Small margin for floating-point precision issues

class Point:
    """Represents a point on the Oxy plane"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_squared(self, other):
        """Returns the squared distance between two points"""
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

class Circle:
    """Represents a circle on the Oxy plane"""
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    @classmethod
    def from_three_points(cls, A, B, C):
        """Constructs a circle from three non-collinear points"""
        x1, y1 = A.x, A.y
        x2, y2 = B.x, B.y
        x3, y3 = C.x, C.y

        det = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        if det == 0:
            return None  # Points are collinear

        a = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / det
        b = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / det
        center = Point(a, b)
        radius = sqrt(center.distance_squared(A))  # Radius of the circle

        return cls(center, radius)

    def contains(self, point):
        """Returns True if the point is strictly inside the circle"""
        return self.center.distance_squared(point) < self.radius ** 2 - EPSILON

class Solver:
    """Solves the problem by checking all circle candidates"""
    def __init__(self, points, K):
        self.points = points
        self.K = K

    def solve(self):
        """Determines whether a valid circle exists"""
        for A, B, C in combinations(self.points, 3):
            circle = Circle.from_three_points(A, B, C)
            if circle:
                count = sum(1 for p in self.points if p not in [A, B, C] and circle.contains(p))
                if count == self.K:
                    return "YES"
        return "NO"

# Processing input
T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())  # Number of points
    K = int(input())  # Required number of enclosed points
    points = [Point(*map(int, input().split())) for _ in range(N)]  # Read N points

    solver = Solver(points, K)
    print(solver.solve())
