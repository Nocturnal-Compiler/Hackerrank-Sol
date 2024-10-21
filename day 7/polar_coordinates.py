import cmath

value = complex(input().strip())

result = cmath.polar(value)

for i in result:
    print(i)