# a = int(input())
# if a < 0: print(a*(-1))
# else: print(a)


#2---------------------------------
# a = int(input("Первое число: "))
# b = int(input("Второе число: "))
# if a > b: print("Минимум: ", b)
# else: print("Минимум: ", a)


#3-----------------------------
# a = int(input("Первое число: "))
# b = int(input("Второе число: "))
# c = int(input("Третье число: "))
# if a > b:
#     if a>c: print(a)
#     else: print(c)
# else:
#     if b > c: print(b)
#     else: print(c)


#4---------------------------------
# x = int(input("Введите x: "))
# y = int(input("Введите y: "))
#
# if x*y>0:
#     if x>0: print("Первая четверть")
#     else: print("Третья четверть")
# else:
#     if x>0: print("Четвёртая четверть")
#     else: print("Вторая четверть")


#5----------------------------------
# min_summa = 102
# minute = int(input("Кол-во изр. минут: "))
# sms = int(input("Кол-во изр. смс: "))
#
#
# def dop(all_minute=0, all_sms=0):
#     Stoim_min = (all_minute-100)*2.2 + (all_minute-100)*0.26
#     Stoim_sms = (all_sms-15)*1.7 + (all_sms-15)*0.26
#     return Stoim_min+Stoim_sms
#
#
# if minute <= 100 and sms <= 15: print("Стоимость услуг за месяц = 102 руб")
# else: print("Стоимость услуг за месяц = ", 102 + dop(minute, sms), " руб")


#6----------------------------------------------
# Kol = int(input("Кол - во чисел: "))
# res = 0
# kol = Kol
# while(kol>0):
#     kol -= 1
#     digit = int(input("Число: "))
#     res += digit
#
# print(res/Kol)


# 7---------------------------------------------
# n = int(input())
# for i in range(1, n+1, 2): print(i)


#8---------------------------
# def polynomial_value(coefficients, x):
#     n = len(coefficients) - 1  # Степень многочлена
#     result = 0
#     for i in range(n + 1):
#         result += coefficients[i] * (x ** (n - i))
#     return result
#
# print(polynomial_value(3, 5))


#9-------------------------------
# def max_three(a,b,c):
#     a = int(input("Первое число: "))
#     b = int(input("Второе число: "))
#     c = int(input("Третье число: "))
#     if a > b:
#         if a>c: print(a)
#         else: print(c)
#     else:
#         if b > c: print(b)
#         else: print(c)


#10--------------------
def Prov(a, b, c):
    if a*b*c>0:
        if a<c+b and b<a+c and c<b+a:
            print("Всё верно")
        else: print("Не прав. стор.")
    else: print("Стороны доджны быть положительными")