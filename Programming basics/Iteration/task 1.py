Total_Parts = 0
OldModel_Parts = 0
print("enter part number")
Num = int(input())
while Num != 9999:

    while Num//1000 < 1:
        print("invalid part number, enter number between 1000 and 9999")	
        Num = int(input())
    #End while

    Total_Parts = Total_Parts + 1

    if Num % 10 == 6 or Num % 10 == 7 or Num % 10 == 8:
            OldModel_Parts = OldModel_Parts + 1 
    #End if
    print("enter part number")
    Num = int(input())
#End While
print("there are", Total_Parts, "total parts")
print("there are", OldModel_Parts, "old model parts")
