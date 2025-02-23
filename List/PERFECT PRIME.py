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

def reverse_number(n):
    return int(str(n)[::-1])

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def all_digits_prime(n):
    prime_digits = {'2', '3', '5', '7'}
    return all(digit in prime_digits for digit in str(n))

def is_perfect_prime(n):
    return (is_prime(n) and
            is_prime(reverse_number(n)) and
            is_prime(sum_of_digits(n)) and
            all_digits_prime(n))

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        print("Yes" if is_perfect_prime(N) else "No")
