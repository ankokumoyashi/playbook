def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    import collections
    herasenai = collections.Counter(get_soinsu(A[0]))
    counter = 0
    import pdb;pdb.set_trace()
    for i, a in enumerate(A[1:], start=2):
        soinsu = get_soinsu(a)
        if i%6 == 0:
            diff = collections.Counter(soinsu) - herasenai
            diff = collections.Counter(soinsu) - herasenai
            if set(diff) - set([2, 3]):
                print(-1)
                exit()
            counter += diff[2] + diff[3]
        elif i%2 == 0:
            diff = collections.Counter(soinsu) - herasenai
            if set(diff) - set([2]):
                print(-1)
                exit()
            counter += diff[2]
        elif i%3 == 0:
            diff = collections.Counter(soinsu) - herasenai
            if set(diff) - set([3]):
                print(-1)
                exit()
            counter += diff[3]
        else:
            if not collections.Counter(soinsu) == herasenai:
                print(-1)
                exit()
    print(counter)

def get_soinsu(N):
    T_soin = []
    if N == 1:
        return []
    while True:
        for k in range(2, int(N**(1/2))+1):
            if N % k == 0:
                T_soin.append(k)
                N = N // k
                break
        else:
            break
    T_soin.append(N)
    return T_soin
if __name__ == "__main__":
    main()
