import collections
import itertools
import re
def main():
    N, M = list(map(int, input().split(' ')))
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    paterns = dict()
    dic = dict()
    # 全ての可能な組み合わせを列挙
    for perm in list(itertools.permutations(S)):
        joined = '_'.join(perm)
        paterns[joined] = perm
        dic[joined] = []
    # 全てのTを最小限の_を付与してグループ分け
    syukutai_under = re.compile('_+')
    for s in T:
        keyword = syukutai_under.sub('_', s)
        if keyword in dic:
            dic[keyword].append(s)
    under_bar_re = re.compile('_+')
    min_patern = min(dic.items(), key=lambda x: len(x[1]))[0]
    min_perm = paterns[min_patern]
    cand = []
    for i in range(16 - len(min_patern) +1):
        for ubp in itertools.product(range(N-1), repeat=i):
            default = [1 for i in range(N-1)]
            for ind in ubp:
                default[ind] += 1
            #cand_str.append(''.join([i+j for i,j in zip(min_perm[:-1], default)] + min_perm[-1]))
            cand.append(''.join([str(i) for i in default]))
    used_under_bar_pattern = [''.join([str(len(i)) for i in under_bar_re.findall(s)]) for s in dic[min_patern]]
    can_use = set(cand) - set(used_under_bar_pattern)
    if can_use:
        can_use = [int(i) for i in list(can_use)[0]]
        hoge = ''.join(tuple(i+int(j)*'_' for i,j in zip(min_perm[:-1], can_use)) + min_perm[-1:])
        if len(hoge) >= 3:
            print(hoge)
        else:
            print(-1)
    else:
        print(-1)

    # 自由に動かせる_の数
    #zan_moji = 16 - len(min_patern) - (len(min_perm) - 1)

    

if __name__ == "__main__":
    main()
