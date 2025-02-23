N = int(input())
scores = list(map(float, input().split()))
filtered = [score for score in scores if score != max(scores) and score != min(scores)]
average = sum(filtered) / len(filtered)
print(f'{average:.2f}')