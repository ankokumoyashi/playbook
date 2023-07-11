def main():
    N, M = list(map(int, input().split(' ')))
    #stage = np.zeros((N,N), dtype=np.int32)
    stage = [[0]*N for _ in range(N)]
    stage[0][0] = 1
    now = (0,0)
    def get_move_patern(M):
        paterns = []
        for a in range(int(M**(1/2))+1):
            for b in range(a, int(M**(1/2))+1):
                if (a**2 + b**2) == M:
                    paterns = paterns + [(a,b), (b,a), (-a, -b),(-b,-a),(-a,b),(b,-a),(a,-b),(-b,a)]
        return paterns
    paterns = get_move_patern(M)

    search_target = [(0,0,1)]
    while True:
        stage, search_target = update_stage(stage, paterns, N, search_target)
        #stage = (stage-1).astype(str)
        #for i in range(stage.shape[0]):
        #    print(' '.join(stage[i]))
        if not search_target:
            for i in range(len(stage)):
                print(*[j-1 for j in stage[i]])
        exit()

def update_stage(new_stage, paterns, N, search_target):
    #new_stage = stage.copy()
    next_search_target = search_target
    while next_search_target:
        search_target = next_search_target
        next_search_target = []
        for i, j, d in search_target:
            for patern in paterns:
                ni = i+patern[0]
                nj = j+patern[1]
                if 0 <= ni < N and 0 <= nj < N and not new_stage[ni][nj]:
                #if 0 <= ni < N and 0 <= nj < N:
                    new_stage[ni][nj] = d + 1
                    next_search_target.append((ni, nj, d+1))
    return new_stage, next_search_target

if __name__ == "__main__":
    main()
