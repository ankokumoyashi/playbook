def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    import collections
    herasenai = []
    heraseru_2 = []
    heraseru_3 = []
    heraseru_2_3 = []
    soinsus = []
    for i, a in enumerate(A, start=1):
        soinsu = get_soinsu(a)
        if i % 6 == 0:
            heraseru_2_3.append(soinsu)
            soinsus.append([n for n in soinsu if n != 2 and n!= 3])
        elif i % 2 == 0:
            heraseru_2.append(soinsu)
            soinsus.append([n for n in soinsu if n != 2])
        elif i % 3 == 0:
            heraseru_3.append(soinsu)
            soinsus.append([n for n in soinsu if n != 3])
        else:
            herasenai.append(soinsu)
            soinsus.append([n for n in soinsu])
    herasenai_max_2 = max([len([prime for prime in primes if prime == 2]) for primes in herasenai + heraseru_3])
    herasenai_max_3 = max([len([prime for prime in primes if prime == 3]) for primes in herasenai + heraseru_2])
    a = [len([prime for prime in primes if prime == 2]) - herasenai_max_2 for primes in heraseru_2]
    b = [len([prime for prime in primes if prime == 3]) - herasenai_max_3 for primes in heraseru_3]
    c = [len([prime for prime in primes if prime == 2]) - herasenai_max_2 for primes in heraseru_2_3]
    d = [len([prime for prime in primes if prime == 3]) - herasenai_max_3 for primes in heraseru_2_3]
    abcd = a + b + c + d
    if min(abcd) < 0:
        print(-1)
        exit()
    if not all([soinsus[0] == h for h in soinsus]):
        print(-1)
        exit()
    print(sum(abcd))

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
