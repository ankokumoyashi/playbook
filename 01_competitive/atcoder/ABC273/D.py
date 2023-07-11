def main():
    H, W, rs, cs = list(map(int, input().split(' ')))
    N = int(input())
    rc = [list(map(int, input().split(' '))) for _ in range(N)]
    Q = int(input())
    #dl = [[*input(split(' '))] for _ in range(Q)]
    dl = [list(map(lambda x: (x[0], int(x[1])), [input().split()]))[0] for i in range(Q)]
    #rows = [[0, W+1] for _ in range(H)]
    #columns = [[0, H+1] for _ in range(W)]
    rows = dict()
    columns = dict()
    now = [rs, cs]
    import bisect
    for kabe in rc:
        if kabe[0]-1 not in rows:
            rows[kabe[0]-1] = [0, W+1]
        if kabe[1]-1 not in columns:
            columns[kabe[1]-1] = [0, H+1]
        rows[kabe[0]-1].append(kabe[1])
        columns[kabe[1]-1].append(kabe[0])
    rows = {k:sorted(row) for k,row in rows.items()}
    columns = {k:sorted(column) for k, column in columns.items()}
    for move in dl:
        # x成分の移動
        if move[0] == 'L':
            if now[0]-1 in rows:
                near_kabe = rows[now[0]-1][bisect.bisect_left(rows[now[0]-1], now[1])-1]+1
            else:
                near_kabe = 1
            now[1] = max(1, near_kabe, now[1] - move[1])
        if move[0] == 'R':
            if now[0]-1 in rows:
                near_kabe = rows[now[0]-1][bisect.bisect_left(rows[now[0]-1], now[1])]-1
            else:
                near_kabe = W
            now[1] = min(W, near_kabe, now[1] + move[1])
        if move[0] == 'U':
            if now[1]-1 in columns:
                near_kabe = columns[now[1]-1][bisect.bisect_left(columns[now[1]-1], now[0])-1]+1
            else:
                near_kabe = 1
            now[0] = max(1, near_kabe, now[0] - move[1])
        if move[0] == 'D':
            if now[1]-1 in columns:
                near_kabe = columns[now[1]-1][bisect.bisect_left(columns[now[1]-1], now[0])]-1
            else:
                near_kabe = H
            now[0] = min(H, near_kabe, now[0] + move[1])
        print(f"{now[0]} {now[1]}")

if __name__ == "__main__":
    main()
