def multiples():
    name = str(input("what is your name?"))
    print("enter the times table, start number and end number")
    times_table = int(input())
    start_num  = int(input())
    end_num = int(input())
    print("Hi", name, "here is your times table:")
    for i in range(start_num,end_num+1):
        print(times_table, "x", i, "=", times_table*i)
    
multiples()
