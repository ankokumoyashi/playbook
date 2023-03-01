import collections
def main():
    N = int(input())
    TXA = [list(map(int, input().split(' '))) for i in range(N)]
    dic = collections.defaultdict(lambda : 0)
    for t,x,a in TXA:
        dic[f'{t}_{x}'] = a
    dp = [[0 for i in range(5)] for i in range(10**5+1)]
    for i in range(10**5+1):
        for j in range(min(i+1, 5)):
            dp[i][j] = dic[f'{i}_{j}'] + max(dp[i-1][max(0, j-1): min(5, j+2)])
    print(max(dp[i]))

if __name__ == "__main__":
    main()
