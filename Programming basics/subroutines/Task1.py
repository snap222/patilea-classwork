name = input("what is your name:")
print("enter table, start num and end num:")
table = int(input())
startnum = int(input())
endnum = int(input())
def multiples():
    print("Hi", name,"here is your times table")
    for i in range(startnum,endnum+1):
        num = (i*table)
        print(table,"x",i,"=",num)
    #next i
#end procedure
multiples()
