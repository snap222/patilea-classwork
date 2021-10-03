temp = int(input("do you have a temperature?"))
if temp == "yes":
	Sore_Throat = int(input("is your throat sore?"))
	if Sore_Throat == "yes":
		print("you may have a throat infection")
		Cough = int(input("do you have a cough?"))
		if Cough == "yes":
			print("you have a chest infection")
		#End If
	elif Sore_Throat == "no":
		print("you have a fever")
	#End If
elif temp == "no":
    print("you are likely healthy")
#End If
	
