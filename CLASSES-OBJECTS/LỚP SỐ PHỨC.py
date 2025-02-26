class SoPhuc:
    def __init__(self, A, B):
        self.A = complex(A[0], A[1])
        self.B = complex(B[0], B[1])

    def format_complex(self, z):
        real = int(z.real)
        imag = int(z.imag)
        sign = "+" if imag >= 0 else "-"
        return f"{real} {sign} {abs(imag)}i"
    
    def bieu_thuc(self):
        C = (self.A + self.B) * self.A
        D = (self.A + self.B) ** 2
        return self.format_complex(C) + ", " + self.format_complex(D)

if __name__ == "__main__": 
    for _ in range(int(input())):
        data = []
        while len(data) < 4:
            line = input().strip()
            if line:
                data.extend(map(int, line.split()))
        A = data[:2]
        B = data[2:]

        p = SoPhuc(A, B)
        print(p.bieu_thuc())
