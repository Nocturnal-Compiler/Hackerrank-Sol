from itertools import product

k, m = map(int, input().split())
n = []

for i in range(k):
    n.append(list(map(int, input().split()))[1:])
    
result = []

for i in product(*n):
    result.append(sum([x*x for x in i]) % m)

print(max(result))