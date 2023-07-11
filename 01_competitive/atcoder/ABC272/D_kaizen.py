from collections import deque

n,m = map(int, input().split()) 
mmap = [["-1"]*n for _ in range(n)]
num = [i**2 for i in range(n)]
can = []

for i in range(n):
    for j in range(i,n):
        if num[i] + num[j] == m:
            can += [(i,j),(i,-j),(-i,j),(-i,-j),(j,i),(j,-i),(-j,i),(-j,-i)]

q = deque([(0, 0, 0)])
visited = [[True]*n for _ in range(n)]
while q:
    i, j, d = q.popleft()
    if visited[i][j]:
        mmap[i][j] = d
        visited[i][j] = False
        mmap[j][i] = d
        visited[j][i] = False
        for ix,jx in can:
            ni = i + ix
            nj = j + jx
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj]:
                    q.append((ni, nj, d+1))

for line in mmap: 
    print(*line) 
