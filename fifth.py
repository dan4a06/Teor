#1 ----------------------------------------
#Myset = {2, 5, 3, 11, 7, 6}
#pod_my_set = set()
#for i in Myset:
#    if i % 2 == 0:
#        pod_my_set.add(i)
#print(pod_my_set)

#2 ----------------------------------------
#my_set = {2, 5, 3, 11, 7, 6}
#for element in sorted(my_set):
#    print(element)

#3 ----------------------------------------
def count_unique_numbers(my_set):
    return len(set(my_set))

print(count_unique_numbers([3, 4, 10, 3, 2, 8, 2, 11]))
