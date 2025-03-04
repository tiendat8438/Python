from math import sqrt, pow, pi
a, b = map(float, input().split())
c = sqrt(a*a+b*b) # Cạnh huyền
r = (a+b-c)/2 # Bán kính của đường tròn nội tiếp đầu tiên
x = sqrt(pow(b-r,2) + r*r) # Khoảng cách từ cạnh b đến tâm đường tròn
k = (x-r)/(x+r) # tỉ lệ giảm dần của bán kính giữa các hình tròn tiếp theo.
p = 2*pi*pow(r,2)/(1-pow(k,2))/a/b # Tỉ lệ diện tích
print(f'{p:.4f}')