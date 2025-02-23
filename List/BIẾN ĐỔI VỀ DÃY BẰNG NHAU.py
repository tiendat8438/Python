def min_steps(A):
    unq = list(dict.fromkeys(A)) # Trả về danh sách các giá trị duy nhất trong mảng theo thứ tự
    min_steps = float('inf')
    chosen_val = None # Gía trị được chọn để biến đổi về
    for target in unq:
        steps = sum(abs(x - target) for x in A)
        if steps < min_steps:
            min_steps = steps
            chosen_val = target
    return min_steps, chosen_val

N = int(input())
A = list(map(int, input().split()))
steps, val = min_steps(A)
print(f'{steps} {val}')


