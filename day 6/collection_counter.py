from collections import Counter

n = int(input())

stock = list(map(int, input().split(" ")))

x = int(input())

counting_dict = Counter(stock)

p = 0

for i in range(x):
    size, price = map(int, input().split(' '))
    
    if counting_dict[size]:
        counting_dict[size] -= 1
        p = p+price
        
print(p)