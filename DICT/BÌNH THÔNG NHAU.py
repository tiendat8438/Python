from collections import defaultdict
import sys
class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = defaultdict(int)
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1
            return x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rooty] < self.rank[rootx]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1

input = sys.stdin.read
data = input().splitlines()
q = int(data[0])
dsu = DSU()
for i in range(1, q + 1):
    x, y, z = map(int, data[i].split())
    if z == 1:
        dsu.union(x, y)
    else:
        print("1" if dsu.find(x) == dsu.find(y) else "0")
        