def PrintDict(dic):
	for i in dic.items():
		print(i)

print("#1 ---------------")
people1 = {
   "John": 25,
   "Emma": 30,
   "Michael": 22,
   "Sophia": 28,
   "David": 35,
   "Olivia": 26
}

N = int(input('put age: '))

for key in people1:
   if people1[key] > N:
       print(key)

Skip = input("Введите любой")
print("#2 ----------------")
people2 = {
   "25": "Jonh",
   "30": "Emma",
   "22": "Michael",
   "28": "Sophia",
   "35": "David",
   "26": "Olivia",
}

N = int(input('put age: '))

for key in people2:
   if int(key) > N:
       print(people2[key])

Skip = input("Введите любой")
print("#3 -------")

for key in people2:
	people1[key] = people2[key]

PrintDict(people1)

Skip = input("Введите любой")
print("#4 ---------------------------------")
MySet = (1, 5, 7, 9, 4, 2, 1, 7, 5, 2, 4)
MyDic = {}
for i in range(3):
	k = int(input("Введите число 0-9: "))
	MyDic[k] = MySet.count(k)

for i in MyDic.items():
	print(i)

Skip = input("Введите любой")
print("#5 ---------------------------------")
def FunSquare(digit):
	Dic = {}
	Dic[digit] = digit ** 2
	return Dic

digit = int(input("Введите число: "))
print(FunSquare(digit))

Skip = input("Введите любой")
print("#6 ------------------------------------")
Scrabble = {
	"AEIOULNSTR": 1,
	"DG": 2,
	"BCMP": 3,
	"FHVWY": 4,
	"K": 5,
	"JX": 8,
	"QZ": 10,
}

Word = str(input("Введите слово большими буквами на англ.:"))
res = 0
for w in Word:
	for key in Scrabble:
		if w in key:
			res+=Scrabble.get(key)

print(res)

Skip = input("Введите любой")
print("#7 --------------------------------------")
School = {
	"1а": 20,
	"1б": 22,
	"2б": 25,
	"6а": 19,
	"7в": 21,
}
print("До изменений")
PrintDict(School)
print("Первое изменение добавили 2б")
School['2б'] = 23
PrintDict(School)
print("Второго изменения изменили 3а")
School['3а'] = 	17
PrintDict(School)
print("Третье изменение убрали 1б")
School.pop("1б")
PrintDict(School)

