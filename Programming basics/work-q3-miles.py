print("input the car mileage the last time the car was filled:")
car_mileage_past = int(input())
print("the car mileage now:")
car_mileage_now = int(input())
print("the total number of litres taken to fill the tank:")
litres_total = int(input())
gallons_total = litres_total * 4.546

car_mileage_diff = car_mileage_now - car_mileage_past
consumption = (car_mileage_diff/gallons_total)

print("the number of miles per gallon the car is doing is", consumption)