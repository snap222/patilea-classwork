print("input the number of elements in the array:")
max = int(input())
name = [0] * max

for i in range(0, max):
    print("input a pupil name:")
    name[i] = str(input())
#next

print("input a name which you wish to find:")
find = str(input())
flag = False
for i in range(0,max):
    if name[i] == find:
        location = i
        flag = True
#next

if flag == True:
    print("the name", find, "has been has been found, its postition in the array is", location)
else:
    print("the name has not been found")
#end if