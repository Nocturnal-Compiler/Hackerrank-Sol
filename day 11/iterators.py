from itertools import combinations

n = int(input())
n_chars = input().split()
k = int(input())

comb = list(combinations(n_chars, k))
count = 0
for i in comb:
    if 'a' in i:
        count += 1

print(count/len(comb))
