from collections import Counter
import math
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    filtered = [num for num in A if is_prime(num)]
    counter = Counter(filtered)
    for key, val in counter.items():
        print(key, val)