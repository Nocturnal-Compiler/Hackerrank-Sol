from itertools import *

s = input()

for i, j in groupby(s):
    print(tuple([len(list(j)), int(i)]), end = " ")
