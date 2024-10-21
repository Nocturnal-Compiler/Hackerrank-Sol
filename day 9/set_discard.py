n1 = int(input())
oper = set(map(int, input().split()))
n2 = int(input())

for i in range(n2):
    command = input().split()
    if len(command) > 1:
        act = int(command[1])
    
    if command[0] == "pop":
        oper.pop()
    if command[0] == "remove":
        oper.remove(act)
    if command[0] == "discard":
        oper.discard(act)

print(sum(oper))
