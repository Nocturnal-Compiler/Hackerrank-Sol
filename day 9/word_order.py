from collections import Counter
n = int(input())
lis = []

for i in range(n):
    s = input()
    lis.append(s)
    
presult = Counter(lis)
print(len(presult))

for i in presult.values():
    print(i, end=" ")
    
