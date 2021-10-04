Outlet1Sales = [0] * 4
Outlet2Sales = [0] * 4
Outlet3Sales = [0] * 4

for i in range(0,4):
    print("input the total for quarter no.", i+1, "for Outlet1:")
    Outlet1Sales[i] = int(input())
#next

print("-----------")

for i in range(0,4):
    print("input the total for quarter no.", i+1, "for Outlet2:")
    Outlet2Sales[i] = int(input())
#next

print("-----------")

for i in range(0,4):
    print("input the total for quarter no.", i+1, "for Outlet3:")
    Outlet3Sales[i] = int(input())
#next

print("-----------")

for i in range(0,4):
    print("Total for quarter", i+1, Outlet1Sales[i]*1000, "for Outlet1")
#next

print("-----------")

for i in range(0,4):
    print("Total for quarter", i+1, Outlet2Sales[i]*1000, "for Outlet2")
#next

print("-----------")

for i in range(0,4):
    print("Total for quarter", i+1, Outlet3Sales[i]*1000, "for Outlet3")
#next