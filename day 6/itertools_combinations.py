from itertools import combinations

S, k = input().split(" ")
k = int(k)
S = sorted(S)

for i in range(1, k+1):
    for variants in combinations(S, i):
        print("".join(variants))