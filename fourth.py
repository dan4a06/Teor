#1------------------------------
# lis = [2, 7, 15, 38, 2, 90, 54, 77, 23]
# print(1 + lis.index(max(lis)))


#2------------------------------
# lis = [-2, -7, -15, 38, -2, -90, 54, 77, -23]
# for i in lis:
#     if i > 0:
#         print(lis.index(i))
#         break
# else:
#     print("Такого элемента нет")


#3------------------------------
# lis = []
# for i in range(5): lis.append(input("Введите значение: "))
# print(lis)


#4------------------------------
# lis = [2, 7, 15, 38, 2]
# print(lis)
# lis[1], lis[3] = lis[3], lis[1]
# print(lis)

#5------------------------------
# lis = [2, 7, 15, 38, 2, 90, 54, 77, 23]
# print(lis)
# n = int(input("Введите число: "))
# if n in lis: print(lis.index(n)+1)
# else: print("Нема")

#6------------------------------
# lis = [2, 7, 15, 38, 2, 90, 54, 77, 23]
#
# def del_min(lis, n):
#     for i in range(n): lis.remove(min(lis))
#     return lis
#
# def del_max(lis, m):
#     for i in range(m): lis.remove(max(lis))
#     return lis
#
# n = int(input("Кол-во наим. элементов: "))
# m = int(input("Кол-во макс. элементов: "))
#
# print(lis)
# print(del_min(lis, n))
# print(del_max(lis, m))
# print(lis)


#7------------------------------
# s = input()
# lis = []
# for i in s.split(" "):
#     if not i in lis: lis.append(i)
#
# print(lis)


#8------------------------------
# def if_sort(lis):
#     if sorted(lis) == lis: return True
#     else: return False
#
#
# lis = [2, 7, 15, 38, 2, 90, 54, 77, 23]
# lis = [1, 2, 3]
# print(if_sort(lis))

#9------------------------------
def Fun(list):
    res = 0
    for i in list:
        res += list
    res = res / len(list)
    k = 0
    for i in list:
        if i > res:
            k+=1
    return k

#10-----------------------------
# lis1 = [2, 3, 4]
# lis2 = [1, 2, 3, 4, 5, 6]
#

# def one_in_one(lis1, lis2):
#     flag = True
#     if len(lis1) >= len(lis2):
#         for i in len2:
#             if i in lis1:
#
#             else:


# print(one_in_one(lis1, lis2))
# lis =[[],[],[]]
# for i in range(3):
#     for j in range(3):
#         if i - j == 0:
#             lis[i].append(1)
#         else:
#             lis[i].append(0)
#
# for i in lis:
#     for j in i:
#         print(j, end=" ")
#     print("\n")


lis =[[],[],[]]
for i in range(0, 3):
    for j in range(0, 3):
        lis[i].append((i+1)*(j+1))

for i in lis:
    for j in i:
        print(j, end=" ")
    print("\n")

