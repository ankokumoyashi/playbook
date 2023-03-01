import sys
sys.setrecursionlimit(3000000)

def main():
    N, M = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    memo = {}
    from functools import lru_cache
    counter = 0
    def dfs(from_i, depth):
        #print(depth)
        nonlocal counter
        memo_key=f"{depth}_{from_i}"
        if memo_key not in memo:
            if depth == M:
                counter += 1
                memo[memo_key] = max(A[from_i:]) * depth
            else:
                counter += 1
                memo[memo_key] = max([A[i]*depth + dfs(i+1, depth+1) for i in range(from_i, N-(M-depth))])
        return memo[memo_key]
    #= max([A[i]*depth + dfs(i+1, depth+1) for i in range(from_i, N-(M-depth))])
    #for from_i in range(N-M):
        #evals.append(dfs(from_i=from_i,depth=1))
    print(dfs(from_i=0,depth=1)) 
    print(counter)
if __name__ == "__main__":
    main()
