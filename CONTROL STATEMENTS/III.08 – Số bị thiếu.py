import sys

n = int(input())

# Tính XOR của dãy từ 1 đến n
xor_all = 0
for i in range(1, n + 1):
    xor_all ^= i

# Tính XOR của các số nhập vào
xor_input = 0
for _ in range(n - 1):
    num = int(input())
    xor_input ^= num

# Số bị thiếu
missing_number = xor_all ^ xor_input
print(missing_number)
