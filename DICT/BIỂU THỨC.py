def bracket_numbering(expression):
    stack = []
    result = []
    counter = 1  # Số thứ tự của cặp ngoặc

    numbering = {}  # Lưu thứ tự của dấu '(' tại mỗi vị trí

    for i, char in enumerate(expression):
        if char == '(':
            stack.append(counter)
            numbering[i] = counter
            counter += 1
        elif char == ')':
            if stack:
                numbering[i] = stack.pop()

    # In thứ tự của các cặp dấu ngoặc theo đúng thứ tự xuất hiện trong biểu thức
    output = [str(numbering[i]) for i in range(len(expression)) if expression[i] in "()"]
    return " ".join(output)


# Đọc dữ liệu đầu vào
T = int(input())  # Số bộ test

for _ in range(T):
    expr = input().strip()
    print(bracket_numbering(expr))
