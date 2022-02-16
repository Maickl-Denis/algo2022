#7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


def ravenstvo(n):

    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return factorial(n - 1) * n

    def uravnenie(n):
        return (n * (n+1))/2
    return factorial(n) == uravnenie(n)

num = 3
print(ravenstvo(num))
num = 4
print(ravenstvo(num))