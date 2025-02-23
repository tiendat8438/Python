if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, d = map(int, input().split())
        arr = list(map(int, input().split()))
        rotate_arr = arr[d:] + arr[:d]
        print(*rotate_arr)