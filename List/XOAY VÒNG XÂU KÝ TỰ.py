def min_steps(n, strings):
    L = len(strings[0])
    A = [strings[0][i:] + strings[0][:i] for i in range(L)] # Danh sách các xâu đã được xoay của 1 xâu target
    min_steps = float('inf')
    for target in A:
        steps = 0
        for s in strings:
            found = False
            for i in range(L):
                rotate_s = s[i:] + s[:i] # Xoay các xâu còn lại
                if rotate_s == target:
                    steps += i # Số bước cần đạt đến cấu hình target hiện tại là i
                    found = True
                    break
            if not found:
                return -1
        min_steps = min(min_steps, steps)
    return min_steps

def main():
    N = int(input())
    strings = [input() for _ in range(N)]
    print(min_steps(N, strings))

if __name__ == '__main__':
    main()
