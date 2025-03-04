# tạo ra một chu kỳ lặp lại của các hệ số: 1 -2 3 -4 5
def get(i):
    if i%5==0: return 5
    return i%5*pow(-1,i%5-1)

for t in range(int(input())):
    n, k = map(int, input().split())
    m = 5*k # Số lượng phần tử cần xét trong dãy số
    # dp[i][j] sẽ lưu giá trị tối ưu khi xem xét i phần tử đầu tiên của chu kỳ và j phần tử đầu tiên của dãy số.
    a, dp = [0] + list(map(int, input().split())), [[0]*(n+1) for i in range(m+1)]
    for i in range(1,m+1):
        x = get(i)
        dp[i][i]=x*a[i]+dp[i-1][i-1]
        for j in range(i+1,n+1):
            dp[i][j]=max(dp[i][j-1], x*a[j]+dp[i-1][j-1])
    print(dp[m][n])
    

