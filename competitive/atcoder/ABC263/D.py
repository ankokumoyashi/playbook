#メイン
from itertools import accumulate
def main():
    N, L, R = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    rev_A = A[::-1]
    A_minus_L = [L - a for a in A]
    A_minus_R = [R - a for a in A]
    L_accum = list(accumulate([0] + A_minus_L))
    R_accum = list(accumulate(A_minus_R[::-1]))[::-1] + [0]
    L_accum_min = list(accumulate(L_accum, min))
    R_accum_min = list(accumulate(R_accum[::-1], min))[::-1]
    accumus = []
    for l, r in zip(L_accum_min, R_accum_min):
        accumus.append(l+r)
    print(sum(A) + min(accumus))
    # A:       [  5, 5,  0 ,6 ]  
    # L_accum: [0,-2,-3,-4,-5]
    # R_accum: [  -5,-3,-4,-5,0]
if __name__ == "__main__":
    main()

