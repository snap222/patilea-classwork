def Pword():
    password = input("enter password:")
    while len(password) < 5 or len(password) > 9:
        print("Error. Password must be 6 to 8 characters long.")
        password = input("Enter password:")
    #endwhile
    password2 = input("enter password again:")
    while password != password2:
        print("Error - password don't match")
        password = input("Enter password:")
        while len(password) < 5 or len(password) > 9:
            print("Error. Password must be 6 to 8 characters long.")
            password = input("Enter password:")
        #endwhile
        password2 = input("Enter password again:")
    print("Password change succesful")
    #endwhile
#endprocedure
Pword()
