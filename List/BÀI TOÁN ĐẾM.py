def find_missing_nums(A, n):
    if not A:  # Xử lý trường hợp không có dữ liệu đầu vào
        return False
    else:
        max_value = max(A)
        marked = [False] * (max_value + 1)

        for num in A:
            marked[num] = True

        missing_numbers = [i for i in range(1, max_value) if not marked[i]]

        if missing_numbers:
            return missing_numbers  # In tất cả các số bị thiếu
        else:
            return "Excellent!"

if __name__ == '__main__':
    while True:
        line = input().strip()
        if line:
            N = int(line)
            break
    A = []
    while len(A) < N:
        line = input().strip()
        if line:
            A.extend(map(int, line.split()))
    res = find_missing_nums(A, N)
    if res == 'Excellent!':
        print("Excellent!")
    else:
        for x in res:
            print(x)
    
    
    