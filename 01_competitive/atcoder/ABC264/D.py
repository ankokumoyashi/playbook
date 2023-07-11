
#メイン
def main():
    S = input()
    def swap(s, a, b):
        return s[:a] + s[b] + s[a] + s[b+1:]
    memo = dict()
    from collections import deque
    memo['atcoder'] = 0
    q = deque([('atcoder', 0)])
    while q:
        s, counter = q.popleft()
        for i in range(0,6):
            swaped = swap(s, i,i+1)
            if swaped not in memo:
                memo[swaped] = counter+1
                q.append((swaped, counter + 1))
    print(memo[S])



if __name__ == "__main__":
    main()
