# #1 ---------------
# people1 = {
#    "John": 25,
#    "Emma": 30,
#    "Michael": 22,
#    "Sophia": 28,
#    "David": 35,
#    "Olivia": 26
# }
# #
# #N = int(input('put age: '))
# #
# #for key in people1:
# #    if people1[key] > N:
# #        print(key)
#
# #2 ----------------
# people2 = {
#    "25": "Jonh",
#    "30": "Emma",
#    "22": "Michael",
#    "28": "Sophia",
#    "35": "David",
#    "26": "Olivia",
# }
# #
# #N = int(input('put age: '))
#
# #for key in people2:
# #    if int(key) > N:
# #        print(people2[key])
#
# #3 -------
#
# for key in people2:
# 	people1[key] = people2[key]
#
# for i in people1.items():
# 	print(i)

#4 ---------------------------------
# MySet = (1, 5, 7, 9, 4, 2, 1, 7, 5, 2, 4)
# MyDic = {}
# for i in range(3):
# 	k = int(input("Введите число 0-9: "))
# 	MyDic[k] = MySet.count(k)
#
# for i in MyDic.items():
# 	print(i)

#5 ---------------------------------
# def FunSquare(digit):
# 	Dic = {}
# 	Dic[digit] = digit ** 2
# 	return Dic
#
# digit = int(input("Введите число: "))
# print(FunSquare(digit))

#6 ------------------------------------
Scrabble = {
	['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']: 1,
	['D', 'G']: 2,
	['B', 'C', 'M', 'P']: 3,
	['F', 'H', 'V', 'W', 'Y']: 4,
	['K']: 5,
	['J', 'X']: 8,
	['Q', 'Z']: 10
}

Word = str(input("Введите слово большими буквами на англ."))