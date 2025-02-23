for t in range(int(input())):
    n = int(input())
    s = float(input())
    arr = list(map(float, input().split()))
    a = {}
    for i in arr:
        if a.get(i) is None: a[i] = 1
        else: a[i]+=1
    a = [[i, a[i]] for i in sorted(a)] # gom nhóm các giá trị giống nhau và tần xuất xuất hiện của chúng    
    while len(a)>1:
        dis = a[1][0]-a[0][0] # tìm dìf của số đằng trước nó để hợp nhất các giá trị
        if s>dis*a[0][1]:
            s-=dis*a[0][1] # trừ đi giá trị thêm vào phần tử tiếp theo khi hợp nhất
            a[1][1] += a[0][1] # hợp nhất các giá trị
            a.pop(0) # xóa đi giá trị đã được hợp nhất
        else: break
    a[0][0] += s/a[0][1] # phân bổ các giá trị s còn lại 
    ans = 1 # Tính kết quả theo ct: ∏(x^freq)
    for i in a:
        ans*=i[0]**i[1]
    print(f'{min(1, ans):.6f}')