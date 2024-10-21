from collections import deque

t = int(input())

def piling(val):
    while val:
        large = None
        if val[-1] > val[0]:
            large = val.pop()
        else:
            large = val.popleft()
        
        if len(val) == 0:
            return "Yes"
        
        if val[-1] > large or val[0] > large:
            return "No"

for i in range(t):
    cubes = int(input())
    d = deque(map(int, input().split()))
    print(piling(d))
    
