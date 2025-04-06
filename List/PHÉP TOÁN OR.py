def solve(A, n):
    cur_set = set()
    uniq_vals = set()
    for i in range(n):
        new_set = {A[i]}
        for val in cur_set:
            new_set.add(val | A[i])
        cur_set = new_set
        uniq_vals.update(cur_set)
    return len(uniq_vals)


if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    print(solve(A, n))