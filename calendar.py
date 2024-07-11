import calendar

year = int(input("Введите год : "))
month = int(input("Введите меяц : "))

mycal = calendar.month(year,month)

print(mycal)
