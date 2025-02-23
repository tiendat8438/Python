import re
from collections import Counter

# Hàm kiểm tra số không giảm
def is_non_decreasing(n):
    s = str(n)
    return all(s[i] <= s[i+1] for i in range(len(s)-1))

# Hàm đọc file và chuyển về list số nguyên
def read_list_from_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read().strip()
        numbers = list(map(int, re.findall(r'\d+', content)))  # Tìm tất cả số nguyên trong file
    return numbers

# Xử lý file
def process_file(filename):
    data = read_list_from_file(filename)
    filtered_data = [num for num in data if is_non_decreasing(num)]
    return Counter(filtered_data)
import pickle
from collections import Counter

def is_non_decreasing(n):
    s = str(n)
    return all(s[i] <= s[i + 1] for i in range(len(s) - 1))

def read_data(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
    
def solve(file1, file2):
    data1 = read_data(file1)
    data2 = read_data(file2)
    counter1 = Counter(n for n in data1 if n >= 10 and is_non_decreasing(n))
    counter2 = Counter(n for n in data2 if n >= 10 and is_non_decreasing(n))
    count_vals = sorted(set(counter1.keys()) & set(counter2.keys()))
    for key in count_vals:
        print(key, counter1[key], counter2[key])

solve('DATA1.in', 'DATA2.in')


# Đọc dữ liệu từ hai file
file1 = "DATA1.in"
file2 = "DATA2.in"

counter1 = process_file(file1)
counter2 = process_file(file2)

# Tìm các số chung trong cả hai file
common_numbers = sorted(set(counter1.keys()) & set(counter2.keys()))

# Xuất kết quả
for num in common_numbers:
    print(num, counter1[num], counter2[num])
