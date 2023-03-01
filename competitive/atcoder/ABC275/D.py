def main():
    N = int(input())
    memo = dict()
    memo[0] = 1
    def recursive(n):
        if n not in memo:
            memo[n] = recursive(n//2) + recursive(n//3)
        return memo[n]
    recursive(N)
    print(memo[N])

if __name__ == "__main__":
    main()
