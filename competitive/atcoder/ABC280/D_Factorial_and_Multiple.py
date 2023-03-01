def main():
    K = int(input())
    # Nの階乗がKの倍数となるような最小のNを出力せよ
    T_soin = get_soinsu(K)
    #print(T_soin)
    import collections
    counter = collections.Counter(T_soin)
    # 会場の最大値を調べる。2が10個、7が1個なら
    maxies = []
    for v, num in counter.items():
        count = 0
        for v_i in range(v, v*num+1, v):
            i = 1
            while True:
                if v_i % v**i != 0:
                    i += -1
                    break
                i += 1
            count += i
            if count >= num:
                maxies.append(v_i)
                break
    print(max(maxies))

def get_soinsu(N):
    T_soin = []
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
