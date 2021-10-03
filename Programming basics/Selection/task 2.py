print("enter value of order")
Total_Value = int(input())
print("do you want guaranteed next day delivery?")
if input == "Yes":
   GNDD = 1
else:
   GNDD = 2
#End If
if Total_Value >= 15.00 and GNDD == 1:
   print("the postage charge is “ & 5.00")
   print("the overall total charge is " & Total_Value + 5.00)
elif Total_Value >= 15.00 and GNDD == 2:
   print("the postage charge is " & 0.00)
   print("the overall total charge is " & Total_Value)
elif Total_Value < 15.00 and GNDD == 1:
   print("the postage charge is " & 8.50)
   print("the overall total charge is " & Total_Value + 8.50)
else:
   print("the postage charge is " & 3.50)
   print("the overall total charge is " & Total_Value + 3.50)
#End If	
