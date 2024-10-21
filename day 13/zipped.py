n, x = map(int, input().split())
sheet = []
for _ in range(x):
    sheet.append(list(map(float, input().split())))
for i in zip(*sheet):
    print(sum(i) / x)