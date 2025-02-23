# N = int(input())
# mylist = [input() for _ in range(N)]
# ans = []
# for line in mylist:
#     sum = 0
#     has_digit = False
#     for i in range(len(line)):
#         if line[i].isdigit():
#             sum = sum * 10 + int(line[i])
#             has_digit = True
#         else:
#             if has_digit:
#                 ans.append(sum)
#                 sum = 0
#                 has_digit = False
#     if has_digit:
#         ans.append(sum)
# sorted_ans = sorted(ans)
# print(*sorted_ans, sep='\n')


import re

N = int(input())
numbers = []

for _ in range(N):
    line = input()
    extracted_numbers = re.findall(r'\d+', line)  # Tìm tất cả chuỗi số liên tiếp
    numbers.extend(int(num) for num in extracted_numbers)  # Chuyển thành số nguyên và thêm vào danh sách

numbers.sort()  # Sắp xếp tăng dần

for num in numbers:
    print(num)