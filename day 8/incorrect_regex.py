import re
t = int(input())
for i in range(0, t):  
    try:
        s = input()
        result = (re.compile(s))
        print(bool(result))
    except re.error:
        print('False')
