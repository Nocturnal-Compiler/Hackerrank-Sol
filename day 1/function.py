year = int(input())

def check_year(n):
    leap = False
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        leap = True
    else:
        leap = False
    print(leap)

check_year(year)