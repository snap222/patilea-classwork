Exam_Grade = int(input())
Attendance = int(input())
if Attendance <= 90:
   print("fail")
   if Exam_Grade > 90:
      print("Grade = A")
   elif Exam_Grade > 80 and Exam_Grade <=90:
      print("Grade = B")
   elif Exam_Grade > 70 and Exam_Grade <=80:
      print("Grade = C")
   else:
      print("fail")
   #End If	
#End If
