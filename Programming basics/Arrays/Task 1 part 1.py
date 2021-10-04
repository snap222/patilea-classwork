numbers = [0]*6
total = 0
print("input 6 integers")
for i in range(0,6):
    numbers[i] = int(input())
#next

print("-----------")
for i in range(5,-1,-1):
    print(numbers[i], sep='', end='')
    total += numbers[i]
#next

print(" ")
print("-----------")
print("the total is", total, "and the average is", total/6)


