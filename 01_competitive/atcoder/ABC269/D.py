def main():
    N = int(input())
    XY = [tuple(map(int, input().split(' '))) for i in range(N)]
    import copy
    checked_XY = []
    count = 0
    for xy in XY:
        if xy not in checked_XY:
            count += 1
            dfs(xy[0], xy[1], XY, checked_XY)
    print(count)

def dfs(i, j, XY, checked_XY):
    checked_XY.append((i, j))
    if (i-1,j-1) in XY and (i-1,j-1) not in checked_XY:
        dfs(i-1, j-1, XY, checked_XY)
    if (i-1,j) in XY and (i-1,j) not in checked_XY:
        dfs(i-1, j, XY, checked_XY)
    if (i,j-1) in XY and (i,j-1) not in checked_XY:
        dfs(i, j-1, XY, checked_XY)
    if (i+1,j+1) in XY and (i+1,j+1) not in checked_XY:
        dfs(i+1, j+1, XY, checked_XY)
    if (i+1,j) in XY and (i+1,j) not in checked_XY:
        dfs(i+1, j, XY, checked_XY)
    if (i,j+1) in XY and (i,j+1) not in checked_XY:
        dfs(i, j+1, XY, checked_XY)

if __name__ == "__main__":
    main()

