import calendar

month, date, year = map(int, input().split(" "))

date = calendar.weekday(year, month, date)

if (date==0):
    print("MONDAY")
elif(date==1):
    print("TUESDAY")
elif(date==2):
    print("WEDNESDAY")
elif(date==3):
    print("THURSDAY")
elif(date==4):
    print("FRIDAY")
elif(date==5):
    print("SATURDAY")
elif(date==6):
    print("SUNDAY")