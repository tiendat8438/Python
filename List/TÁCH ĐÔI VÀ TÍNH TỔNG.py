def split_and_sum(number: str):
    while len(number) > 1:
        n = len(number)
        mid = n // 2
        first_half = int(number[:mid])
        second_half = int(number[mid:])
        number = str(first_half + second_half)
        print(number)

# Đọc số từ input
number = input().strip()
split_and_sum(number)
