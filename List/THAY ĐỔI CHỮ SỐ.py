import sys

def find_max(x1, x2, p, q):
    max_numb = max(p, q)
    min_numb = min(p, q)
    x1 = ''.join([str(max_numb) if digit == str(min_numb) else digit for digit in x1])
    x2 = ''.join([str(max_numb) if digit == str(min_numb) else digit for digit in x2])
    return int(x1) + int(x2)

def find_min(x1, x2, p, q):
    max_numb = max(p, q)
    min_numb = min(p, q)
    x1 = ''.join([str(min_numb) if digit == str(max_numb) else digit for digit in x1])
    x2 = ''.join([str(min_numb) if digit == str(max_numb) else digit for digit in x2])
    return int(x1) + int(x2)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        p, q = map(int, input().split())
        nums = input().split()
        # input nhập vào cùng dòng và khác dòng
        if len(nums) == 2:
            x1, x2 = nums
        else:
            x1 = nums[0]
            x2 = input()
        print(find_min(x1, x2, p, q), find_max(x1, x2, p, q))
