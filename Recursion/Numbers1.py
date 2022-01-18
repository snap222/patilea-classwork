numbers = [] 
n = int(input("how many numbers do yoou want in list?")) 
for i in range(n): 
    new_element = int(input("input a number:")) 
    numbers.append(new_element) 


total = 0
for i in range(n):
  total += numbers[n]

print(total)