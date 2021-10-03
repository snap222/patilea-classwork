print("here are the three options for a car rental firm:")
print("1: Economy Car")
print("2: Saloon Car")
print("3: Sports Car")
choice = int(input())
if choice >=1 and choice <=3:
	print("do you wish to proceed or cancel?")
	choice2 = str(input())
	if choice2 == "proceed":
	 	print("response confirmed")
		print("have a nice day")
     #End If
else:
	print("invalid choice")
#End If
