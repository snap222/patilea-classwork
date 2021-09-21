print("enter a name:")
name = str(input())
length = len(name)
spaces = 0
for i in range(0,length):
    if name[i] == ' ':
        spaces += 1
print("the name is", length-spaces, "characters long")