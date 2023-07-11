#メイン
def main():
    N, K, D = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    #dp[i個目まで見える][j個選ぶような組み合わせ]:(最大, 総和, Dで割ったあまり)
    #dp = [[(0, 0) for j in range(K+1)] for i in range(N+1)]
    dp = [[[-1 for i in range(D)] for j in range(K+1)] for i in range(N+1)]
    #for l in range(D):
    dp[0][0][0] = 0
    #for i in range(N):
    #    dp[i][1][A[i]]

    for i in range(N):
        # iが1なら0こめまで見た状態。とりうる選択ずみは0と1+1ならok
        for j in range(min(i+1, K+1)):
            #for l in range(D):
            #    dp[i+1][j+1][l] = dp[i][j][l]
            for l in range(D):
                #dpijl = dp[i][j]
                # i個目を選ばずに据え置き
                dp[i+1][j][l] = max(dp[i][j][l], dp[i+1][j][l])
                # 新たなA[j]を足すことで、今まで作られてきた各あまりの中の最大値を更新する
                # あまりが100まで、同じあまりの値を大小で二つ持っておく必要がないので、同あまりの中ではdpできる
                # このように、一見dpできない(過去の状態を見に行かないといけないように見える)場合でも、
                # 保持する範囲を狭められる可能性がある。
                # K個より多くのjは選べないので次のiへ。(上の横移動はしたいのでこちらだけcontinue)
                if j == K:
                    continue
                #if j == 0:
                #    dp[i+1][j+1][A[i]%D] = A[i]
                #if i==2 and j==1:
                    #import pdb;pdb.set_trace()
                if dp[i][j][l] != -1:
                    #dp[i+1][j+1][(l+A[i])%D] = max(dp[i][j][l]+A[i], dp[i+1][j+1][(l+A[i])%D])
                    dp[i+1][j+1][(l+A[i])%D] = dp[i][j][l]+A[i]
                    #dp[i+1][j+1][l] = max(dp[i][j][l], dp[i+1][j+1][l])
    #import pdb;pdb.set_trace()
    #print(-1 if dp[N][K][0] == 0 else dp[N][K][0])
    print(dp[N][K][0])

if __name__ == "__main__":
    main()

"""
dp[i][j][l]: i個目までからj個選んでDで割った時のあまりlとなる最大の値
dp[i][j][(l+A[i])%D]: dp[i-1][j-1][l]+A[i] (たとえ小さくなろうともk個選んだ中で最大なら良い。比較は下のupdateで行う)
dp[i][j][(l+A[i])%D]: max(dp[i-1][j][l], dp[i])
"""
