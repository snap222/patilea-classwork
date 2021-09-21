
def permutation(pin):
 
    if len(pin) == 0:
        return []
 
    if len(pin) == 1:
        return [pin]
 
    current_perm = [] 
    for i in range(len(pin)):
       m = pin[i]
 
       RemainingList = pin[0:i] + pin[i+1:len(pin)]
 
       for p in permutation(RemainingList):
            current_perm.append([m] + p)
 
 
data = list('123')
for p in permutation(data):
    print(p)