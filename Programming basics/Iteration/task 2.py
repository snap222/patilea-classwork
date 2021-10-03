Test1 = 0
Test2 = 0
Test3 = 0
Total = 0
Temp = 0

for i in range(1,31):
	Temp = int(input())
	Test1 = Test1 + Temp
#Next
Temp = 0
for i in range(1,31):
	Temp = int(input())
	Test2 = Test2 + Temp
#Next
Temp = 0
for i in range(1,31):
	Temp = int(input())
	Test3 = Test3 + Temp
#Next
Total = Test1 + Test2 + Test3
print("The average for test 1 is " & Test1/30)
print("The average for test 2 is " & Test2/30)
print("The average for test 3 is " & Test1/30)
print("The average test score for the whole year is " & Total/90)
