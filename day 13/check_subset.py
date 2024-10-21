n = int(input())

for i in range(n):
    n = int(input())
    set_a = set(map(int, input().split()))
    b = int(input())
    set_b = set(map(int, input().split()))
    
    if set_a.issubset(set_b):
        print(True)
    else:
        print(False)