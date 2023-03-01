#メイン
def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    dp_isum = 0
    for i in range(1, N+1):
        dp = [[[0 for _ in range(i)] for _ in range(i+1)] for _ in range(N+1)]
        dp[0][0][0] = 1
        # j番目のカードまで見る
        for j in range(N):
            # k個のカードを選択している状態
            for k in range(i+1):
                # 今見ているかーどを選択or非選択した場合の２分岐でdpを更新する。更新されるのはj+1とj+1,k+1
                for l in range(i):
                    dp[j+1][k][l] += dp[j][k][l]
                    # あまりに足して、再度あまりを求めると、全体からあまりを求めるのに等しい
                    if k != i:
                        dp[j+1][k+1][(l+A[j])%i] += dp[j][k][l]

        dp_isum += dp[N][i][0]
        # N個見た時にiで割って、あまりが0になるものの個数
        # これを1から100までの全てのiで足してあげれば良い
    print(dp_isum % 998244353)

if __name__ == "__main__":
    main()
