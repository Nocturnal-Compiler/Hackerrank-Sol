n = int(input())
A = set(map(int, input().split()))

for _ in range(int(input())):
    cmd, _ = input().split()
    B = set(map(int, input().split()))
    eval(f"A.{cmd}(B)")
print(sum(A))
