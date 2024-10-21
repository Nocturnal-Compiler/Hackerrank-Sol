from collections import defaultdict

n, m = map(int, input().split(" "))

dict = defaultdict(list)

for i in range(n):
    raw = input().rstrip()
    dict[raw].append(i+1)
    
for i in range(m):
    raw = input().rstrip()
    if raw in dict:
        print(" ".join(map(str, dict[raw])))
    else:
        print("-1")