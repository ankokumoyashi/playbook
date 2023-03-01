N = int(input())
A = list(map(int, input().split(' ')))
Q = int(input())
Qs = [list(map(int, input().split(' '))) for i in range(Q)]

import collections
import numpy as np
A = np.array(A)
A_shape = A.shape
# Aに代入しない仕組みにする
dic = collections.defaultdict(lambda : 0)
for query in Qs:
    if query[0] == 1:
        dic = collections.defaultdict(lambda : 0)
        A = query[1]
    elif query[0] == 2:
        dic[query[1]-1] = dic[query[1]-1] + query[2]
    elif query[0] == 3:
        if type(A) == int:
            print(dic[query[1]-1] + A)
        else:
            print(dic[query[1]-1] + A[query[1]-1])
