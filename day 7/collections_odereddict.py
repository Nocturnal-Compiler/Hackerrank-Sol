from collections import OrderedDict

n = int(input())
d = OrderedDict()

for i in range(n):
    item, space, price = input().rpartition(" ")
    price = int(price)
    if item in d.keys():
        d[item] += price
    else:
        d[item] = price

for i in d.keys():
    print(i, d[i])