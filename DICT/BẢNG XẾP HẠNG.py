if __name__ == "__main__":
    n = int(input())
    sv = {}
    for _ in range(n):
        ten = input()
        C, T = map(int, input().split())  
        sv[ten] = (C, T)
    sorted_list = sorted(sv.items(), key=lambda x : (-x[1][0], x[1][1], x[0]))
    for ten, (C, T) in sorted_list:
        print(f"{ten} {C} {T}")
    
    
    
    
        