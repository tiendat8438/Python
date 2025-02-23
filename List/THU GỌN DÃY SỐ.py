if __name__ == '__main__':
    N = int(input())
    mylist = list(map(int, input().split()))
    stack = []
    for num in mylist:
        if stack and (stack[-1] + num) % 2 == 0:
            stack.pop()
        else:
            stack.append(num)
    print(len(stack))

