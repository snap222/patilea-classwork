movementGround = int(input())
movementFirst = int(input())
Trigger = int(input())
if (movementGround == 1 or movementFirst == 1) and Trigger == 1:
 	alarm = 1
	if movementGround == 1:
            print("the intruder is on the ground floor")
	#End If
	if movementFirst == 1:
		    print("the intruder is on the first floor")
	#End If
#End If
