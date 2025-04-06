import sys

def normalize(A):
    sorted_vals = sorted(set(A))
    mapping = {val: idx + 1 for idx, val in enumerate(sorted_vals)}
    return [mapping[val] for val in A]

input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
A = [list(map(int, data[i + 1].split())) for i in range(n)]

row_mapping = [normalize(row) for row in A]
col_mapping = [normalize([A[i][j] for i in range(n)]) for j in range(m)]

B = [[max(row_mapping[i][j], col_mapping[j][i]) for j in range(m)] for i in range(n)]

distinct_vals = len(set(val for row in B for val in row))
print(distinct_vals)