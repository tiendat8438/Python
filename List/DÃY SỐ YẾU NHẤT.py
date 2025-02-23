N = int(input())
A = list(map(int, input().split()))

def weak(X):
    max_pos, min_neg = 0, 0 # Tổng con dương lớn nhất và trị tuyệt đối lớn nhất của tổng con âm
    cur_pos, cur_neg = 0, 0 # Tổng dương và âm ở dãy con hiện tại
    for num in A:
        b = num - X
        cur_pos += b
        cur_neg += b
        if cur_pos > 0:
            if cur_pos > max_pos:
                max_pos = cur_pos
        else:
            cur_pos = 0

        if cur_neg < 0:
            if cur_neg < min_neg:
                min_neg = cur_neg
        else:
            cur_neg = 0
    return round(max_pos, 6), round(-min_neg, 6)

def main():
    l, r = min(A), max(A)
    pos, neg = 1, 0
    while pos != neg:
        mid = (l + r) / 2
        pos, neg = weak(mid)
        if pos > neg: # Tổng dương lớn hơn âm -> giảm tổng dương
            l = mid
        else:
            r = mid
    print(f'{pos:.6f}')

main()
