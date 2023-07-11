#メイン
def main():
    # 固定数の数字
    N, M = list(map(int, input().split(' ')))
    # 可変数の数字
    X = list(map(int, input().split(' ')))
    CY = [list(map(int, input().split(' '))) for i in range(M)]
    from collections import defaultdict

    dic = defaultdict(lambda : 0)
    dic.update({c:y for c,y in CY})
    #dp[N][N]
    dp = [[0 for _ in range(N+1)] for _ in range(N)]
    dp[0] = [0, X[0]+dic[1]]
    _max = X[0] + dic[1]
    for i in range(1, N):
        for j in range(0, i+2):
            if j == 0:
                dp[i][j] = _max
                continue
            dp[i][j] = dp[i-1][j-1] + X[i] + dic[j]
            if _max < dp[i][j]:
                _max = dp[i][j]
    print(max(dp[N-1]))

if __name__ == "__main__":
    main()
