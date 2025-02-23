n = int(input())
questions_by_topic = {}
current_topic = None

for _ in range(n):
    line = input().strip()
    if not line:  # Dòng trống, bỏ qua
        current_topic = None
        continue

    if current_topic is None:
        current_topic = line
        questions_by_topic[current_topic] = 0
    else:
        questions_by_topic[current_topic] += 1

for topic, count in questions_by_topic.items():
    print(f"{topic}: {count}")
