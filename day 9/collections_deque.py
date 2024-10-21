from collections import deque

n = int(input())
de = deque()
for i in range(n):
    var = input().split()
    commands = var[0]
    
    if len(var) > 1:
        num = var[1]
        
    if commands == "append":
        de.append(num)
    elif commands == "pop":
        de.pop()
    elif commands == "appendleft":
        de.appendleft(num)
    elif commands == "popleft":
        de.popleft()

for i in de:
    print(i, end = " ")            
