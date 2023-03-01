def main():
    N, S = list(map(int, input().split(' ')))
    AB = [list(map(int, input().split(' '))) for i in range(N)]
    import copy
    org_stage=['']*(S+1)
    stage = copy.copy(org_stage)
    stage[0] = 'S'
    for i in range(N):
        omote = AB[i][0]
        ura = AB[i][1]
        next_stage = copy.copy(org_stage)
        for j in range(S):
            if stage[j]:
                if S >= j + omote:
                    next_stage[j + omote] = stage[j] + 'H'
                if S >= j + ura:
                    next_stage[j + ura] = stage[j] + 'T'
        stage = next_stage
    if stage[S]:
        print("Yes")
        print(stage[S][1:])
    else:
        print("No")

if __name__ == "__main__":
    main()
