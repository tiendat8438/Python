nums = []
while len(nums) < 10:
    line = input().strip()
    if line:
        nums.extend(map(int, line.split()))

remainders = set()
for num in nums:
    du = num % 42
    remainders.add(du)
print(len(remainders))