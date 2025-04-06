def check(n):
    return n.count('2') > len(n) // 2

def solve(n):
    from queue import Queue
    q = Queue()
    q.put('1')
    q.put('2')
    res = []
    while not q.empty():    
        cur = q.get()
        if check(cur):
            res.append(cur)
            if len(res) == n:
                break

        if len(cur) < 20:
            q.put(cur + '0')
            q.put(cur + '1')
            q.put(cur + '2')
    return res

for _ in range(int(input())):
    n = int(input())
    print(' '.join(solve(n)))    