N = int(input())
A = list(map(int, input().split(' ')))

count = sum([a < 0 for a in A])
abss = [abs(a) for a in A]

if count % 2 == 0:
    print(sum(abss))
else:
    print(sum(abss) - min(abss)*2)
