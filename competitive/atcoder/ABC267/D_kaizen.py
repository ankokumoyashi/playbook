def main():
    N, M = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    dp = [[-100000000000 for j in range(N)] for i in range(M)]
    buf = -1000000000000
    for j,a in enumerate(A):
        if a >= buf:
            buf = a
        dp[0][j] = buf
    for i in range(1, M):
        for j in range(i, N):
            #if j < i:
            #    continue
            # 数字が一個少ない時のi個取った時の最大と、
            dp[i][j]=max(dp[i][j-1], dp[i-1][j-1] + A[j]*(i+1))
            #print(dp)
    print(dp[M-1][N-1])

if __name__ == "__main__":
    main()
