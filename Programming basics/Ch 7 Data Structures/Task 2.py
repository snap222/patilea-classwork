list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
list3 = []
index1 = 0
index2 = 0
while index1 < len(list1) and index2 < len(list2):
    if list1[index1] < list2[index2]:
        list3.append(list1[index1])
        index1 += 1
    else:
        list3.append(list2[index2])
        index2 += 1


print(list1)
print(list2)
print(list3)