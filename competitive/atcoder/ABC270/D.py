def main():
    N, K = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    dp = [[0, 0] for _ in range(N+1)]
    for a in A:
        dp[a][0] = a
        dp[a][1] = a
    # [0, 0, 2, 0, 5]を[0,0,2,2,5]みたいな形にする
    buf = 0
    for i in range(len(dp)):
        if dp[i][0]:
            buf = dp[i][0]
        else:
            dp[i][0] = buf
            dp[i][1] = buf
    #print(dp)
    for stone in range(N+1):
        #import pdb;pdb.set_trace()
        best = max([[syudan + dp[(stone-syudan)-dp[stone-syudan][1]][0], syudan] for syudan in A if syudan <= stone] + [[0,0]], key=lambda x: x[0])
        dp[stone][0] = best[0]
        dp[stone][1] = best[1]
        #print(dp)
    print(dp[N][0])

if __name__ == "__main__":
    main()
