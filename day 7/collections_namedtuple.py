from collections import namedtuple

n = int(input())

data = namedtuple("data", input().split())

preavg_sum = 0
for i in range(n):
    preavg_sum += int(data(*input().split()).MARKS)

print(preavg_sum/n)