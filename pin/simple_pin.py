num = int(input("number of digits in pin:"))
a = [0] * (num-1)
for i in range(0,num):
    a[i] = int(input("input digit number", i, ":"))


print(a)