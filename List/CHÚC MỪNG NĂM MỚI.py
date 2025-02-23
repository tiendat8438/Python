if __name__ == '__main__':
    n = int(input())
    mylist = []
    for _ in range(n):
        s = input()
        mylist.append(s)
    print(len(set(mylist)))

