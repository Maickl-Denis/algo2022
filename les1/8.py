#Определить, является ли год, который ввел пользователем, високосным или не високосным.

def dz3(year: int):
    if year % 4 == 0 and year % 100 != 0 or ((year % 400) == 0 and (year // 400) > 0):
        print("YES")
    else:
        print("NO")


#dz3(int(input('Введите год: ')))
dz3(400)
dz3(100)
dz3(1900)
dz3(2022)