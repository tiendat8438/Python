class matrix:
    def __init__(self, data):
        self.data = data
        self.n = len(data)  # Số hàng
        self.m = len(data[0]) if data else 0  # Số cột (kiểm tra rỗng)

    def chuyen_vi(self):
        trans = [[self.data[j][i] for j in range(self.n)] for i in range(self.m)]
        return matrix(trans)

    def tich(self, other):
        if self.m != other.n:
            return None  # Không thể nhân hai ma trận

        res = [[0] * other.m for _ in range(self.n)]
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    res[i][j] += self.data[i][k] * other.data[k][j]
        return matrix(res)

    def hien_thi(self):
        for row in self.data:
            print(" ".join(map(str, row)))

if __name__ == "__main__":
    t = int(input())  # Số test case
    for _ in range(t):
        while True:
            line = input().strip()
            if line:
                n, m = map(int, line.split())
                break

        mat = []
        for _ in range(n):
            row = list(map(int, input().strip().split()))
            mat.append(row)

        p = matrix(mat)
        transpose_mat = p.chuyen_vi()
        res = p.tich(transpose_mat)

        if res:
            res.hien_thi()
