N, M = list(map(int, input().split(' ')))
A = list(map(int, input().split(' ')))
A = sorted(A)
in_M_minus_1 = M-1 in A
in_0 = 0 in A
spree = []
sum_each_spree = []
spree.append(A[0])
for a in A[1:]:
    if (spree[-1]+1 % M) == a or spree[-1] == a:
        spree.append(a)
    else:
        sum_each_spree.append(sum(spree))
        spree = []
        spree.append(a)

sum_each_spree.append(sum(spree))
if in_M_minus_1 and in_0 and len(sum_each_spree) >=2:
    sum_each_spree[0] = sum_each_spree[-1] + sum_each_spree[0]
print(sum(A) - max(sum_each_spree))
